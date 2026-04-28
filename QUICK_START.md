#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
QUICK START (5 Minutes)

Follow this guide to get the system running in 5 minutes!
"""

print("""
╔════════════════════════════════════════════════════════════════╗
║                    QUICK START GUIDE                           ║
║                                                                ║
║           Set Up Hurriyet News Scraper in 5 Minutes           ║
╚════════════════════════════════════════════════════════════════╝

STEP 1: INSTALL LIBRARIES (1 minute)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run this command in your terminal:

    pip install -r requirements.txt

Expected output:
    Successfully installed requests beautifulsoup4 tabulate


STEP 2: FETCH YOUR FIRST ARTICLES (2 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run this command in your terminal:

    python scraper.py

Expected output:
    Fetching news from hurriyet.com.tr...
    42 articles found!
    ✓ 42 new articles saved!

This command:
   - Fetches the latest 50 articles from hurriyet.com.tr
   - Saves them to "news.csv"
   - On subsequent runs, only adds new articles


STEP 3: SEARCH ARTICLES (1 minute)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Example 1 - Technology articles:

    python search.py technology

Expected output:
    Found 7 results for 'technology':

    ╒═╤═══════════╤══════════════════════════╤═════════════╕
    │#│ Date      │ Title                    │ Link        │
    ╞═╪═══════════╪══════════════════════════╪═════════════╡
    │1│ 2026-04-28│ New technology article...│ https://... │
    └─┴───────────┴──────────────────────────┴─────────────┘


Example 2 - Show recent articles:

    python search.py

Select "2" from the menu to view the last 10 articles.


STEP 4: SET UP AUTOMATIC SCHEDULING (1 minute) [OPTIONAL]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

To run automatically every morning at 09:00:

    python setup_scheduler.py

Select "1" from the menu to complete setup.

After this:
   - Windows will automatically run the scraper every day at 09:00
   - You don't need to do anything
   - Articles are automatically added to news.csv


═══════════════════════════════════════════════════════════════════

DONE!

The system is now running. Here's what you can do:

1.  Search articles:
    python search.py [keyword]

2.  Run scraper manually:
    python scraper.py

3.  View articles:
    python search.py
    Select from menu

4.  View statistics:
    python utils.py
    Select "1" from menu

5.  Export data:
    python utils.py
    Select "4" -> Export to JSON


IMPORTANT FILES

  news.csv      <- All articles are stored here
  scraper.log   <- Errors and info logged here
  README.md     <- Detailed documentation


QUICK QUESTIONS

Q: How do I open the CSV file?
A: Double-click news.csv to open in Excel

Q: Can I change the schedule time?
A: Yes! Change the time in setup_scheduler.py

Q: How many articles does it store?
A: Up to 500 (newest ones are kept)

Q: What if I encounter a problem?
A: Check the scraper.log file


RECOMMENDED USAGE

Daily Monitoring:
  1. First day: python scraper.py (collect articles)
  2. setup_scheduler.py (set to 09:00)
  3. Search articles: python search.py [topic]

Weekly Summary:
  1. python utils.py (view statistics)
  2. python utils.py (export to JSON)
  3. Generate your report


NEXT STEPS

For more information see:
  - README.md         -> All features
  - GUIDE.md          -> Comprehensive guide
  - config_example.py -> Advanced settings


Happy Scraping!

═══════════════════════════════════════════════════════════════════
""")

if __name__ == '__main__':
    input("\nPress Enter to continue...")
