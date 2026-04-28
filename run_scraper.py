#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SCRAPER LAUNCHER - Choose Scraper Type
You can use either scraper:
1. HTML Scraper (scraper.py) - Parses site HTML directly
2. RSS Feed Scraper (scraper_rss.py) - Reads from RSS feed
"""

import subprocess
import sys
import os

def print_menu():
    """Prints the menu"""
    print("\n" + "="*60)
    print("HURRIYET NEWS SCRAPER - SELECT TYPE")
    print("="*60)
    print("\n1. HTML Scraper (scraper.py)")
    print("   ✓ Works directly from site HTML")
    print("   ✓ Can find all articles")
    print("   ✗ Sensitive to site blocking")
    print("   ✗ May fail if page is inaccessible\n")

    print("2. RSS Feed Scraper (scraper_rss.py) [RECOMMENDED]")
    print("   ✓ Reads safely from RSS feed")
    print("   ✓ Unaffected by site blocking")
    print("   ✓ Fetches articles by category")
    print("   ✓ Faster and more reliable")
    print("   ✗ Only fetches articles within RSS categories\n")

    print("3. Try Both (HTML -> RSS fallback)")
    print("   ✓ Falls back to RSS if HTML fails\n")

    print("4. Exit")
    print("="*60)

def run_scraper(scraper_type):
    """Runs the selected scraper"""
    try:
        if scraper_type == 1:
            print("\nRunning HTML Scraper...\n")
            subprocess.run([sys.executable, 'scraper.py'], check=True)

        elif scraper_type == 2:
            print("\nRunning RSS Feed Scraper...\n")
            subprocess.run([sys.executable, 'scraper_rss.py'], check=True)

        elif scraper_type == 3:
            print("\nTrying HTML Scraper...\n")
            result = subprocess.run(
                [sys.executable, 'scraper.py'],
                capture_output=True,
                text=True
            )

            if result.returncode == 0 and os.path.exists('news.csv') and os.path.getsize('news.csv') > 100:
                print(result.stdout)
                print("✓ HTML Scraper succeeded!")
            else:
                print("HTML Scraper failed, switching to RSS Scraper...\n")
                subprocess.run([sys.executable, 'scraper_rss.py'], check=True)

    except subprocess.CalledProcessError as e:
        print(f"✗ Scraper error: {e}")
    except FileNotFoundError as e:
        print(f"✗ File not found: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    """Main menu"""
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            run_scraper(1)
        elif choice == '2':
            run_scraper(2)
        elif choice == '3':
            run_scraper(3)
        elif choice == '4':
            print("\nGoodbye!\n")
            break
        else:
            print("\n✗ Invalid choice. Please enter a number between 1-4.\n")

        input("\nPress Enter to continue...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nClosed.")
    except Exception as e:
        print(f"\n✗ Error: {e}")
