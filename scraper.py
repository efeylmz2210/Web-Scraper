import requests
from bs4 import BeautifulSoup
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

def scrape_hurriyet():
    """Fetches current news from hurriyet.com.tr"""
    try:
        url = 'https://www.hurriyet.com.tr'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'tr-TR,tr;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://www.google.com/'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        news_data = []

        # Search for article links (main news sections)
        article_links = soup.find_all('a', {'data-testid': 'internal-link'})

        if not article_links:
            # Alternative selector
            article_links = soup.find_all('a', class_='link')

        if not article_links:
            # Another alternative
            articles = soup.find_all('article')
            article_links = []
            for article in articles:
                link = article.find('a')
                if link:
                    article_links.append(link)

        # Set to track unique articles
        seen_links = set()

        for link in article_links[:50]:  # Get first 50 articles
            try:
                title = link.get_text(strip=True)
                href = link.get('href', '')

                if title and href and href not in seen_links:
                    # Convert to full URL
                    if href.startswith('/'):
                        full_url = 'https://www.hurriyet.com.tr' + href
                    elif href.startswith('http'):
                        full_url = href
                    else:
                        continue

                    seen_links.add(href)
                    news_data.append({
                        'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'Title': title,
                        'Link': full_url
                    })
            except Exception as e:
                logging.warning(f"Error processing link: {e}")
                continue

        return news_data

    except requests.RequestException as e:
        logging.error(f"Scraping error: {e}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
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
                existing_data = list(reader)

        # Merge new and existing data (prevent duplicates)
        existing_links = {item['Link'] for item in existing_data}
        new_data = [item for item in news_data if item['Link'] not in existing_links]
        all_data = new_data + existing_data

        # Keep maximum 500 articles
        all_data = all_data[:500]

        # Write to CSV
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['Date', 'Title', 'Link']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)

        logging.info(f"{len(new_data)} new articles saved. Total: {len(all_data)} articles")
        print(f"✓ {len(new_data)} new articles saved!")
        return True

    except Exception as e:
        logging.error(f"CSV save error: {e}")
        print(f"✗ CSV save error: {e}")
        return False

def main():
    """Main function"""
    print("Fetching news from hurriyet.com.tr...")
    news_data = scrape_hurriyet()

    if news_data:
        print(f"{len(news_data)} articles found!")
        save_to_csv(news_data)
    else:
        print("✗ No articles found or connection error")
        logging.warning("No articles found")

if __name__ == '__main__':
    main()
