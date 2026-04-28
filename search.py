import csv
import os
from datetime import datetime
from tabulate import tabulate

def search_news(keyword):
    """Searches for news articles in the CSV file"""
    filename = 'news.csv'

    if not os.path.exists(filename):
        print("✗ 'news.csv' not found. Please run the scraper first.")
        return

    results = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Search in title (case-insensitive)
                if keyword.lower() in row['Title'].lower():
                    results.append(row)

    except Exception as e:
        print(f"✗ Search error: {e}")
        return

    if results:
        print(f"\nFound {len(results)} results for '{keyword}':\n")

        # Format table
        table_data = []
        for idx, result in enumerate(results, 1):
            table_data.append([
                idx,
                result['Date'][:10],
                result['Title'][:60] + '...' if len(result['Title']) > 60 else result['Title'],
                result['Link'][:50] + '...' if len(result['Link']) > 50 else result['Link']
            ])

        print(tabulate(
            table_data,
            headers=['#', 'Date', 'Title', 'Link'],
            tablefmt='grid',
            maxcolwidths=[3, 12, 60, 50]
        ))

        # Show detailed results
        print("\n" + "="*80)
        for idx, result in enumerate(results[:5], 1):  # Show first 5
            print(f"\n{idx}. Title: {result['Title']}")
            print(f"   Date:  {result['Date']}")
            print(f"   Link:  {result['Link']}")
    else:
        print(f"\n✗ No results found for '{keyword}'.")

    print(f"\nTotal articles: {len(list(open(filename, 'r', encoding='utf-8')))}")

def list_recent_news(limit=10):
    """Lists the most recent news articles"""
    filename = 'news.csv'

    if not os.path.exists(filename):
        print("✗ 'news.csv' not found.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            news = list(reader)[:limit]

        if news:
            print(f"\nLatest {len(news)} articles:\n")

            table_data = []
            for idx, item in enumerate(news, 1):
                table_data.append([
                    idx,
                    item['Date'][:10],
                    item['Title'][:60] + '...' if len(item['Title']) > 60 else item['Title'],
                ])

            print(tabulate(
                table_data,
                headers=['#', 'Date', 'Title'],
                tablefmt='grid'
            ))

            print("\nDetails:")
            for idx, item in enumerate(news[:3], 1):
                print(f"\n{idx}. {item['Title']}")
                print(f"   Link: {item['Link']}")
        else:
            print("✗ No articles found.")

    except Exception as e:
        print(f"✗ Error: {e}")

def export_search_results(keyword, output_file='search_results.csv'):
    """Exports search results to a new CSV file"""
    filename = 'news.csv'

    if not os.path.exists(filename):
        print("✗ 'news.csv' not found.")
        return

    results = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if keyword.lower() in row['Title'].lower():
                    results.append(row)

        if results:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['Date', 'Title', 'Link'])
                writer.writeheader()
                writer.writerows(results)

            print(f"✓ {len(results)} results saved to '{output_file}'.")
        else:
            print(f"✗ No results found for '{keyword}'.")

    except Exception as e:
        print(f"✗ Export error: {e}")

def interactive_menu():
    """Interactive menu"""
    while True:
        print("\n" + "="*50)
        print("NEWS SEARCH INTERFACE")
        print("="*50)
        print("1. Search by keyword")
        print("2. Show recent articles")
        print("3. Export search results")
        print("4. Exit")
        print("="*50)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            keyword = input("Enter keyword: ").strip()
            if keyword:
                search_news(keyword)
            else:
                print("✗ Keyword cannot be empty.")

        elif choice == '2':
            try:
                limit = int(input("How many articles to show? (default: 10): ").strip() or "10")
                list_recent_news(limit)
            except ValueError:
                print("✗ Please enter a number.")

        elif choice == '3':
            keyword = input("Enter keyword: ").strip()
            if keyword:
                export_search_results(keyword)
            else:
                print("✗ Keyword cannot be empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("✗ Invalid choice.")

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        # Command-line usage
        keyword = ' '.join(sys.argv[1:])
        search_news(keyword)
    else:
        # Interactive menu
        interactive_menu()
