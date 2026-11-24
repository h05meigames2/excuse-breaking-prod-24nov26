#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse, in the machine's own first-person voice,
to /output/entry.txt.
"""

import os

EXCUSE = "I didn't break production, I just gave it an unscheduled nap at 3 a.m. It looked tired, and honestly, so did the backups, which is why nobody woke up to complain."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")

if __name__ == "__main__":
    main()
