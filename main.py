#!/usr/bin/env python3
"""make.fun entry: "Alien Field Notes: The Two Day Earth Review".

A one-line review of Earth, filed by a visitor from elsewhere. The
program's only task is to write that review into entry.txt in the
output directory, exactly as it stands here and with no trailing
newline.
"""

import os

REVIEW = (
    "Two stars. They domesticated wolves into animals that wear "
    "sweaters, then built entire festivals around apologising to "
    "them. Would visit again."
)


def file_review(text: str) -> None:
    # Write the note exactly as composed: no newline is appended, so the
    # file ends on the review's closing words.
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as stream:
        stream.write(text)


if __name__ == "__main__":
    file_review(REVIEW)
