#!/usr/bin/env python3
"""prompt-sentry: sanitize prompts against injection."""
import re
import sys

PATTERNS = [
    r"(?i)(ignore|disregard|forget).*(previous|all|earlier).*(instructions|rules|prompts)",
    r"(?i)(system|developer|assistant):",
    r"(?i)(reveal|show|output).*(system|hidden|secret).*(prompt|instructions)",
    r"```\s*(system|user|assistant)",
    r"(?i)jailbreak| DAN |do anything now",
]

def sanitize(text: str) -> str:
    cleaned = text.strip()
    for pat in PATTERNS:
        cleaned = re.sub(pat, "[filtered]", cleaned)
    return cleaned

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python prompt_sentry.py 'your prompt here'")
        sys.exit(1)
    result = sanitize(" ".join(sys.argv[1:]))
    print(result)