#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
News Scraper - Quick Start Guide
Run this script to test all features
"""

import subprocess
import sys
import os
from pathlib import Path

def print_banner():
    """Prints the startup banner"""
    print("\n" + "="*70)
    print("HURRIYET NEWS SCRAPER - QUICK START GUIDE")
    print("="*70 + "\n")

def check_requirements():
    """Checks required libraries"""
    print("Checking required libraries...\n")

    required = ['requests', 'beautifulsoup4', 'tabulate']
    missing = []

    for package in required:
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} - MISSING")
            missing.append(package)

    if missing:
        print(f"\nMissing libraries found!")
        print("Install them with:")
        print(f"  pip install {' '.join(missing)}\n")
        return False

    print("\n✓ All required libraries are installed!\n")
    return True

def test_scraper():
    """Tests the scraper"""
    print("="*70)
    print("1. TEST SCRAPER")
    print("="*70)
    print("\nFetching news from hurriyet.com.tr...")
    print("(This may take 10-30 seconds)\n")

    try:
        result = subprocess.run(
            [sys.executable, 'scraper.py'],
            capture_output=True,
            text=True,
            timeout=60
        )

        print(result.stdout)
        if result.stderr:
            print("Warnings:", result.stderr)

        # Check news.csv file
        if os.path.exists('news.csv'):
            with open('news.csv', 'r', encoding='utf-8') as f:
                lines = f.readlines()
            print(f"✓ CSV file contains {len(lines)-1} articles\n")
            return True
        else:
            print("✗ CSV file could not be created\n")
            return False

    except subprocess.TimeoutExpired:
        print("✗ Timeout - Connection is taking too long\n")
        return False
    except Exception as e:
        print(f"✗ Error: {e}\n")
        return False

def test_search():
    """Tests the search feature"""
    print("="*70)
    print("2. TEST SEARCH FEATURE")
    print("="*70)

    if not os.path.exists('news.csv'):
        print("\n✗ news.csv not found")
        print("Please run the scraper first!\n")
        return False

    print("\nShowing recent articles...\n")

    try:
        result = subprocess.run(
            [sys.executable, 'search.py'],
            input="2\n10\n4\n",  # Select 2, show 10 articles, then exit
            capture_output=True,
            text=True,
            timeout=10
        )

        print(result.stdout)

        # Run example search
        print("\n" + "-"*70)
        print("Example search: searching for 'technology'...\n")

        result = subprocess.run(
            [sys.executable, 'search.py', 'technology'],
            capture_output=True,
            text=True,
            timeout=10
        )

        print(result.stdout)
        print()
        return True

    except Exception as e:
        print(f"✗ Error: {e}\n")
        return False

def setup_scheduler_demo():
    """Shows scheduler setup instructions"""
    print("="*70)
    print("3. SET UP AUTOMATIC SCHEDULING")
    print("="*70)
    print("\nWill run automatically every day at 09:00\n")

    print("To activate scheduling:")
    print("  python setup_scheduler.py")
    print("\nSelect '1' from the menu to complete setup\n")

    print("To check scheduling status:")
    print("  python setup_scheduler.py")
    print("Select '2' from the menu to check status\n")

def show_file_info():
    """Shows information about created files"""
    print("="*70)
    print("4. PROJECT FILES")
    print("="*70 + "\n")

    files = {
        'scraper.py': 'Main web scraper (fetches articles)',
        'search.py': 'Search and listing interface',
        'setup_scheduler.py': 'Windows Task Scheduler setup',
        'news.csv': 'Stores fetched articles',
        'scraper.log': 'Log of all operations'
    }

    for filename, description in files.items():
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            size_str = f"{size/1024:.1f} KB" if size > 1024 else f"{size} B"
            print(f"✓ {filename:<25} ({size_str:<10}) - {description}")
        else:
            print(f"○ {filename:<25} (Not yet created) - {description}")

    print()

def main():
    """Main menu"""
    print_banner()

    if not check_requirements():
        print("Please install missing libraries and try again.\n")
        return

    while True:
        print("="*70)
        print("QUICK START")
        print("="*70)
        print("1. Test scraper (fetch articles)")
        print("2. Test search feature")
        print("3. Set up automatic scheduling")
        print("4. Show file information")
        print("5. Test Everything")
        print("6. Exit")
        print("="*70)

        choice = input("Enter your choice (1-6): ").strip()
        print()

        if choice == '1':
            test_scraper()
            input("Press Enter to continue...")

        elif choice == '2':
            test_search()
            input("Press Enter to continue...")

        elif choice == '3':
            setup_scheduler_demo()
            input("Press Enter to continue...")

        elif choice == '4':
            show_file_info()
            input("Press Enter to continue...")

        elif choice == '5':
            scraper_ok = test_scraper()
            if scraper_ok:
                test_search()
            setup_scheduler_demo()
            show_file_info()
            input("Press Enter to continue...")

        elif choice == '6':
            print("Goodbye!\n")
            break

        else:
            print("✗ Invalid choice. Please enter a number between 1-6.\n")
            input("Press Enter to continue...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nClosed.")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
