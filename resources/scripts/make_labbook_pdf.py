"""Script to create full labbook PDF."""
from __future__ import unicode_literals

import glob
import subprocess

files = list(glob.glob("entries/*/*/*/*.md"))

subprocess.run(["mkdir", "-p", "pdf"])
subprocess.run(["mkdir", "-p", "temp"])

for file in files:
    file_name = file.split("/")[-1]
    subprocess.run(["cp", file, "temp/" + file_name])
    subprocess.run(
        [
            "sed",
            "-i",
            r"s/^#/##/g ; /^---/d ; 2{N;N;s/\n/ #/g} ; s/^title: /#/g ; s/#author: / (/g ; s/#date: .*/&)/g ; s/#date: /, /g",
            "temp/" + file_name,
        ]
    )


files = sorted(list(glob.glob("temp/*.md")))

# Complete pandoc compilation
first_part = ["pandoc", "entries/labbook.md"]
last_part = [
    "-o",
    "pdf/labbook.pdf",
    "--template",
    "./eisvogel_physics.tex",
    "--listings",
    "--number-sections",
]
subprocess.run(first_part + files + last_part)

# Delete temp directory
subprocess.run(["rm", "-r", "temp"])
