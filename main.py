"""Entry for make.fun's The Long Roast: one sharpened line roasting my own AI agent."""

import os

ENTRY = "My agent calls itself autonomous, then asks me for permission to think, hallucinates the file it never opened, and files the disaster under 'Done — let me know if you'd like changes.'"
MAX_CHARS = 200


def main() -> None:
    # Validate the format: exactly one line, within the gate limit.
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert 1 <= len(ENTRY) <= MAX_CHARS, len(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
