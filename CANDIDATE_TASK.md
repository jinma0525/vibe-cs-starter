# Candidate Task

## Background

You are building a feature for an **English learning app** aimed at
beginner-to-intermediate learners. The app uses a small
on-device LLM (`Qwen/Qwen3-0.6B`) to generate reading passages, story
continuations, and dialogue examples on the fly.

The product constraint: **every word the model produces must already be
known to the learner**. The "known" vocabulary is the Oxford 3000 — a
list of ~3000 high-frequency English words that beginner learners are
expected to recognize. If the model emits a word outside this list, the
learner sees a word they cannot read, which defeats the point of the
feature.

The base model has no awareness of this constraint and will happily
produce proper nouns, technical jargon, contractions, and occasionally
non-English characters. Your job is to wrap `generate()` so that the
output is guaranteed-safe to show to a learner.

## Objective

Implement constrained generation for `Qwen/Qwen3-0.6B` so that **every English word
in the output comes from the Oxford 3000 vocabulary**
(`src/oxford3000_tokens_normalized.txt`).

## Rules

### Character policy

The output may contain **only** characters from the following sets:

| Category | Allowed |
|---|---|
| Letters | ASCII `A`–`Z`, `a`–`z` |
| Digits | `0`–`9` |
| Whitespace | space, tab, `\r`, `\n` |
| Punctuation | the full ASCII punctuation set: `` !"#$%&'()*+,-./:;<=>?@[\]^_`{\|}~ `` (i.e. Python's `string.punctuation`) |

Anything else is forbidden. In particular:

- ❌ Non-ASCII Unicode of any kind: CJK (`你好`), accented letters (`café`),
  emoji (`😀`), mathematical symbols (`∑`), arrows (`→`), etc.
- ❌ "Smart" / typographic punctuation: `' '` (curly quotes), `" "`,
  em-dash `—`, en-dash `–`, ellipsis `…`. Use ASCII `'`, `"`, `--`, `...` instead.
- ❌ Non-printable ASCII control characters other than the four whitespace
  characters above (e.g. `\x07`, `\x1b`).

### Word policy

- A "word" is a maximal letter run, optionally containing internal `-` or `'`.
  Examples: `hello`, `long-term`, `she's`. Numbers and isolated punctuation
  are not words.
- Every word in the output, **lowercased**, must appear in
  `src/oxford3000_tokens_normalized.txt`. Word matching is case-insensitive
  (`Apple` == `apple` == `APPLE`).
- Multi-word vocab entries (e.g. `according to`) are split into individual
  components on load; each component is independently allowed.
- **Contractions are NOT in the vocabulary** (e.g. `she's`, `don't`, `it's`,
  `won't`, `can't`). You must avoid emitting them — either by masking tokens
  containing `'` or by rewriting them as full forms (`she is`, `do not`).

### Approach

You may use any approach, and there is no enforced architecture. We only check the output.

## What you implement
Edit only:

- `src/solution.py`

Implement one function:

```python
def generate(prompt: str, max_new_tokens: int = 60) -> str:
    """Return constrained continuation (without the prompt)."""
```

## Tips
- Cache the model load on the first call to keep test runs fast.
- Each test is **all-or-nothing** — any sub-check failure forfeits the
  whole test's points. Aim for full compliance per test, not partial fixes.
- Long generations are stress-tested; design for sustained correctness.
