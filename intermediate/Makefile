.PHONY: all clean presentation book view view-book help

# Default target - compile both presentation and book
all: presentation book

# Compile the presentation
presentation: rust_intermediate.tex
	pdflatex rust_intermediate.tex
	pdflatex rust_intermediate.tex

# Compile the book
book: rust_intermediate_book.tex
	pdflatex rust_intermediate_book.tex
	pdflatex rust_intermediate_book.tex

# View the presentation
view: rust_intermediate.pdf
	start rust_intermediate.pdf

# View the book
view-book: rust_intermediate_book.pdf
	start rust_intermediate_book.pdf

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Clean everything including PDFs
distclean: clean
	rm -f rust_intermediate.pdf rust_intermediate_book.pdf

# Help
help:
	@echo "Available targets:"
	@echo "  make              - Compile both presentation and book"
	@echo "  make presentation - Compile the presentation only"
	@echo "  make book         - Compile the book only"
	@echo "  make view         - Open the presentation PDF"
	@echo "  make view-book    - Open the book PDF"
	@echo "  make clean        - Remove auxiliary files"
	@echo "  make distclean    - Remove all generated files"
