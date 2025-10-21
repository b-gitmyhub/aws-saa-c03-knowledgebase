#!/usr/bin/env python3
import pathlib, re, csv, json, random

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
QUIZ_DIR = DOCS_DIR / "quizzes"
FLASHCARDS_DIR = REPO_ROOT / "flashcards"
QUIZ_DIR.mkdir(parents=True, exist_ok=True)
FLASHCARDS_DIR.mkdir(parents=True, exist_ok=True)

def extract_entries(md_text):
    entries, current = [], None
    for line in md_text.splitlines():
        h = re.match(r'^### (.+)', line)
        if h:
            if current: entries.append(current)
            current = {"heading": h.group(1).strip(), "lines": []}
        elif current is not None and line.strip():
            current["lines"].append(line.strip())
    if current: entries.append(current)
    return entries

def read_topics():
    topics = {}
    for md in sorted(DOCS_DIR.glob("*.md")):
        if md.name == "index.md": 
            continue
        topics[md.stem] = md.read_text(encoding="utf-8")
    return topics

def to_flashcards(topics):
    cards = []
    for topic, text in topics.items():
        for entry in extract_entries(text):
            heading = entry["heading"]
            bullets = [re.sub(r'^[-*]\s*', '', l) for l in entry["lines"] if re.match(r'^[-*]\s+', l)]
            if bullets:
                for b in bullets:
                    cards.append((f"{topic}: {heading} — What about this?", b))
            else:
                for l in entry["lines"]:
                    if ":" in l or "→" in l:
                        parts = re.split(r':|→', l, maxsplit=1)
                        if len(parts) == 2:
                            cards.append((f"{topic}: {parts[0].strip()}", parts[1].strip()))
                body = "\n".join(entry["lines"]).strip()
                if body:
                    cards.append((f"{topic}: {heading}", body))
    return cards

def to_quizzes(topics, per_topic=6):
    rng = random.Random(1337)
    quizzes = {}
    for topic, text in topics.items():
        entries = extract_entries(text)
        facts = []
        for e in entries:
            for l in e["lines"]:
                m = re.match(r'^[-*]\s+(.*)', l)
                if m: facts.append(m.group(1).strip())
        facts = list(dict.fromkeys(facts))
        qs = []
        for e in entries[:per_topic]:
            local = [re.sub(r'^[-*]\s*', '', l).strip() for l in e["lines"] if re.match(r'^[-*]\s+', l)]
            if not local and facts:
                local = [facts[rng.randrange(len(facts))]]
            if not local:
                continue
            correct = local[0]
            distractors = [f for f in facts if f != correct]
            rng.shuffle(distractors)
            distractors = distractors[:3]
            options = [correct] + distractors
            rng.shuffle(options)
            answer = options.index(correct)
            qs.append({"question": f"{topic}: {e['heading']}", "options": options, "answer": answer})
        quizzes[topic] = qs
    return quizzes

def write_flashcards(cards):
    (FLASHCARDS_DIR / "anki.csv").write_text(
        "Front,Back\n" + "\n".join([f'"{f.replace("\"","\"\"")}","{b.replace("\"","\"\"")}"' for f,b in cards]),
        encoding="utf-8"
    )
    (FLASHCARDS_DIR / "anki.json").write_text(
        json.dumps([{"front":f,"back":b} for f,b in cards], ensure_ascii=False, indent=2), encoding="utf-8"
    )

def write_quizzes(quizzes):
    index_lines = ["# Quizzes\n"]
    for topic, qs in quizzes.items():
        md = [f"# {topic} Quiz", "", "> Choose the best answer.", ""]
        for i, q in enumerate(qs, 1):
            md.append(f"**Q{i}. {q['question']}**")
            for j, opt in enumerate(q["options"]):
                md.append(f"- {chr(65+j)}. {opt}")
            md.append(f"<details><summary>Answer</summary>\n\n**{chr(65+q['answer'])}**\n\n</details>\n")
        (QUIZ_DIR / f"{topic}.md").write_text("\n".join(md), encoding="utf-8")
        index_lines.append(f"- [{topic}](./{topic}.md)")
    (QUIZ_DIR / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

def main():
    topics = read_topics()
    cards = to_flashcards(topics)
    write_flashcards(cards)
    quizzes = to_quizzes(topics)
    write_quizzes(quizzes)
    print(f"Generated {len(cards)} flashcards and {sum(len(v) for v in quizzes.values())} quiz questions.")

if __name__ == "__main__":
    main()
