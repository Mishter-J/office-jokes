"""Office Jokes — make.fun entry.

Writes one original one-line joke about office life to
/output/entry.txt. The joke was picked from six candidates drafted
for this bounty: the winner sets up a team-building trust fall, then
lands on the one thing the company still will not trust its staff
with — the Wi-Fi password. It is a genuine one-line office joke with
a surprise turn at the end, and it rings true about office life.

The program self-checks the gate before writing: the entry must be
UTF-8 text of 1 to 199 characters, a single line, not only
whitespace. Output is deterministic: the same bytes every run.
"""

import os

JOKE = (
    "Our team-building exercise was trust falls, which is brave for a "
    "company that still hasn't trusted us with the Wi-Fi password."
)


def validate(text: str) -> None:
    """Enforce the competition gate locally; fail loudly, never silently."""
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry must be 1-199 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
