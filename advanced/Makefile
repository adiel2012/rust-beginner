.PHONY: all clean presentation book view view-book help

# Default target - compile both presentation and book
all: presentation book

# Compile the presentation
presentation: rust_advanced.tex
	pdflatex rust_advanced.tex
	pdflatex rust_advanced.tex

# Compile the book
book: rust_advanced_book.tex
	pdflatex rust_advanced_book.tex
	pdflatex rust_advanced_book.tex

# View the presentation
view: rust_advanced.pdf
	start rust_advanced.pdf

# View the book
view-book: rust_advanced_book.pdf
	start rust_advanced_book.pdf

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Clean everything including PDFs
distclean: clean
	rm -f rust_advanced.pdf rust_advanced_book.pdf

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
