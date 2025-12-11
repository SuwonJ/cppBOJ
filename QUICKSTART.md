# Quick Start Guide - README Automation

## Adding a New Problem Solution

When you add a new problem solution to the `code/` folder, follow these steps to update README.md:

### Method 1: Automatic (Recommended)
```bash
# 1. Add your solution file
# Example: code/2750.cpp

# 2. Run the automation script
python3 update_readme.py

# 3. Commit and push
git add README.md code/2750.cpp
git commit -m "Add problem 2750 solution"
git push
```

### Method 2: GitHub Actions (Fully Automated)
Simply push your new `.cpp` file to the `main` branch:
```bash
git add code/2750.cpp
git commit -m "Add problem 2750 solution"
git push origin main
```

The GitHub Actions workflow will automatically update README.md for you!

### Method 3: Manual (No dependencies)
```bash
# 1. Edit update_readme_simple.py and add the problem title:
# PROBLEM_TITLES = {
#     2750: "수 정렬하기",
#     ...
# }

# 2. Run the script
python3 update_readme_simple.py

# 3. Commit and push
git add README.md code/2750.cpp update_readme_simple.py
git commit -m "Add problem 2750 solution"
git push
```

## Testing the Scripts

To test without modifying README.md, you can run:
```bash
# See what would be generated without writing to file
python3 update_readme.py --help  # Shows usage
python3 update_readme_simple.py  # Check the warning messages
```

## Troubleshooting

**Script not found?**
Make sure you're in the repository root directory:
```bash
cd /path/to/cppBOJ
```

**Import error for requests?**
Install the required library:
```bash
pip install requests
```

**GitHub Actions not running?**
- Make sure the workflow file exists in `.github/workflows/update-readme.yml`
- Check that you're pushing to the `main` branch
- Verify that Actions are enabled in your repository settings

For more details, see `AUTOMATION.md`.
