#!/usr/bin/env python3
"""
Script to automatically update README.md with links to all problem solutions.

This script scans the 'code' folder for .cpp files and updates README.md
with links to each problem on acmicpc.net and the corresponding source code.

Usage:
    python3 update_readme.py
"""

import os
import re
import requests
from pathlib import Path


def get_problem_title(problem_number):
    """
    Fetch the problem title from acmicpc.net.
    Returns the title if found, otherwise returns a placeholder.
    """
    try:
        url = f"https://www.acmicpc.net/problem/{problem_number}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            # Extract title from the HTML page
            title_match = re.search(r'<title>(\d+)번: (.+?)</title>', response.text)
            if title_match:
                return title_match.group(2).strip()
    except Exception as e:
        print(f"Warning: Could not fetch title for problem {problem_number}: {e}")
    
    return f"Problem {problem_number}"


def get_cpp_files(code_dir):
    """
    Get all .cpp files from the code directory.
    Returns a list of tuples (problem_number, filename) sorted by problem number.
    """
    cpp_files = []
    
    for filename in os.listdir(code_dir):
        if filename.endswith('.cpp'):
            # Extract problem number from filename
            match = re.match(r'^(\d+)\.cpp$', filename)
            if match:
                problem_number = match.group(1)
                cpp_files.append((int(problem_number), filename))
    
    # Sort by problem number
    cpp_files.sort(key=lambda x: x[0])
    
    return cpp_files


def generate_readme_content(cpp_files, repo_owner='SuwonJ', repo_name='cppBOJ', branch='main'):
    """
    Generate the content for README.md based on the cpp files found.
    """
    lines = [
        "# [NOJ.AM](https://noj.am)",
        "***",
        "##"
    ]
    
    for problem_num, filename in cpp_files:
        problem_number = str(problem_num)
        
        # Fetch the problem title
        print(f"Fetching title for problem {problem_number}...")
        title = get_problem_title(problem_number)
        
        # Generate the markdown links
        problem_link = f"https://www.acmicpc.net/problem/{problem_number}"
        source_link = f"https://github.com/{repo_owner}/{repo_name}/blob/{branch}/code/{filename}"
        
        lines.append(f">[{problem_number}:{title}]({problem_link})")
        lines.append(f">[[소스]]({source_link})")
        lines.append("")
    
    return "\n".join(lines) + "\n"


def main():
    """Main function to update README.md"""
    # Get the script directory
    script_dir = Path(__file__).parent.absolute()
    code_dir = script_dir / 'code'
    readme_path = script_dir / 'README.md'
    
    if not code_dir.exists():
        print(f"Error: Code directory not found at {code_dir}")
        return 1
    
    # Get all cpp files
    print(f"Scanning {code_dir} for .cpp files...")
    cpp_files = get_cpp_files(code_dir)
    print(f"Found {len(cpp_files)} problem files")
    
    if not cpp_files:
        print("No .cpp files found in code directory")
        return 1
    
    # Generate README content
    print("\nGenerating README content...")
    readme_content = generate_readme_content(cpp_files)
    
    # Write to README.md
    print(f"\nWriting to {readme_path}...")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"\n✓ README.md updated successfully with {len(cpp_files)} problems!")
    return 0


if __name__ == '__main__':
    exit(main())
