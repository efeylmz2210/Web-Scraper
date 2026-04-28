#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CONFIGURATION SETTINGS
Copy this file and use it as config.py
"""

# ========================================
# NEWS SCRAPER SETTINGS
# ========================================

# 1. NEWS SOURCE SETTINGS
# ========================================
NEWS_SOURCE = 'https://www.hurriyet.com.tr'

# Maximum number of articles to fetch
MAX_ARTICLES = 50

# Connection timeout (seconds)
TIMEOUT = 10

# User-Agent (to be recognized as a browser)
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

# 2. CSV SETTINGS
# ========================================
CSV_FILE = 'news.csv'

# Maximum number of rows in CSV file
# Older articles are automatically deleted
MAX_CSV_ROWS = 500

# CSV encoding (UTF-8 for special characters)
CSV_ENCODING = 'utf-8'

# 3. TIME SETTINGS
# ========================================
# Time to run the scraper (HH:MM format)
RUN_TIME = '09:00'

# Display log timestamps in UTC
TIMEZONE = 'Europe/Istanbul'  # UTC+3

# 4. LOG SETTINGS
# ========================================
LOG_FILE = 'scraper.log'

# Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = 'INFO'

# Maximum log file size (in MB)
MAX_LOG_SIZE = 10

# 5. SEARCH SETTINGS
# ========================================
# Maximum search results to display
MAX_SEARCH_RESULTS = 100

# Title truncation (in characters)
MAX_TITLE_LENGTH = 100

# Link truncation (in characters)
MAX_LINK_LENGTH = 100

# Case-sensitive search
SEARCH_CASE_SENSITIVE = False

# 6. BACKUP SETTINGS
# ========================================
# Enable automatic backups
AUTO_BACKUP = True

# Backup directory
BACKUP_DIR = './backups'

# Maximum number of backups (older ones are deleted)
MAX_BACKUP_COUNT = 10

# 7. DATABASE SETTINGS (Future Version)
# ========================================
# Use database (sqlite3)
USE_DATABASE = False

DATABASE_FILE = 'news.db'

# 8. ADVANCED SETTINGS
# ========================================
# Tolerate errors during scraping
TOLERATE_ERRORS = True

# Use proxy
USE_PROXY = False
PROXY_ADDRESSES = {
    'http': 'http://proxy.example.com:8080',
    'https': 'http://proxy.example.com:8080',
}

# Verify SSL certificate
SSL_VERIFY = True

# Retry count (how many times to retry on connection failure)
RETRY_COUNT = 3

# Wait time between retries (seconds)
RETRY_WAIT = 2

# 9. FILTER SETTINGS
# ========================================
# Only fetch articles from specific categories
CATEGORY_FILTERS = [
    'technology',
    'economy',
    'sports',
    'politics',
]

# Exclude articles containing these words
BLACKLIST = [
    'advertisement',
    'announcement',
    'sponsor',
]

# 10. EMAIL NOTIFICATIONS (Future Version)
# ========================================
EMAIL_NOTIFICATIONS = False
EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-password'
EMAIL_RECIPIENT = 'recipient@example.com'

# ===========================================
# EXAMPLE COMBINATIONS
# ===========================================

"""
Scenario 1: Light Usage (Daily Monitoring)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAX_ARTICLES = 30
MAX_CSV_ROWS = 300
RUN_TIME = '09:00'
AUTO_BACKUP = False

Scenario 2: Heavy Usage (Research)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAX_ARTICLES = 100
MAX_CSV_ROWS = 2000
RUN_TIME = '08:00'
AUTO_BACKUP = True
RETRY_COUNT = 5

Scenario 3: Performance-Focused
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAX_ARTICLES = 15
MAX_CSV_ROWS = 100
LOG_LEVEL = 'ERROR'
AUTO_BACKUP = False

Scenario 4: Enterprise Usage
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAX_ARTICLES = 50
MAX_CSV_ROWS = 5000
USE_DATABASE = True
EMAIL_NOTIFICATIONS = True
AUTO_BACKUP = True
"""

# ===========================================
# USAGE EXAMPLE
# ===========================================

"""
Use in scraper.py like this:

from config import MAX_ARTICLES, CSV_FILE, TIMEOUT

# In your code:
for link in article_links[:MAX_ARTICLES]:
    # ...

save_to_csv(news_data, CSV_FILE)

# or in setup_scheduler.py:
from config import RUN_TIME

# Use RUN_TIME in your scheduling logic
"""

# ===========================================
# CUSTOMIZATION EXAMPLES
# ===========================================

def get_config():
    """Returns configuration as a dictionary"""
    return {
        'source': NEWS_SOURCE,
        'max_articles': MAX_ARTICLES,
        'timeout': TIMEOUT,
        'csv_file': CSV_FILE,
        'max_csv_rows': MAX_CSV_ROWS,
        'run_time': RUN_TIME,
        'log_file': LOG_FILE,
    }

def print_config():
    """Prints all settings"""
    config = get_config()

    print("\nCURRENT SETTINGS")
    print("="*50)

    for key, value in config.items():
        print(f"  {key:<20}: {value}")

    print("="*50 + "\n")

if __name__ == '__main__':
    print_config()
