#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
News Scraper - Utility Tools
Helper functions for common tasks
"""

import csv
import os
from datetime import datetime, timedelta
import subprocess
import sys

def clear_screen():
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_stats():
    """Displays news statistics"""
    filename = 'news.csv'

    if not os.path.exists(filename):
        print("✗ news.csv not found")
        return

    print("\nNEWS STATISTICS")
    print("="*50)

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            news = list(reader)

        total = len(news)
        print(f"Total articles: {total}")

        if total > 0:
            # Newest and oldest articles
            print(f"Newest: {news[0]['Date']}")
            print(f"Oldest: {news[-1]['Date']}")

            # Date-based statistics
            today = datetime.now().strftime('%Y-%m-%d')
            yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
            week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

            today_count = sum(1 for n in news if n['Date'].startswith(today))
            yesterday_count = sum(1 for n in news if n['Date'].startswith(yesterday))
            week_count = sum(1 for n in news if n['Date'] >= week_ago)

            print(f"\nFetched today:      {today_count}")
            print(f"Fetched yesterday:  {yesterday_count}")
            print(f"Last 7 days:        {week_count}")

            # Average title length
            avg_title_len = sum(len(n['Title']) for n in news) // total
            print(f"Avg title length:   {avg_title_len} characters")

    except Exception as e:
        print(f"✗ Error: {e}")

    print("="*50 + "\n")

def backup_csv():
    """Creates a backup of the CSV file"""
    filename = 'news.csv'

    if not os.path.exists(filename):
        print("✗ news.csv not found")
        return

    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f'news_backup_{timestamp}.csv'

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(content)

        size = os.path.getsize(backup_file) / 1024
        print(f"✓ Backup created: {backup_file} ({size:.1f} KB)\n")

    except Exception as e:
        print(f"✗ Backup error: {e}\n")

def clean_old_news(days=30):
    """Deletes articles older than the specified number of days"""
    filename = 'news.csv'

    if not os.path.exists(filename):
        print("✗ news.csv not found")
        return

    try:
        cutoff_date = datetime.now() - timedelta(days=days)
        cutoff_str = cutoff_date.strftime('%Y-%m-%d')

        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            news = list(reader)

        original_count = len(news)
        news = [n for n in news if n['Date'] >= cutoff_str]
        removed = original_count - len(news)

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Date', 'Title', 'Link'])
            writer.writeheader()
            writer.writerows(news)

        print(f"✓ {removed} old articles deleted (older than {days} days)")
        print(f"  Remaining: {len(news)}\n")

    except Exception as e:
        print(f"✗ Cleanup error: {e}\n")

def export_json():
    """Exports CSV data to JSON format"""
    filename = 'news.csv'

    if not os.path.exists(filename):
        print("✗ news.csv not found")
        return

    try:
        import json

        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            news = list(reader)

        json_file = f'news_{datetime.now().strftime("%Y%m%d")}.json'

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump({
                'date': datetime.now().isoformat(),
                'total': len(news),
                'articles': news
            }, f, ensure_ascii=False, indent=2)

        size = os.path.getsize(json_file) / 1024
        print(f"✓ JSON file created: {json_file} ({size:.1f} KB)\n")

    except ImportError:
        print("✗ JSON support required\n")
    except Exception as e:
        print(f"✗ Export error: {e}\n")

def search_by_date():
    """Searches for articles within a date range"""
    filename = 'news.csv'

    if not os.path.exists(filename):
        print("✗ news.csv not found")
        return

    try:
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        end_date = input("End date (YYYY-MM-DD): ").strip()

        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            news = list(reader)

        results = [n for n in news
                  if start_date <= n['Date'][:10] <= end_date]

        print(f"\nFound {len(results)} articles between {start_date} and {end_date}:\n")

        for idx, n in enumerate(results[:10], 1):
            print(f"{idx}. [{n['Date'][:10]}] {n['Title'][:60]}...")

        if len(results) > 10:
            print(f"\n... and {len(results)-10} more articles")

        print()

    except Exception as e:
        print(f"✗ Error: {e}\n")

def show_logs():
    """Displays the log file"""
    if not os.path.exists('scraper.log'):
        print("✗ scraper.log not found\n")
        return

    print("\nLAST LOG ENTRIES (last 20 lines)")
    print("="*60)

    try:
        with open('scraper.log', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines[-20:]:
            print(line.rstrip())

        print("="*60 + "\n")

    except Exception as e:
        print(f"✗ Error: {e}\n")

def run_scraper_manual():
    """Runs the scraper manually"""
    print("Running scraper...\n")

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

    except subprocess.TimeoutExpired:
        print("✗ Timeout - Operation is taking too long")
    except FileNotFoundError:
        print("✗ scraper.py not found")
    except Exception as e:
        print(f"✗ Error: {e}")

    print()

def main():
    """Main menu"""
    while True:
        clear_screen()

        print("\n" + "="*60)
        print("NEWS SCRAPER - UTILITY TOOLS")
        print("="*60)
        print("\n1. Show statistics")
        print("2. Backup CSV file")
        print("3. Clean old articles (30 days)")
        print("4. Export to JSON")
        print("5. Search by date range")
        print("6. Show log file")
        print("7. Run scraper manually")
        print("8. Exit")
        print("="*60)

        choice = input("\nEnter your choice (1-8): ").strip()
        print()

        if choice == '1':
            get_stats()
        elif choice == '2':
            backup_csv()
        elif choice == '3':
            try:
                days = int(input("Delete articles older than how many days? (default: 30): ") or "30")
                clean_old_news(days)
            except ValueError:
                print("✗ Please enter a number\n")
        elif choice == '4':
            export_json()
        elif choice == '5':
            search_by_date()
        elif choice == '6':
            show_logs()
        elif choice == '7':
            run_scraper_manual()
        elif choice == '8':
            print("Goodbye!\n")
            break
        else:
            print("✗ Invalid choice\n")

        input("Press Enter to continue...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nClosed.")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
