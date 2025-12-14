# Rust Learning Presentation

A comprehensive LaTeX Beamer presentation covering Rust programming from beginner to intermediate level.

## Contents

The presentation covers all major topics from the Rust learning notebooks:

### Part 1: Getting Started
- What is Rust?
- Why Learn Rust?
- Hello, World!
- Installation Guide

### Part 2: Basic Syntax and Concepts
- Variables and Mutability
- Data Types (Scalar and Compound)
- Functions
- Control Flow (if/else, loops)

### Part 3: Core Concepts - Ownership
- Ownership Rules
- Move Semantics
- Clone and Copy
- The Stack and Heap

### Part 4: References and Borrowing
- References
- Borrowing Rules
- Mutable References
- Slices

### Part 5: Structs and Enums
- Defining Structs
- Methods and Associated Functions
- Enums and Pattern Matching
- Option and Result Types

### Part 6: Collections
- Vectors
- Hash Maps
- String Manipulation

### Part 7: Error Handling
- Result Type
- The ? Operator
- Custom Error Types

### Part 8: Generics and Traits
- Generic Functions
- Trait Definitions
- Trait Bounds

### Part 9: Fearless Concurrency
- Threads
- Message Passing with Channels
- Shared State with Mutex and Arc

### Part 10: Summary and Next Steps
- What We've Learned
- Resources
- Community

## Compiling the Presentation

### Prerequisites

You need a LaTeX distribution installed:

**Windows:**
- MiKTeX: https://miktex.org/download
- TeX Live: https://www.tug.org/texlive/

**macOS:**
```bash
brew install --cask mactex
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# Fedora
sudo dnf install texlive-scheme-full
```

### Compilation

#### Using Make (Recommended)

```bash
# Compile the presentation
make

# Or explicitly
make presentation

# View the PDF
make view

# Clean auxiliary files
make clean

# Remove everything including PDF
make distclean
```

#### Manual Compilation

```bash
# Run twice for proper table of contents
pdflatex rust_presentation.tex
pdflatex rust_presentation.tex
```

### Output

The compilation will generate `rust_presentation.pdf` - a professional Beamer presentation ready for teaching or learning.

## Features

- **Professional Theme**: Madrid theme with clean layout
- **Syntax Highlighting**: Custom Rust syntax highlighting
- **Code Examples**: All major concepts include runnable code
- **Progressive Structure**: From basics to advanced topics
- **Visual Appeal**: Clean formatting with blocks and alerts

## Customization

### Changing Theme

Edit line 2 in `rust_presentation.tex`:

```latex
\usetheme{Madrid}  % Change to: Berkeley, Berlin, Copenhagen, etc.
```

### Changing Colors

Edit line 3 in `rust_presentation.tex`:

```latex
\usecolortheme{default}  % Change to: crane, beaver, dolphin, etc.
```

### Font Size

For code listings, edit the lstset configuration:

```latex
basicstyle=\ttfamily\small,  % Change to: \tiny, \footnotesize, \normalsize
```

## Using the Presentation

### For Teaching

1. **Classroom Setting**: Full presentation flow (60-90 minutes)
2. **Workshop**: Focus on specific sections as modules
3. **Online Course**: One section per video/lesson

### For Learning

1. **Self-Study**: Work through slides at your own pace
2. **Review**: Quick reference for concepts
3. **Practice**: Type and run the code examples

### Presentation Tips

- **Take Your Time**: Don't rush through ownership and borrowing
- **Live Coding**: Demonstrate examples in real-time when possible
- **Q&A**: Pause for questions after each major section
- **Exercises**: Have students complete exercises between sections

## File Structure

```
.
├── rust_presentation.tex    # Main presentation file
├── Makefile                  # Build automation
├── PRESENTATION.md          # This file
└── rust_presentation.pdf    # Generated output (after compilation)
```

## Troubleshooting

### "pdflatex: command not found"

Install a LaTeX distribution (see Prerequisites above).

### Missing packages

If you get package errors, install them:

```bash
# MiKTeX (Windows)
# Will prompt automatically to install missing packages

# TeX Live (Linux/Mac)
tlmgr install <package-name>
```

### Compilation errors

1. Check for syntax errors in the .tex file
2. Ensure all required packages are installed
3. Try cleaning and recompiling:
   ```bash
   make distclean
   make
   ```

## License

Educational material provided for learning purposes.

## Contributing

To improve the presentation:

1. Edit `rust_presentation.tex`
2. Compile and test
3. Submit changes via GitHub

## GitHub Repository

https://github.com/adiel2012/rust-beginner

---

**Happy Teaching/Learning! 🦀**
