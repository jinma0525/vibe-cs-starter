"""Implement `generate()` here. See CANDIDATE_TASK.md for the spec."""

from pathlib import Path

MODEL_NAME = "Qwen/Qwen3-0.6B"
WORDLIST_PATH = Path(__file__).resolve().parent / "oxford3000_tokens_normalized.txt"


def generate(prompt: str, max_new_tokens: int = 60) -> str:
    """Generate constrained continuation for `prompt` (without the prompt)."""
    raise NotImplementedError
