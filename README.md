# AWS SAA-C03 Knowledge Base (Automated)

This repo turns your raw study notes into a searchable, pretty documentation site and deploys it with GitHub Pages.

## How it works

1. Put raw notes in `notes_raw/` as `.txt` files.
2. On push, GitHub Actions runs `scripts/transform_notes.py` which creates Markdown in `docs/` organized by topics (IAM, EC2, EBS, EFS).
3. MkDocs builds a static site from `docs/`.
4. The site is deployed to GitHub Pages automatically.

## One-time setup

1. Create a repo named `aws-saa-c03-knowledgebase` (or any name).
2. Copy this project into it and push to `main`.
3. In GitHub: **Settings → Pages → Build and deployment: GitHub Actions**.
4. Wait for the first workflow to finish; your site will appear at `https://<your-username>.github.io/<repo>/`.

## Adding new notes

- Drop a new `.txt` into `notes_raw/` (e.g., `2025-10-28_ec2_networking.txt`).
- Commit and push. The pipeline will re-build the docs and deploy.

## Local preview

```bash
pip install mkdocs mkdocs-material
python scripts/transform_notes.py
mkdocs serve
```

Open http://127.0.0.1:8000

## Customize topics

Edit `TOPIC_MAP` in `scripts/transform_notes.py` to add S3, VPC, RDS, etc.

## License

Choose the license you prefer (MIT is common for notes). See `LICENSE` if provided.
