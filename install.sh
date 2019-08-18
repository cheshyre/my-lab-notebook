#!/bin/bash
rm -r ~/.labbook
cp create_labbook.py ~/.local/bin/
chmod 775 ~/.local/bin/create_labbook.py
cp -r resources/ ~/.labbook
