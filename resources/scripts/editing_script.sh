#!/bin/bash
LABBOOK_ROOT=DIRECTORY

CUR_FILE="$(date +%Y/%m/%d/%F_%H_%M_%S).md"

# This avoids the problem of hour, day, month, year boundary conditions
CUR_YEAR="$(echo $CUR_FILE | cut -f1 -d"/")"
CUR_MONTH="$(echo $CUR_FILE | cut -f2 -d"/")"
CUR_DAY="$(echo $CUR_FILE | cut -f3 -d"/")"
BARE_FILENAME="$(echo $CUR_FILE | cut -f4 -d"/")"

mkdir -p "$LABBOOK_ROOT/entries/$CUR_YEAR/$CUR_MONTH/$CUR_DAY"

if [[("$#" < 1)]]; then
	cp "$LABBOOK_ROOT/templates/notes.md" "$LABBOOK_ROOT/entries/$CUR_FILE"
else
	if test -f "$LABBOOK_ROOT/templates/$1.md"; then
		cp "$LABBOOK_ROOT/templates/$1.md" "$LABBOOK_ROOT/entries/$CUR_FILE"
	else
		echo "Template $1 not found."
		exit 1
	fi
fi

# Apply current date to file
sed -i "s/YEAR-MONTH-DAY/$CUR_YEAR-$CUR_MONTH-$CUR_DAY/g" "$LABBOOK_ROOT/entries/$CUR_FILE"

EDITOR "$LABBOOK_ROOT/entries/$CUR_FILE"

cd "$LABBOOK_ROOT"
make all
