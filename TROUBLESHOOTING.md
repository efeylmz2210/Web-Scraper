# HURRIYET SCRAPING ISSUES & SOLUTIONS

## Problem

Connection errors may occur when scraping the Hurriyet.com.tr homepage. Possible causes:

1. **Dynamic Content** - Articles loaded via JavaScript
2. **Bot Protection** - Hurriyet has anti-bot systems
3. **Rate Limiting** - Too many requests get blocked
4. **Missing Headers** - Not being recognized as a browser

---

## SOLUTION 1: Improved Headers (Simple Fix)

### Change Made

Headers were improved in `scraper.py`:

**Before:**
```python
headers = {
    'User-Agent': 'Mozilla/5.0 ...'
}
```

**After (More Realistic):**
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'text/html,application/xhtml+xml,...',
    'Accept-Language': 'tr-TR,tr;q=0.9,...',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.google.com/',
    # ... and more
}
```

### To use:
```bash
python scraper.py
```

---

## SOLUTION 2: RSS Feed (Recommended - 100% Works)

### What is RSS?

RSS = Really Simple Syndication

- **Advantage**: No site blocking, fast, reliable
- **How**: Hurriyet provides all articles via RSS feed
- **Categories**: Homepage, News, Politics, Economy, Sports, Technology, Lifestyle

### To use:

**Step 1: Install RSS scraper library**
```bash
pip install feedparser
```

**Step 2: Run RSS Scraper**
```bash
python scraper_rss.py
```

**Expected Output:**
```
============================================================
HURRIYET RSS FEED SCRAPER
============================================================

Fetching news from Hurriyet RSS feeds...

  Fetching Homepage... ✓ 20 articles
  Fetching News... ✓ 20 articles
  Fetching Politics... ✓ 20 articles
  Fetching Economy... ✓ 20 articles
  Fetching Sports... ✓ 20 articles
  Fetching Technology... ✓ 20 articles
  Fetching Lifestyle... ✓ 20 articles

Total 140 articles found
✓ 140 new articles saved!
✓ Total articles: 140
```

---

## SOLUTION 3: Try Both (Hybrid)

### To use:
```bash
python run_scraper.py
```

**Selection Menu:**
```
1. HTML Scraper (site HTML)
2. RSS Feed Scraper (RSS feed) <- RECOMMENDED
3. Try Both (HTML -> RSS fallback)
4. Exit
```

---

## Comparison Table

| Feature | HTML Scraper | RSS Scraper | Hybrid |
|---------|-------------|------------|--------|
| Block-resistant | ✗ | ✅ | ✅ |
| Finds all articles | ✅ | ✓ (by category) | ✅ |
| Categories | ✗ | ✅ | ✅ |
| Speed | Slow | Very Fast | Fast |
| Reliability | Low | High | High |
| Simplicity | Easy | Easy | Easy |

---

## Quick Start

### Best Option: RSS Scraper

```bash
# 1. Install library
pip install feedparser

# 2. Run RSS Scraper
python scraper_rss.py

# 3. Search articles
python search.py technology
```

### Alternative: Hybrid Mode

```bash
# 1. Run run_scraper.py
python run_scraper.py

# 2. Select "2" (RSS) or "3" (Hybrid)
# 3. Articles are fetched automatically
```

---

## RSS Feed URLs

Hurriyet provides RSS feeds for all these categories:

```
https://www.hurriyet.com.tr/rss/anasayfa          (Homepage)
https://www.hurriyet.com.tr/rss/gundem            (News)
https://www.hurriyet.com.tr/rss/politika          (Politics)
https://www.hurriyet.com.tr/rss/ekonomi           (Economy)
https://www.hurriyet.com.tr/rss/spor              (Sports)
https://www.hurriyet.com.tr/rss/teknoloji         (Technology)
https://www.hurriyet.com.tr/rss/yasam             (Lifestyle)
```

You can open any of them in your browser to verify.

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'feedparser'"

**Solution:**
```bash
pip install feedparser
```

### Problem: 0 articles from RSS Scraper

**Solution:**
```bash
# Check RSS feeds
# Test by opening in your browser:
https://www.hurriyet.com.tr/rss/anasayfa
```

### Problem: HTML Scraper fails but RSS works

**Explanation:** Normal! RSS is much more reliable. Keep using RSS:
```bash
python scraper_rss.py
```

---

## Files

| File | Description |
|------|-------------|
| `scraper.py` | Original HTML scraper (with improved headers) |
| `scraper_rss.py` | ✅ RSS Feed scraper (recommended) |
| `run_scraper.py` | Launcher for selecting scraper type |
| `search.py` | Article search (compatible with both scrapers) |
| `requirements.txt` | Updated: feedparser added |

---

## Recommendations

✅ **Best:** Use RSS Scraper
```bash
python scraper_rss.py
```

✅ **For Testing:** Hybrid Mode
```bash
python run_scraper.py
# Select "3" (Try Both)
```

✅ **For Automation:** Set up RSS scraper in setup_scheduler.py

---

## FAQ

**Q: Why no articles found in RSS?**
**A:** RSS doesn't fetch articles outside its categories. Try HTML scraper.

**Q: Does HTML scraper ever work?**
**A:** It works occasionally but RSS is much more reliable.

**Q: Which should I use?**
**A:** **RSS Scraper** (scraper_rss.py) - most reliable and fastest.

**Q: Can I run both at the same time?**
**A:** Yes, but unnecessary. RSS is sufficient.

---

## Next Steps

1. **Install libraries:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test RSS Scraper:**
   ```bash
   python scraper_rss.py
   ```

3. **Search articles:**
   ```bash
   python search.py technology
   ```

4. **Set up automation:**
   ```bash
   python setup_scheduler.py
   ```

---

**Good luck!**
