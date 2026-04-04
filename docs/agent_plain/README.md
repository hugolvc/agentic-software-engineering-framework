# Plain-text export for RAG (optional)

This folder documents how to produce **lean plain text** from the framework’s Markdown for embeddings and retrieval—without maintaining a full duplicate tree of `.md` files.

## Approach

Run the repository script from the framework root:

```bash
python3 scripts/rag_strip_markdown.py README.md
python3 scripts/rag_strip_markdown.py 01_agent_based_software_engineering_process_description/01_04_process_workflow.md
```

Pipe a whole tree from your shell (example):

```bash
find . -name '*.md' -not -path './.venv/*' | while read -r f; do
  mkdir -p "plain/$(dirname "$f")"
  python3 scripts/rag_strip_markdown.py "$f" > "plain/${f%.md}.txt"
done
```

Keep emoji in output (if you prefer):

```bash
python3 scripts/rag_strip_markdown.py --keep-emoji README.md
```

## Scope

The stripper removes common Markdown syntax, fenced-code fences (keeps inner text), many emoji blocks, and light HTML. It is **best-effort** for chunking, not a full CommonMark renderer.
