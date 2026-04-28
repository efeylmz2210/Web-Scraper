# HURRIYET NEWS SCRAPER - COMPREHENSIVE GUIDE

## Overview

This project is a fully-featured Python application that automatically fetches, archives, and lets you search news from hurriyet.com.tr.

### Components

```
┌─────────────────────────────────────────────┐
│         scraper.py                          │
│    (Article Fetching & CSV Storage)         │
├─────────────────────────────────────────────┤
│         search.py                           │
│    (Search & Listing Interface)             │
├─────────────────────────────────────────────┤
│      setup_scheduler.py                     │
│  (Windows Task Scheduler Automation)        │
├─────────────────────────────────────────────┤
│         utils.py                            │
│     (Utility Tools & Reports)               │
├─────────────────────────────────────────────┤
│      quickstart.py                          │
│  (Quick Start & Test Tools)                 │
└─────────────────────────────────────────────┘
```

---

## STEP-BY-STEP GETTING STARTED

### Step 1: Installation (2 minutes)

**Option A: Automatic Installation (Recommended)**
```bash
python quickstart.py
```
Select "5" from the menu to test everything.

**Option B: Manual Installation**
```bash
pip install -r requirements.txt
```

---

### Step 2: Fetch First Articles

```bash
python scraper.py
```

**Expected output:**
```
Fetching news from hurriyet.com.tr...
42 articles found!
✓ 42 new articles saved!
```

---

### Step 3: Search Articles

```bash
python search.py technology
```

Or Interactive Menu:
```bash
python search.py
```

---

### Step 4: Automatic Scheduling (Optional)

```bash
python setup_scheduler.py
```

Select "1" from the menu to set up daily automatic run at 09:00.

---

## USAGE EXAMPLES

### Scenario 1: Daily News Report

**Articles are automatically fetched at 9 AM**
```
2026-04-28 09:00 -> scraper.py runs
2026-04-28 09:00 -> 23 new articles found
2026-04-28 09:00 -> news.csv updated
```

### Scenario 2: Finding Articles on a Specific Topic

**Search for technology articles:**
```bash
python search.py artificial intelligence
```

**Search for economy articles:**
```bash
python search.py bank inflation
```

**Search for politics articles:**
```bash
python search.py election parliament
```

### Scenario 3: Creating a Weekly Report

```bash
python utils.py
# Select "1" to view statistics
# Select "4" to export to JSON
```

---

## COMMAND REFERENCE

### Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `python scraper.py` | Fetch and save articles | `python scraper.py` |
| `python search.py [keyword]` | Search articles | `python search.py sports` |
| `python search.py` | Open search menu | `python search.py` |

### Utility Commands

| Command | Description |
|---------|-------------|
| `python quickstart.py` | Quick start guide |
| `python setup_scheduler.py` | Set up scheduling |
| `python utils.py` | Utility tools |

---

## SEARCH EXAMPLES

### Simple Search

```bash
python search.py economy
# Finds all articles containing "economy"
```

Output:
```
Found 5 results for 'economy':

╒═════╤═══════════╤══════════════════════════════════╤═══════════════════╕
│   # │ Date      │ Title                            │ Link              │
╞═════╪═══════════╪══════════════════════════════════╪═══════════════════╡
│   1 │ 2026-04-28│ New economic policy...           │ https://hurriyet..│
│   2 │ 2026-04-27│ Central bank announcement        │ https://hurriyet..│
└─────┴───────────┴──────────────────────────────────┴───────────────────┘
```

### Multi-Word Search

```bash
python search.py "artificial intelligence"
# Searches for the phrase "artificial intelligence"
```

---

## DATA STRUCTURES

### CSV Format

```csv
Date,Title,Link
2026-04-28 09:15:30,"Technology article",https://www.hurriyet.com.tr/...
2026-04-28 09:14:22,"Politics article",https://www.hurriyet.com.tr/...
```

### JSON Format (Export)

```json
{
  "date": "2026-04-28T10:30:00.123456",
  "total": 287,
  "articles": [
    {
      "Date": "2026-04-28 09:15:30",
      "Title": "Technology article",
      "Link": "https://www.hurriyet.com.tr/..."
    }
  ]
}
```

---

## ADVANCED SETTINGS

### Changing the Schedule Time

**Goal:** Run every day at 14:30

1. Open `setup_scheduler.py`
2. Find this line:
   ```xml
   <StartBoundary>2026-04-28T09:00:00</StartBoundary>
   ```
3. Change it to:
   ```xml
   <StartBoundary>2026-04-28T14:30:00</StartBoundary>
   ```
