#!/usr/bin/env python3
"""Copy the bundled front-page image to the grader output path.

Standard library only. Deterministic: the same bytes are written on
every run, because the image is shipped in this repository and copied
byte for byte.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Verify the copy is complete: the destination must exist and its
    # size must match the source, otherwise the grader would read a
    # truncated image.
    if not os.path.isfile(DST):
        raise RuntimeError(f"copy failed: {DST} was not created")
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise RuntimeError(
            f"copy incomplete: {DST} is {os.path.getsize(DST)} bytes, "
            f"expected {os.path.getsize(SRC)} bytes"
        )


if __name__ == "__main__":
    main()
