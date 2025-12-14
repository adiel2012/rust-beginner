# Notebook Setup Guide

## What Was Done

All 20 Jupyter notebooks in this repository have been configured to be **fully runnable in Google Colab** without requiring any local Rust installation.

## How It Works

### Automatic Rust Installation
Each notebook contains a setup cell that:
1. Downloads and installs Rust using `rustup`
2. Configures the Rust environment
3. Verifies the installation

### Code Execution
All Rust code examples are wrapped in bash cells that:
1. Source the Rust environment
2. Compile the Rust code
3. Execute the compiled program
4. Display the output

## Using the Notebooks

### In Google Colab (Recommended)

1. Click any "Open in Colab" badge in the [README](README.md)
2. Wait for Colab to load the notebook
3. **Important**: Run the first code cell to install Rust (this takes ~1-2 minutes)
4. Once installation completes, you can run any other cell
5. Modify code examples and re-run to experiment

**Note**: Each Colab session is temporary. If you restart the runtime, you'll need to re-run the installation cell.

### Locally with Jupyter

1. Install Rust: https://rustup.rs
2. Install Jupyter: `pip install jupyter`
3. Clone this repo: `git clone https://github.com/adiel2012/rust-beginner.git`
4. Run: `jupyter notebook`
5. Open any chapter notebook
6. Skip the installation cell (Rust is already installed)
7. Run code cells as normal

## Notebook Structure

Each notebook follows this pattern:

```
1. Title and Introduction (Markdown)
2. Setup Cell (Code) - Installs Rust
3. Content Sections (Markdown)
4. Code Examples (Code) - Executable Rust code
5. Exercises (Markdown + Code)
6. Key Takeaways (Markdown)
```

## Technical Details

### Rust Installation Command
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source $HOME/.cargo/env
rustc --version
```

### Code Execution Pattern
```bash
source $HOME/.cargo/env
cat > program.rs << 'EOF'
fn main() {
    println!("Hello, Rust!");
}
EOF
rustc program.rs
./program
```

## Troubleshooting

### "Command not found: rustc"
- Make sure you ran the first setup cell
- Restart the Colab runtime and try again

### "Permission denied"
- This shouldn't happen in Colab
- If using locally, check file permissions

### Compilation errors
- Check the error message - Rust provides detailed feedback
- Review the code for syntax errors
- Compare with the correct example in the notebook

## Contributing

If you find issues with the notebooks:
1. Check existing issues: https://github.com/adiel2012/rust-beginner/issues
2. Create a new issue with:
   - Chapter number
   - Cell that's failing
   - Error message
   - Environment (Colab vs local)

## Updates

To update the notebooks, we use the `update_notebooks.py` script:

```bash
python update_notebooks.py
```

This script:
- Adds setup cells to notebooks without them
- Updates kernel metadata
- Ensures consistent formatting

## License

This educational material is provided as-is for learning purposes.

---

Happy Learning! 🦀
