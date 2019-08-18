"""Script to create individual PDFs."""
from __future__ import unicode_literals

from sys import argv
import glob
import subprocess

# Support for only compiling single file
if len(argv) < 2:
    files = list(glob.glob("entries/*/*/*/*.md"))
else:
    files = argv[1:]

for file in files:
    out = file.replace("entries", "pdf").replace(".md", ".pdf")
    path = "/".join(out.split("/")[:-1])
    subprocess.run(["mkdir", "-p", path])
    subprocess.run(
        [
            "pandoc",
            file,
            "-o",
            out,
            "--template",
            "./eisvogel_physics.tex",
            "--listings",
        ]
    )

