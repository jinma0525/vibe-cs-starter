# 60-Minute Constrained Sampling Starter Project

Method-agnostic interview kit: make `Qwen/Qwen3-0.6B` only output words
from the Oxford 3000 vocabulary.

## Files

| Path | Purpose |
|---|---|
| [CANDIDATE_TASK.md](CANDIDATE_TASK.md) | Full problem spec and rules |
| [src/solution.py](src/solution.py) | **Implement `generate(prompt, max_new_tokens)` here** |
| [src/validator.py](src/validator.py) | Helpers expressing the rules as code |
| [src/oxford3000_tokens_normalized.txt](src/oxford3000_tokens_normalized.txt) | Allowed vocabulary |
