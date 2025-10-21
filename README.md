# AWS SAA-C03 Knowledge Base

> A living, self-updating knowledge system for the AWS Solutions Architect Associate (SAA-C03) exam.

## Vision

This project began as handwritten notes and evolved into an automated learning environment.
Each new note—whether text, OCR, or quick snippet—flows through a Python pipeline
that cleans, organizes, and publishes it into a searchable documentation site.

Goal: study once, retain forever.  
Method: automation, reflection, and incremental improvement.  
Inspired by: Applied Systems Automation for Knowledge Architectures.

## How It Works

1. Raw Input → drop study notes (`.txt`) into `/notes_raw/`
2. Transformation → `scripts/transform_notes.py` routes content into topics (IAM, EC2, EBS, EFS)
3. Output → Markdown files in `/docs/` with headings and index
4. Publishing → GitHub Actions builds privately now; can deploy later to GitHub Pages

## Folder Structure

aws-saa-c03-knowledgebase/
├── notes_raw/         # Source notes
├── docs/              # Generated Markdown
├── scripts/           # Transformation logic
├── .github/
│   └── workflows/     # Automation (CI/CD)
├── mkdocs.yml         # MkDocs configuration
└── README.md

## Local Usage (Private Mode)

pip install mkdocs mkdocs-material
python scripts/transform_notes.py
mkdocs serve

Browse locally at http://127.0.0.1:8000.

## Going Public Later

1. Set repo visibility → Public  
2. Enable GitHub Pages (Settings → Pages → GitHub Actions)  
3. Push → your site appears at  

https://<your-username>.github.io/aws-saa-c03-knowledgebase/

## Learning Philosophy

"Automation is not about removing humans from the loop—it’s about amplifying human intent."

Every `.txt` file you add expands your knowledge base and chronicles your progress as a learning engineer.

## License

This work is licensed under the  
[Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE).

You may share and adapt these materials for non-commercial purposes.  
Commercial use requires permission from the author.

## Contributions

Feel free to fork and extend.  
Follow the topic-mapping convention in `scripts/transform_notes.py`.

## Author

Iulian B.
 
GitHub → [@b-gitmyhub](https://github.com/b-gitmyhub)
