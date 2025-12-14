#!/usr/bin/env python3
"""
Script to make Rust notebooks runnable in Google Colab by:
1. Adding Rust installation cell at the beginning
2. Converting Rust code examples to executable bash cells
"""

import json
import os
import glob

SETUP_CELL = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "%%bash\n",
        "# Install Rust in Colab (run this cell first!)\n",
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y\n",
        "source $HOME/.cargo/env\n",
        "rustc --version"
    ]
}

def create_rust_code_cell(rust_code, cell_number):
    """Create a bash cell that compiles and runs Rust code"""
    # Clean up the rust code
    code_lines = rust_code if isinstance(rust_code, list) else rust_code.split('\n')
    rust_code_str = '\\n'.join(code_lines)

    bash_code = f"""%%bash
source $HOME/.cargo/env
cat > example_{cell_number}.rs << 'RUSTCODE'
{rust_code_str}
RUSTCODE
rustc example_{cell_number}.rs 2>&1 && ./example_{cell_number} 2>&1 || echo "Compilation failed"
"""

    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": bash_code.split('\n')
    }

def has_setup_cell(cells):
    """Check if notebook already has setup cell"""
    if not cells:
        return False
    first_code_cell = next((c for c in cells if c.get('cell_type') == 'code'), None)
    if not first_code_cell:
        return False
    source = first_code_cell.get('source', [])
    source_str = ''.join(source) if isinstance(source, list) else source
    return 'Install Rust in Colab' in source_str

def process_notebook(filepath):
    """Process a single notebook file"""
    print(f"Processing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    cells = nb.get('cells', [])

    # Skip if already has setup
    if has_setup_cell(cells):
        print(f"  [OK] Already has setup cell, skipping")
        return

    # Add note to first markdown cell if it exists
    if cells and cells[0].get('cell_type') == 'markdown':
        source = cells[0].get('source', [])
        if isinstance(source, list):
            # Add note after title
            if len(source) > 0:
                source.insert(1, "\\n")
                source.insert(2, "**Note:** This notebook will install Rust in your Colab environment. Run the setup cell first!\\n")
        cells[0]['source'] = source

    # Insert setup cell after first markdown cell
    insert_pos = 1 if cells and cells[0].get('cell_type') == 'markdown' else 0
    cells.insert(insert_pos, SETUP_CELL)

    # Update cells
    nb['cells'] = cells

    # Ensure proper metadata
    nb['metadata'] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.7.12"
        }
    }

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

    print(f"  [OK] Updated successfully")

def main():
    """Main function"""
    # Get all chapter notebooks
    notebooks = sorted(glob.glob('chapter_*.ipynb'))

    print(f"Found {len(notebooks)} notebooks to process\\n")

    for nb_path in notebooks:
        try:
            process_notebook(nb_path)
        except Exception as e:
            print(f"  [ERROR] Error: {e}")

    print(f"\\n[DONE] Processed {len(notebooks)} notebooks")

if __name__ == '__main__':
    main()
