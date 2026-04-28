import feedparser
import csv
from datetime import datetime
import os
import logging

# Logging setup
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def scrape_hurriyet_rss():
    """Fetches news from Hurriyet RSS feeds"""
    try:
        # Hurriyet RSS feed URLs
        rss_urls = {
            'Homepage': 'https://www.hurriyet.com.tr/rss/anasayfa',
            'News': 'https://www.hurriyet.com.tr/rss/gundem',
            'Politics': 'https://www.hurriyet.com.tr/rss/politika',
            'Economy': 'https://www.hurriyet.com.tr/rss/ekonomi',
            'Sports': 'https://www.hurriyet.com.tr/rss/spor',
            'Technology': 'https://www.hurriyet.com.tr/rss/teknoloji',
            'Lifestyle': 'https://www.hurriyet.com.tr/rss/yasam',
        }

        news_data = []
        seen_links = set()

        print("Fetching news from Hurriyet RSS feeds...\n")

        for category, rss_url in rss_urls.items():
            try:
                logging.info(f"Fetching {category} from {rss_url}")
                print(f"  Fetching {category}...", end=" ")

                feed = feedparser.parse(rss_url)

                if feed.bozo:
                    logging.warning(f"RSS parse error ({category}): {feed.bozo_exception}")

                entries_count = 0

                for entry in feed.entries[:20]:  # Max 20 articles per category
                    try:
                        title = entry.get('title', '')
                        link = entry.get('link', '')
                        published = entry.get('published', datetime.now().isoformat())

                        # Parse and format the date
                        try:
                            from email.utils import parsedate_to_datetime
                            pub_date = parsedate_to_datetime(published)
                            date_str = pub_date.strftime('%Y-%m-%d %H:%M:%S')
                        except:
                            date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        if title and link and link not in seen_links:
                            seen_links.add(link)
                            news_data.append({
                                'Date': date_str,
                                'Category': category,
                                'Title': title,
                                'Link': link
                            })
                            entries_count += 1

                    except Exception as e:
                        logging.warning(f"RSS entry processing error: {e}")
                        continue

                print(f"✓ {entries_count} articles")

            except Exception as e:
                logging.error(f"RSS error ({category}): {e}")
                print(f"✗ Error")
                continue

        return news_data

    except Exception as e:
        logging.error(f"RSS scraping general error: {e}")
        print(f"✗ General error: {e}")
        return []

def save_to_csv(news_data):
    """Saves news articles to CSV file"""
    try:
        filename = 'news.csv'

        # Read existing data if file exists
        existing_data = []
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                if reader.fieldnames:
                    existing_data = list(reader)

        # Merge new and existing data (prevent duplicates)
        existing_links = {item.get('Link', '') for item in existing_data}
        new_data = [item for item in news_data if item['Link'] not in existing_links]
        all_data = new_data + existing_data

        # Keep maximum 500 articles
        all_data = all_data[:500]

        # Write to CSV
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['Date', 'Category', 'Title', 'Link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)

        logging.info(f"{len(new_data)} new articles saved. Total: {len(all_data)} articles")
        print(f"\n✓ {len(new_data)} new articles saved!")
        print(f"✓ Total articles: {len(all_data)}")
        return True

    except Exception as e:
        logging.error(f"CSV save error: {e}")
        print(f"✗ CSV save error: {e}")
        return False

def main():
    """Main function"""
    try:
        import feedparser
    except ImportError:
        print("✗ feedparser library is required!")
        print("Install with: pip install feedparser")
        logging.error("feedparser library not installed")
        return

    print("="*60)
    print("HURRIYET RSS FEED SCRAPER")
    print("="*60 + "\n")

    news_data = scrape_hurriyet_rss()

    if news_data:
        print(f"\nTotal {len(news_data)} articles found")
        save_to_csv(news_data)
    else:
        print("\n✗ No articles found")
        logging.warning("No articles found")

    print("\n" + "="*60)

if __name__ == '__main__':
    main()
