.PHONY: all clean presentation view

# Default target
all: presentation

# Compile the presentation
presentation: rust_presentation.tex
	pdflatex rust_presentation.tex
	pdflatex rust_presentation.tex

# View the presentation
view: rust_presentation.pdf
	start rust_presentation.pdf

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Clean everything including PDF
distclean: clean
	rm -f rust_presentation.pdf

# Help
help:
	@echo "Available targets:"
	@echo "  make              - Compile the presentation"
	@echo "  make presentation - Compile the presentation"
	@echo "  make view         - Open the PDF"
	@echo "  make clean        - Remove auxiliary files"
	@echo "  make distclean    - Remove all generated files"
