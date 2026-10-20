"""Validate catalog, skill frontmatter, local links, packages and original hashes.

Install scripts/requirements-validation.txt, then run from the repository root:
python scripts/validate_library.py
This validates artifacts, not end-to-end investigation or detector efficacy.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import zipfile
import yaml

ROOT=Path(__file__).resolve().parents[1]


def git_hash(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def heading_anchor(text):
    return re.sub(r'[^\w\s-]','',text.lower()).replace(' ','-')


def validate(root=ROOT):
    catalog=json.loads((root/'community-catalog.json').read_text(encoding='utf-8'))
    skills=catalog['skills']
    assert len(skills)==catalog['total_skills']==150
    assert len({s['id'] for s in skills})==150
    assert Counter(s['release_status'] for s in skills)=={'preserved-original':44,'new-reference-reviewed':106}
    assert len(list((root/'skills').rglob('SKILL.md')))==150
    assert len(list((root/'dist/chatgpt').glob('*.zip')))==150
    new_zip_exact=0
    original_zip_exact=0
    newline_compatible=0
    for item in skills:
        path=root/item['source']
        text=path.read_text(encoding='utf-8')
        match=re.match(r'^---\n(.*?)\n---\n',text,re.S)
        assert match,('Frontmatter',item['id'])
        front=yaml.safe_load(match[1])
        assert front['name']==item['id']==path.parent.name
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',front['name'])
        assert len(front['name'])<=64
        assert isinstance(front['description'],str) and 0<len(front['description'])<=1024
        assert '[TODO:' not in text
        expected={p.relative_to(path.parent).as_posix():p.read_bytes() for p in path.parent.rglob('*')
                  if p.is_file() and '__pycache__' not in p.parts}
        with zipfile.ZipFile(root/item['chatgpt_zip']) as z:
            assert z.testzip() is None
            assert len(z.namelist())==len(set(z.namelist()))
            assert all(n.startswith(item['id']+'/') and '..' not in Path(n).parts for n in z.namelist())
            archived={n.removeprefix(item['id']+'/'):z.read(n) for n in z.namelist()}
        assert set(archived)==set(expected),('ZIP files',item['id'])
        exact=archived==expected
        if item['release_status']=='new-reference-reviewed':
            assert exact,('New ZIP bytes',item['id'])
            new_zip_exact+=1
        elif exact:
            original_zip_exact+=1
        else:
            for name,raw in expected.items():
                if archived[name]!=raw:
                    assert archived[name].decode('utf-8').replace('\r\n','\n')==raw.decode('utf-8').replace('\r\n','\n'),('Original ZIP text',item['id'],name)
            newline_compatible+=1
    for doc in root.rglob('*.md'):
        for target in re.findall(r'\]\(([^\s)]+)\)',doc.read_text(encoding='utf-8')):
            if '://' in target: continue
            file,_,fragment=target.partition('#')
            linked=(doc.parent/file).resolve() if file else doc
            assert linked.exists(),('Missing link',str(doc),target)
            if fragment and linked.suffix=='.md':
                headings=re.findall(r'^#{1,6}\s+(.+)$',linked.read_text(encoding='utf-8'),re.M)
                assert fragment in {heading_anchor(h) for h in headings},('Missing heading',str(doc),target)
    original=json.loads((root/'docs/original-44-manifest.json').read_text(encoding='utf-8'))
    for item in original['files']:
        assert git_hash((root/item['path']).read_bytes())==item['sha'],('Original changed',item['path'])
    return dict(skills=150,new_skills=106,preserved_skills=44,zips=150,
                original_files_hash_preserved=len(original['files']),
                new_zip_byte_matches=new_zip_exact,original_zip_byte_matches=original_zip_exact,
                original_zip_newline_equivalent=newline_compatible,
                frontmatter='passed',local_links='passed')


if __name__=='__main__': print(json.dumps(validate(),indent=2))
