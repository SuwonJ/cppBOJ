#!/usr/bin/env python3
"""
Simple script to automatically update README.md with links to all problem solutions.

This script scans the 'code' folder for .cpp files and updates README.md
with links to each problem on acmicpc.net and the corresponding source code.

Note: You need to manually add problem titles to the PROBLEM_TITLES dictionary below.

Usage:
    python3 update_readme_simple.py
"""

import os
import re
from pathlib import Path


# Manually add problem titles here
# Format: problem_number: "title"
PROBLEM_TITLES = {
    10845: "큐",
    1929: "소수 구하기",
    1978: "소수 찾기",
    1158: "요세푸스 문제",
    1966: "프린터 큐",
    11724: "연결 요소의 개수",
    1012: "유기농 배추",
    4963: "섬의 개수",
    # Add more problem titles here as you add new problems
}


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
    Note: The '##' line is kept for compatibility with the existing README format.
    """
    lines = [
        "# [NOJ.AM](https://noj.am)",
        "***",
        "##"
    ]
    
    for problem_num, filename in cpp_files:
        problem_number = str(problem_num)
        
        # Get the problem title from the dictionary
        title = PROBLEM_TITLES.get(problem_num, f"Problem {problem_number}")
        
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
    
    # Check for problems without titles
    missing_titles = [num for num, _ in cpp_files if num not in PROBLEM_TITLES]
    if missing_titles:
        print(f"\nWarning: The following problems don't have titles in PROBLEM_TITLES:")
        print(f"  {missing_titles}")
        print(f"  They will be labeled as 'Problem X' in the README.")
        print(f"  Add them to PROBLEM_TITLES in update_readme_simple.py for proper titles.\n")
    
    # Generate README content
    print("Generating README content...")
    readme_content = generate_readme_content(cpp_files)
    
    # Write to README.md
    print(f"Writing to {readme_path}...")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"\n✓ README.md updated successfully with {len(cpp_files)} problems!")
    return 0


if __name__ == '__main__':
    exit(main())
