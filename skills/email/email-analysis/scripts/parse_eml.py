"""Read an .eml as data and print a bounded JSON summary. No network or payload execution."""

import argparse
import json
import re
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
from pathlib import Path

MAX_BYTES = 10 * 1024 * 1024
MAX_BODY_CHARS = 100_000
URL_RE = re.compile(r"(?:https?://|hxxps?://)[^\s<>\"']+", re.IGNORECASE)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src", "action"} and value:
                self.links.append({"tag": tag, "attribute": key, "value": value})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("eml", type=Path, help="Path to a local .eml file")
    args = parser.parse_args()
    if args.eml.stat().st_size > MAX_BYTES:
        parser.error("Email exceeds the 10 MiB parsing limit")

    msg = BytesParser(policy=policy.default).parsebytes(args.eml.read_bytes())
    result = {"source": str(args.eml), "headers": list(msg.raw_items()), "parts": [], "urls": []}
    seen_urls = set()
    for part in msg.walk():
        if part.is_multipart():
            continue
        item = {
            "content_type": part.get_content_type(),
            "disposition": part.get_content_disposition(),
            "filename": part.get_filename(),
        }
        payload = part.get_payload(decode=True)
        item["size_bytes"] = len(payload) if payload is not None else 0
        if part.get_content_disposition() != "attachment" and part.get_content_maintype() == "text":
            try:
                body = part.get_content()
            except (LookupError, UnicodeError, ValueError):
                body = (payload or b"").decode("utf-8", errors="replace")
            item["body"] = body[:MAX_BODY_CHARS]
            for url in URL_RE.findall(body):
                seen_urls.add(url.rstrip(".,;!?)"))
            if part.get_content_type() == "text/html":
                links = LinkParser()
                links.feed(body[:MAX_BODY_CHARS])
                item["html_links"] = links.links
                seen_urls.update(link["value"] for link in links.links)
        result["parts"].append(item)
    result["urls"] = sorted(seen_urls)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

