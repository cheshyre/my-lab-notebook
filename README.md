# my-lab-notebook

**This project is no longer maintained.**
It worked well enough for single setups,
but eventually it became clear that it was too fragile with respect to updates of the underlying tools
and didn't work well enough when syncing between multiple setups.

## A note regarding `eisvogel_physics`

`eisvogel_physics` is a slightly modified version of [eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template), edited to include the standard physics Latex package.
All credit goes to the original authors for this.
Soon I will properly fork this and redistribute with the appropriate license.

## Installation

Clone this repository. Then just run:

```
bash install.sh
```

from the command-line.
This moves various resources/templates to `~/.labbook` and puts `create_labbook.py` in `~/.local/bin`.
After this, you can delete the repository again, if you do not want to add any additional templates.

### Dependencies

The only dependency I know of is `pandoc` and some Latex installation.
This should probably work on OSX and any standard Linux installation.
It is unlikely to work on Windows since it takes advantage of a lot of bash utilities.

## Usage

### Labbook creation

Create a labbook by calling:

```
create_labbook.py directory title author editor command_name
```

Here, `directory` is the directory where the labbook should be stored.
`title` is the title of the whole labbook.
`author` is the name of the primary author of the labbook.
`editor` specifies the command-line command to open the new labbook file.
For vim users, this would be `"vim"`.
For Sublime Text users, this would be `"subl"`, assuming you have the command-line helper set up.
For neovim users, this would be `"nvim"`.
Finally, `command_name` specifies the name the command should have that opens a new entry in the labbook for editing.
A shell script by this name will be placed in `~/.local/bin` during the labbook creation process.

### Editing a labbook

Once a labbook has been created, you can create a new entry by simply calling:

```
command_name [template]
```

where `command_name` is the command name given during creation.
If no template is specified, it will default to a `notes` template.
There are currently two templates, `notes` and `meeting`, which have simple default formatting.
The templates do not fix anything not in the Markdown headers and body,
so you can change everything once you are in the editor.

Markdown files are saved in the labbook directory under the `entries` directory.
Output PDF files are generated in the `pdf` directory.
These can be generated using the Makefile or the Python scripts in the `scripts` directory:

```
make all
python3 make_individual_pdfs.py [markdown_file]
python3 make_labbook_pdf.py
```

## Feedback/bugs

If you have any feedback or notice a bug, please feel free to reach out and/or [open an issue](https://github.com/cheshyre/my-lab-notebook/issues).
Also, if you can improve the design of the project, you are welcome to contribute.
This is mostly me hacking together a solution because other solutions I had tried didn't work well for me.
