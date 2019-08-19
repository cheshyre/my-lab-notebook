sources = $(wildcard entries/*/*/*/*.md)
targets = $(subst entries,pdf,$(subst .md,.pdf,$(sources)))

all: pdf/labbook.pdf $(targets)

test:
	echo $(targets)

.SECONDEXPANSION:

$(targets) : % : $$(subst pdf,entries,$$(subst .pdf,.md,$$@))
	python3 scripts/make_individual_pdfs.py $<

pdf/labbook.pdf: % : entries/labbook.md $$(subst pdf,entries,$$(subst .pdf,.md,$$@))
	python3 scripts/make_labbook_pdf.py
