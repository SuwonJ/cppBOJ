# README Automation Scripts

This directory contains scripts to automatically update README.md with links to all your problem solutions.

## Available Scripts

### 1. `update_readme.py` (Recommended)
Automatically fetches problem titles from acmicpc.net.

**Requirements:**
- Python 3.6+
- `requests` library: `pip install requests`

**Usage:**
```bash
python3 update_readme.py
```

**Pros:**
- Automatically fetches problem titles from acmicpc.net
- No need to manually maintain a list of problem titles

**Cons:**
- Requires internet connection
- Requires the `requests` library

### 2. `update_readme_simple.py` (No dependencies)
Uses a manually maintained dictionary of problem titles.

**Requirements:**
- Python 3.6+ (no external libraries needed)

**Usage:**
```bash
python3 update_readme_simple.py
```

**Configuration:**
Edit the `PROBLEM_TITLES` dictionary in the script to add new problem titles:
```python
PROBLEM_TITLES = {
    10845: "큐",
    1929: "소수 구하기",
    1978: "소수 찾기",
    # Add more here...
}
```

**Pros:**
- No external dependencies
- No internet connection required
- Fast execution

**Cons:**
- Need to manually add problem titles for each new problem

## How It Works

Both scripts:
1. Scan the `code/` folder for all `.cpp` files with numeric names (e.g., `1012.cpp`)
2. Extract problem numbers from filenames
3. Generate README.md with:
   - Links to problems on acmicpc.net
   - Links to source code in your GitHub repository
4. Sort problems by problem number

## Workflow

### When adding a new problem:

1. Add your solution file to the `code/` folder (e.g., `code/2750.cpp`)
2. Run the automation script:
   ```bash
   python3 update_readme.py
   ```
   or
   ```bash
   python3 update_readme_simple.py
   ```
3. Commit and push:
   ```bash
   git add README.md
   git commit -m "Update README with problem 2750"
   git push
   ```

### Using GitHub Actions (Optional)

You can automate this further with GitHub Actions. Create `.github/workflows/update-readme.yml`:

```yaml
name: Update README

on:
  push:
    paths:
      - 'code/*.cpp'

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      
      - name: Install dependencies
        run: pip install requests
      
      - name: Update README
        run: python3 update_readme.py
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add README.md
          git diff --quiet && git diff --staged --quiet || git commit -m "Auto-update README.md"
          git push
```

This will automatically update README.md whenever you add a new `.cpp` file to the `code/` folder!

## Customization

Both scripts can be customized by editing these variables:
- `repo_owner`: Your GitHub username (default: 'SuwonJ')
- `repo_name`: Your repository name (default: 'cppBOJ')
- `branch`: Your default branch (default: 'main')

Find these in the `generate_readme_content()` function.