4. Re-register the schedule:
   ```bash
   python setup_scheduler.py
   # Select "1" to update
   ```

### Increasing Article Count

In **scraper.py**:
```python
for link in article_links[:50]:  # Get 50 articles
```
Change it (e.g., 100 articles):
```python
for link in article_links[:100]:  # Get 100 articles
```

### Changing Storage Limit

In **scraper.py**:
```python
all_data = all_data[:500]  # Maximum 500 articles
```
Change it (e.g., 1000 articles):
```python
all_data = all_data[:1000]  # Maximum 1000 articles
```

---

## EXAMPLE WORKFLOWS

### Workflow 1: Daily News Monitoring

```
Monday    09:00 -> Scraper runs (42 articles)
Tuesday   09:00 -> Scraper runs (38 articles) - Total: 80
Wednesday 09:00 -> Scraper runs (41 articles) - Total: 121
...
Sunday    14:00 -> Search weekly summary with search.py
Sunday    15:00 -> Export to JSON
```

### Workflow 2: Research Project

```
Day 1:  python scraper.py  (Collect initial data)
Day 2:  python search.py "research topic"
Day 3:  python utils.py (view statistics)
Day 4:  python utils.py (export to JSON)
```

### Workflow 3: Crisis Monitoring

```
Setup   -> setup_scheduler.py (every 2 hours between 9:00 - 17:00)
Monitor -> search.py "crisis-related keywords"
Report  -> utils.py (statistics and reporting)
```

---

## TROUBLESHOOTING

### Problem 1: Cannot fetch articles

```bash
# Solution steps:
1. Check internet connection
   ping hurriyet.com.tr

2. Check log file
   type scraper.log

3. Check firewall settings

4. Disable VPN/Proxy if using one
```

### Problem 2: Scheduling issue

```bash
# Steps:
1. Check task status
   python setup_scheduler.py
   (Select "2" from menu)

2. Check log file
   python utils.py
   (Select "6" from menu)

3. Reset scheduling
   python setup_scheduler.py
   (Select "3" to remove)
   python setup_scheduler.py
   (Select "1" to re-register)
```

### Problem 3: Special characters not displaying

```bash
# Solution:
Use Command Prompt instead of PowerShell
python search.py
```

### Problem 4: Performance slowdown

```bash
# Solution:
1. Clean old articles
   python utils.py
   (Select "3" from menu)

2. Reduce storage limit
   Lower the all_data[:500] value in scraper.py
```

---

## FREQUENTLY ASKED QUESTIONS

### Q: How often should I fetch articles?

**Answer:** Depending on your needs:
- Daily: `09:00`
- Every 6 hours: `09:00`, `15:00`, `21:00`
- Hourly: Use the `schedule` library

### Q: Maximum articles that can be stored?

**Answer:** Default 500, changeable in `scraper.py`.

### Q: How large does the CSV file get?

**Answer:** Average article is ~200-300 bytes:
- 500 articles ≈ 100 KB
- 5000 articles ≈ 1 MB

### Q: Can I completely remove scheduling?

**Answer:** Yes!
```bash
python setup_scheduler.py
# Select "3" from menu
```

### Q: Can I add my own news source?

**Answer:** Yes! In `scraper.py`:
```python
# Add new source
news_data.extend(scrape_other_source())
```

---

## SECURITY NOTES

**Important:**

1. **Server Load:**
   - Recommend running 2-3 times per day
   - Avoid excessive requests

2. **Data Privacy:**
   - CSV contains publicly available article data
   - Review content before sharing

3. **API Permissions:**
   - Read Hurriyet's Terms of Service
   - Request permission before large-scale scraping

4. **System Performance:**
   - No need to run as administrator
   - Take regular backups

---

## SUPPORT & BUG REPORTING

If you have issues:

1. **Check log file:**
   ```bash
   type scraper.log
   ```

2. **View statistics:**
   ```bash
   python utils.py
   ```

3. **Test entire system:**
   ```bash
   python quickstart.py
   ```

---

## LEARNING RESOURCES

Libraries used in the code:

- **requests** - HTTP requests
- **BeautifulSoup4** - HTML parsing
- **csv** - CSV file operations
- **tabulate** - Table formatting

More info: https://docs.python-requests.org

---

## NOTES

- All files use UTF-8 encoding
- Special characters are fully supported
- Tested on Windows 10/11 and Python 3.7+
- Settings are applied immediately (no restart needed)

---

## CONCLUSION

You now have a fully functional news scraper system!

**Next steps:**
1. ✅ `pip install -r requirements.txt`
2. ✅ `python scraper.py`
3. ✅ `python search.py`
4. ✅ `python setup_scheduler.py`

Good luck!
