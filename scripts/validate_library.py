"""Validate the skill catalog, frontmatter, local links and ZIP packages.

Install scripts/requirements-validation.txt, then run from the repository root:
python scripts/validate_library.py
This validates artifacts, not end-to-end investigation or detector efficacy.
"""
import json
from pathlib import Path
import re
import zipfile
import yaml

ROOT = Path(__file__).resolve().parents[1]


def heading_anchor(text):
    return re.sub(r'[^\w\s-]', '', text.lower()).replace(' ', '-')


def validate(root=ROOT):
    catalog = json.loads((root / 'community-catalog.json').read_text(encoding='utf-8'))
    skills = catalog['skills']
    assert len(skills) == catalog['total_skills'] == 150
    assert len({item['id'] for item in skills}) == len(skills)
    assert len(list((root / 'skills').rglob('SKILL.md'))) == len(skills)
    assert len(list((root / 'dist/chatgpt').glob('*.zip'))) == len(skills)
    byte_matches = 0
    newline_equivalent = 0

    for item in skills:
        path = root / item['source']
        text = path.read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        assert match, ('Frontmatter', item['id'])
        front = yaml.safe_load(match[1])
        assert front['name'] == item['id'] == path.parent.name
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', front['name'])
        assert len(front['name']) <= 64
        assert isinstance(front['description'], str) and 0 < len(front['description']) <= 1024
        assert '[TODO:' not in text

        expected = {
            p.relative_to(path.parent).as_posix(): p.read_bytes()
            for p in path.parent.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts
        }
        with zipfile.ZipFile(root / item['chatgpt_zip']) as archive:
            assert archive.testzip() is None
            assert len(archive.namelist()) == len(set(archive.namelist()))
            assert all(
                name.startswith(item['id'] + '/') and '..' not in Path(name).parts
                for name in archive.namelist()
            )
            actual = {
                name.removeprefix(item['id'] + '/'): archive.read(name)
                for name in archive.namelist()
            }
        assert set(actual) == set(expected), ('ZIP files', item['id'])
        if actual == expected:
            byte_matches += 1
        else:
            for name, raw in expected.items():
                if actual[name] != raw:
                    assert actual[name].decode('utf-8').replace('\r\n', '\n') == raw.decode('utf-8').replace('\r\n', '\n'), ('ZIP text', item['id'], name)
            newline_equivalent += 1

    for doc in root.rglob('*.md'):
        for target in re.findall(r'\]\(([^\s)]+)\)', doc.read_text(encoding='utf-8')):
            if '://' in target:
                continue
            file, _, fragment = target.partition('#')
            linked = (doc.parent / file).resolve() if file else doc
            assert linked.exists(), ('Missing link', str(doc), target)
            if fragment and linked.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+)$', linked.read_text(encoding='utf-8'), re.M)
                assert fragment in {heading_anchor(h) for h in headings}, ('Missing heading', str(doc), target)

    return dict(
        skills=len(skills),
        zips=len(skills),
        source_zip_byte_matches=byte_matches,
        source_zip_newline_equivalent=newline_equivalent,
        frontmatter='passed',
        local_links='passed',
    )


if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
