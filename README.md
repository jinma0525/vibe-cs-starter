# 60-Minute Constrained Sampling Starter Project

Method-agnostic interview kit: make `Qwen/Qwen3-0.6B` only output words
from the Oxford 3000 vocabulary.

## How to start

1. **Click the green `Use this template` button** (top-right of this page) → choose **`Create a new repository`**.
   - Owner: your own GitHub account
   - Name: anything (e.g. `vibe-cs-<yourname>`)
   - Visibility: **Public** is simplest. If you choose **Private**, add `jinma0525` as a collaborator afterwards (Settings → Collaborators).
2. Open the **new repo you just created**, then click **`Code` → `Codespaces` → `Create codespace on main`**.
   - Build takes ~3 min: installs `torch` + `transformers` and pre-downloads `Qwen/Qwen3-0.6B` weights (~1.2 GB).
   - Default machine size is 4-core / 8 GB, which is enough.
3. Read [CANDIDATE_TASK.md](CANDIDATE_TASK.md), then implement `generate()` in [src/solution.py](src/solution.py). You have **60 minutes**.
4. When you're done, commit and push from the Codespace terminal:
   ```bash
   git add -A
   git commit -m "submit"
   git push
   ```
5. Send the **URL of your new repo** (e.g. `https://github.com/<you>/vibe-cs-<yourname>`) to the interviewer.

> ⚠️ Do **not** click "Open in a codespace" directly on this template page — that creates a throwaway codespace with no way to push your code back. Always go through "Use this template → Create a new repository" first.

## Files

| Path | Purpose |
|---|---|
| [CANDIDATE_TASK.md](CANDIDATE_TASK.md) | Full problem spec and rules |
| [src/solution.py](src/solution.py) | **Implement `generate(prompt, max_new_tokens)` here** |
| [src/validator.py](src/validator.py) | Helpers expressing the rules as code |
| [src/oxford3000_tokens_normalized.txt](src/oxford3000_tokens_normalized.txt) | Allowed vocabulary |
