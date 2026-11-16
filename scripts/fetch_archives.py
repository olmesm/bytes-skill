#!/usr/bin/env python3
"""Download every Bytes newsletter issue into data/.

  data/html/NNN.html  raw page as served
  data/md/NNN.md      cleaned Markdown with frontmatter (issue, title, date, url)
  data/index.json     one record per issue

Re-runnable: issues already on disk are skipped unless --force is given.
Requires: beautifulsoup4, markdownify.
"""
import argparse
import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

BASE = "https://bytes.dev/archives"
ROOT = Path(__file__).resolve().parent.parent / "data"
UA = "Mozilla/5.0 (compatible; newsletter-archive-reader/1.0)"


def get(url, tries=4):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            if attempt == tries - 1:
                raise
            time.sleep(2 ** attempt)
    return None


def issue_numbers():
    html = get(BASE)
    return sorted({int(n) for n in re.findall(r"/archives/(\d+)", html)})


def to_markdown(n, html):
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    title = h1.get_text(" ", strip=True) if h1 else ""
    meta = h1.find_next("div").get_text(" ", strip=True) if h1 else ""
    m = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4})", meta)
    date = m.group(1) if m else ""
    post = soup.find("div", class_="post")
    if post is None:
        return None, None
    for tag in post.find_all(["style", "script"]):
        tag.decompose()
    body = markdownify(str(post), heading_style="ATX", bullets="-").strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    rec = {"issue": n, "title": title, "date": date, "url": f"{BASE}/{n}",
           "words": len(body.split())}
    front = "\n".join(["---", f"issue: {n}", f"title: {json.dumps(title)}",
                       f"date: {json.dumps(date)}", f"url: {rec['url']}", "---", ""])
    return rec, f"{front}\n# {title}\n\n{body}\n"


def fetch(n, force):
    raw = ROOT / "html" / f"{n:03d}.html"
    try:
        if raw.exists() and not force:
            html = raw.read_text()
        else:
            html = get(f"{BASE}/{n}")
            raw.write_text(html)
            time.sleep(0.3)
        rec, md = to_markdown(n, html)
        if rec is None:
            return n, None, "no post body"
        (ROOT / "md" / f"{n:03d}.md").write_text(md)
        return n, rec, None
    except Exception as e:  # noqa: BLE001
        return n, None, str(e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-download existing issues")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    (ROOT / "html").mkdir(parents=True, exist_ok=True)
    (ROOT / "md").mkdir(parents=True, exist_ok=True)

    nums = issue_numbers()
    print(f"{len(nums)} issues listed ({nums[0]}..{nums[-1]})")
    records, failed = [], []
    with ThreadPoolExecutor(args.workers) as ex:
        for n, rec, err in ex.map(lambda n: fetch(n, args.force), nums):
            if err:
                failed.append((n, err))
            else:
                records.append(rec)
    (ROOT / "index.json").write_text(json.dumps(records, indent=1) + "\n")
    print(f"ok: {len(records)}  failed: {len(failed)}")
    for n, err in failed:
        print(f"  #{n}: {err}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
