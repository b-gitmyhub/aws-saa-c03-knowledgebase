#!/usr/bin/env python3
import re, os, sys, pathlib, datetime, hashlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
NOTES_DIR = REPO_ROOT / "notes_raw"
DOCS_DIR = REPO_ROOT / "docs"

TOPIC_MAP = {
    "IAM": ["IAM", "MFA", "Access", "Role", "Permissions", "Password Policy"],
    "EC2": ["EC2", "AMI", "Instance Connect", "User Data", "ASG"],
    "EBS": ["EBS", "Snapshot", "Volume", "Multi-Attach", "Encryption"],
    "EFS": ["EFS", "NFS", "Storage Class", "Throughput", "Performance"],
}

def slugify(title:str)->str:
    s = re.sub(r'[^a-zA-Z0-9\s-]', '', title).strip().lower()
    s = re.sub(r'\s+', '-', s)
    return s

def route_paragraph(p:str)->str:
    # choose topic by keyword match count
    scores = {t:0 for t in TOPIC_MAP}
    up = p.upper()
    for topic, kws in TOPIC_MAP.items():
        for kw in kws:
            if kw.upper() in up:
                scores[topic] += 1
    topic = max(scores, key=scores.get)
    # default to EC2 if all zero but contains EC2-like terms
    return topic

def ensure_header(md_path: pathlib.Path, title:str):
    if not md_path.exists():
        md_path.write_text(f"# {title}\n\n> Auto-generated from raw notes.\n\n## Contents\n\n", encoding="utf-8")

def append_section(md_path: pathlib.Path, heading:str, text:str):
    with md_path.open("a", encoding="utf-8") as f:
        f.write(f"\n### {heading}\n\n{text.strip()}\n")

def split_into_blocks(text:str):
    # split on page markers and headings
    parts = re.split(r'(?:^|\n)--- Page \d+ ---\n', text)
    blocks = []
    for part in parts:
        if part.strip():
            # further split by double newlines to get logical chunks
            chunks = [c.strip() for c in re.split(r'\n{2,}', part) if c.strip()]
            blocks.extend(chunks)
    return blocks

def main():
    DOCS_DIR.mkdir(exist_ok=True, parents=True)
    # reset docs (keep index later)
    for p in DOCS_DIR.glob("*.md"):
        if p.name != "index.md":
            p.unlink()
    topics_files = {}
    for topic in TOPIC_MAP:
        path = DOCS_DIR / f"{topic}.md"
        ensure_header(path, topic)
        topics_files[topic] = path

    # read notes
    raw_files = sorted(NOTES_DIR.glob("*.txt"))
    if not raw_files:
        print("No raw notes found.", file=sys.stderr)
        sys.exit(1)

    for rf in raw_files:
        text = rf.read_text(encoding="utf-8")
        for block in split_into_blocks(text):
            # use the first line as heading if it looks like a heading
            lines = block.splitlines()
            heading = lines[0][:80]
            # keep full block
            topic = route_paragraph(block)
            append_section(topics_files[topic], heading, block)

    # build index.md with TOC
    index = ["# AWS SAA-C03 Knowledge Base",
             "",
             "> This site is auto-generated from `/notes_raw` via `scripts/transform_notes.py`.",
             "",
             "## Table of Contents"]
    for topic in sorted(TOPIC_MAP.keys()):
        md = topics_files[topic].read_text(encoding="utf-8")
        # collect headings
        headings = re.findall(r'^### (.+)$', md, flags=re.MULTILINE)
        index.append(f"- [{topic}]({topic}.md)")
        for h in headings[:15]:
            index.append(f"  - [{h}]({topic}.md##{slugify(h)})")
    (DOCS_DIR / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
