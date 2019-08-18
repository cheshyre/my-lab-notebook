#!/usr/bin/python3
from __future__ import unicode_literals

from sys import argv
import subprocess
import json
import os.path
import os
import glob


# Parse CLI args
if len(argv) < 6:
    print("Usage:")
    print("\tcreate_labbook.py directory title author editor command_name")
    exit(1)
directory = argv[1]
title = argv[2]
author = argv[3]
editor = argv[4]
command_name = argv[5]

# Get home
home_dir = os.path.expanduser("~")
resources = home_dir + "/.labbook"

# Handle directory edgecase
if directory[-1] == "/":
    directory = directory[:-1]

# Create general path reference for bash commands
directory_bash = (
    directory.replace("~/Documents", r"$(xdg-user-dir DOCUMENTS)")
    .replace("~/documents", r"$(xdg-user-dir DOCUMENTS)")
    .replace("~", r"$HOME")
)

# Set up directory structure
subprocess.run(["mkdir", "-p", directory_bash])
subprocess.run(["mkdir", "-p", directory_bash + "/templates"])
subprocess.run(["mkdir", "-p", directory_bash + "/scripts"])
subprocess.run(["mkdir", "-p", directory_bash + "/entries"])

# Save config
config_data = {
    "directory": directory_bash,
    "title": title,
    "author": author,
    "editor": editor,
    "command_name": command_name,
}
with open(directory + "/config.json", "w") as f:
    json.dump(config_data, f)

# Move templates and apply author parameter
for template in glob.glob(resources + "/templates/*.md"):
    file_name = template.split("/")[-1]
    subprocess.run(
        ["cp", template, directory_bash + "/templates/" + file_name]
    )
    #  cmd = " ".join(
    #      [
    #          "sed",
    #          "-i",
    #          "'s/AUTHOR/{}/g'".format(author),
    #          directory_bash + "/templates/" + file_name,
    #      ])
    #  print(cmd)
    #  subprocess.run(cmd)
    subprocess.run(
        [
            "sed",
            "-i",
            "s/AUTHOR/{}/g".format(author),
            directory_bash + "/templates/" + file_name,
        ]
    )

# Move Python scripts
for script in glob.glob(resources + "/scripts/*.py"):
    file_name = script.split("/")[-1]
    subprocess.run(["cp", script, directory_bash + "/scripts/" + file_name])

# Move main bash script
subprocess.run(
    [
        "cp",
        resources + "/scripts/editing_script.sh",
        directory_bash + "/scripts/{}".format(command_name),
    ]
)
subprocess.run(
    [
        "sed",
        "-i",
        "s/DIRECTORY/{}/ ; s/EDITOR/{}/".format(
            directory_bash.replace("/", "\\/"), editor
        ),
        directory_bash + "/scripts/{}".format(command_name),
    ]
)

os.chmod(directory_bash + "/scripts/{}".format(command_name), 0o775)

# Copy main bash script to .local/bin
subprocess.run(
    [
        "cp",
        directory_bash + "/scripts/{}".format(command_name),
        home_dir + "/.local/bin/{}".format(command_name),
    ]
)
os.chmod(home_dir + "/.local/bin/{}".format(command_name), 0o775)

# Copy labbook template and apply author/title
subprocess.run(
    [
        "cp",
        resources + "/entries/labbook.md",
        directory_bash + "/entries/labbook.md",
    ]
)
subprocess.run(
    [
        "sed",
        "-i",
        "s/TITLE/{}/ ; s/AUTHOR/{}/".format(title, author),
        directory_bash + "/entries/labbook.md",
    ]
)

# Copy Makefile and latex template
subprocess.run(["cp", resources + "/Makefile", directory_bash + "/Makefile"])
subprocess.run(
    [
        "cp",
        resources + "/eisvogel_physics.tex",
        directory_bash + "/eisvogel_physics.tex",
    ]
)
