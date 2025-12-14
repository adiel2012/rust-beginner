# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Rust learning repository containing 20 educational Jupyter notebooks (chapters 1-20) that teach Rust programming from beginner to intermediate level. The notebooks are designed to run in Google Colab without requiring local Rust installation.

**Note**: The actual notebook files (`chapter_*.ipynb`) have been deleted from the working tree. They exist in git history and are referenced in the README with Colab badges, but are not currently present in the filesystem.

## Repository Structure

- **Jupyter Notebooks**: `chapter_01_*.ipynb` through `chapter_20_*.ipynb` - Interactive learning materials (currently deleted from working tree)
- **Presentation** (`beginner/` folder):
  - `rust_presentation.tex` - LaTeX Beamer presentation covering all topics
  - `Makefile` - Build automation for the presentation
  - `PRESENTATION.md` - Guide for compiling and using the LaTeX presentation
- **Python Utility**: `update_notebooks.py` - Script to add/update Rust setup cells in notebooks
- **Documentation**:
  - `README.md` - Main guide with chapter overview and Colab links
  - `SETUP.md` - Technical details about notebook configuration

## Common Commands

### Notebook Management
```bash
# Update all notebooks to add Rust setup cells
python update_notebooks.py
```

### Presentation (LaTeX)
All presentation files are in the `beginner/` subfolder:
```bash
# Navigate to presentation folder
cd beginner

# Compile the presentation (runs pdflatex twice for TOC)
make
# or
make presentation

# Open the generated PDF
make view

# Clean auxiliary LaTeX files (.aux, .log, .nav, etc.)
make clean

# Remove all generated files including PDF
make distclean
```

### Git Operations
The repository has 20 deleted notebook files in the index. Typical workflow would involve:
```bash
# Check status of deleted notebooks
git status

# Restore notebooks if needed
git restore chapter_*.ipynb
```

## Architecture Notes

### Notebook Design Pattern
Each notebook follows this structure:
1. **Setup Cell** (Code): Installs Rust via rustup in Colab environment
   - Downloads Rust using `curl | sh`
   - Sources `$HOME/.cargo/env`
   - Verifies installation with `rustc --version`

2. **Content Cells** (Markdown): Educational content explaining concepts

3. **Code Examples** (Code): Bash cells that:
   - Source the Rust environment
   - Write Rust code to a `.rs` file using heredoc
   - Compile with `rustc`
   - Execute the compiled binary

### update_notebooks.py Functionality
The Python script automates notebook configuration:
- Detects notebooks without setup cells
- Inserts Rust installation cell after the first markdown cell
- Adds a note to the first markdown cell about running setup first
- Ensures proper kernel metadata (Python 3)
- Preserves existing content while adding necessary infrastructure

### LaTeX Presentation
- Uses Beamer document class with Madrid theme
- Includes custom Rust syntax highlighting via listings package
- Covers all 20 chapters in a condensed presentation format
- Requires two pdflatex passes for proper table of contents

## Content Organization

The learning material is divided into 6 parts:
1. **Getting Started** (Chapters 1-2): Introduction, basic syntax
2. **Core Concepts** (Chapters 3-5): Ownership, borrowing, structs, enums
3. **Building Programs** (Chapters 6-8): Collections, error handling, generics, traits
4. **Advanced Topics** (Chapters 9-12): Lifetimes, testing, cargo, smart pointers
5. **Concurrency and Beyond** (Chapters 13-16): Concurrency, OOP, patterns, async
6. **Real-World Rust** (Chapters 17-20): CLI apps, web dev, unsafe, next steps

## Important Context

- **Execution Environment**: Notebooks are designed for Google Colab (cloud-based), not local Jupyter
- **No Local Rust Required**: Setup cells handle Rust installation automatically in Colab
- **Temporary Sessions**: Colab sessions are ephemeral; Rust must be reinstalled each session
- **GitHub Integration**: README contains Colab badges that link directly to GitHub-hosted notebooks

## File Patterns to Note

- All chapter notebooks follow naming: `chapter_NN_topic_name.ipynb`
- Presentation files in `beginner/`:
  - LaTeX source: `rust_presentation.tex`
  - LaTeX auxiliary files: `rust_presentation.{aux,log,nav,out,snm,toc,vrb}`
  - Generated PDF: `rust_presentation.pdf`
- Rust examples in notebooks: `example_N.rs` (temporary files created during execution)
