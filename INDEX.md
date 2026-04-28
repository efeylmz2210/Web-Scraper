# HURRIYET NEWS SCRAPER - PROJECT OVERVIEW

## Project Purpose

A Python application that automatically fetches, archives, and lets you search current news from hurriyet.com.tr.

---

## PROJECT STRUCTURE

```
├── GETTING STARTED
│   ├── QUICK_START.md         <- 5-minute quick start
│   ├── quickstart.py          <- Test tools
│   └── requirements.txt       <- Install libraries
│
├── MAIN TOOLS
│   ├── scraper.py             <- Fetch and save articles
│   ├── search.py              <- Search and list
│   ├── setup_scheduler.py     <- Set up automation
│   └── utils.py               <- Utility tools
│
├── DOCUMENTATION
│   ├── README.md              <- All features
│   ├── GUIDE.md               <- Comprehensive guide
│   ├── config_example.py      <- Settings examples
│   └── INDEX.md               <- This file
│
└── DATA
    ├── news.csv               <- Stored articles
    └── scraper.log            <- Operation logs
```

---

## GETTING STARTED

### 1. Quick Start (5 minutes)
```bash
# Read this
QUICK_START.md

# Or run this
python quickstart.py
```

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Fetch First Articles
```bash
python scraper.py
```

### 4. Search Articles
```bash
python search.py technology
```

---

## FEATURE STATUS

| Feature | Status | File |
|---------|--------|------|
| Web Scraping | ✅ | `scraper.py` |
| CSV Storage | ✅ | `scraper.py` |
| Search Engine | ✅ | `search.py` |
| Auto Scheduling | ✅ | `setup_scheduler.py` |
| Statistics | ✅ | `utils.py` |
| JSON Export | ✅ | `utils.py` |
| Interactive Menu | ✅ | `search.py`, `utils.py` |
| Logging | ✅ | `scraper.log` |

---

## KEY COMMANDS

### Fetch Articles
```bash
python scraper.py
```
**What it does:** Fetches latest articles from Hurriyet, saves to CSV

### Search Articles
```bash
python search.py technology
```
**What it does:** Finds articles containing "technology"

### Interactive Menu
```bash
python search.py
```
**What it does:** Opens interactive menu to select options

### Utility Tools
```bash
python utils.py
```
**What it does:** Statistics, backup, cleanup, etc.

### Scheduler Setup
```bash
python setup_scheduler.py
```
**What it does:** Sets up automatic daily run at 09:00

### Quick Test
```bash
python quickstart.py
```
**What it does:** Tests the entire system

---

## FILE DESCRIPTIONS

### `scraper.py`
**Purpose:** Fetches articles and saves to CSV

**Features:**
- Scrapes hurriyet.com.tr
- Automatically filters duplicates
- Stores in CSV file
- Writes errors to log file
- Timeout and retry mechanisms

**Run:**
```bash
python scraper.py
```

### `search.py`
**Purpose:** Article search and listing

**Features:**
- Keyword search
- List recent articles
- Export search results
- Interactive menu interface
- Table-formatted display

**Run:**
```bash
python search.py [keyword]
```

### `setup_scheduler.py`
**Purpose:** Set up automation with Windows Task Scheduler

**Features:**
- Set up daily schedule
- Check task status
- Remove task
- Install libraries

**Run:**
```bash
python setup_scheduler.py
```

### `utils.py`
**Purpose:** Utility tools and reporting

**Features:**
- Show statistics
- Backup CSV file
- Clean old articles
- Export to JSON
- Search by date range
- View log file

**Run:**
```bash
python utils.py
```

### `quickstart.py`
**Purpose:** System testing and guidance

**Features:**
- Check libraries
- Test scraper
- Test search feature
- Show file information

**Run:**
```bash
python quickstart.py
```

---

## DOCUMENTATION

### `QUICK_START.md`
Get started in 5 minutes. The most essential steps.

### `README.md`
All features and usage guide. Detailed explanations.

### `GUIDE.md`
Comprehensive guide. Workflows, troubleshooting, examples.

### `config_example.py`
All settings and customization options.

### `INDEX.md` (This file)
Project structure and overview.

---

## COMMON USAGE WORKFLOWS

### Scenario 1: Daily News Monitoring
```
1. Set to 09:00 with setup_scheduler.py
2. Runs automatically every day
3. Search articles with search.py
```

### Scenario 2: Topic Research
```
1. Fetch articles with scraper.py
2. Search topic-related articles with search.py
3. Export to JSON with utils.py
```

### Scenario 3: Weekly Report
```
1. View statistics with utils.py
2. Export to JSON with utils.py
3. Generate your report
```

---

## DATA STRUCTURES

### CSV Format
```csv
Date,Title,Link
2026-04-28 09:15:30,"Article Title","https://..."
```

### JSON Format (Export)
```json
{
  "date": "2026-04-28T10:30:00",
  "total": 287,
  "articles": [...]
}
```

---

## SYSTEM REQUIREMENTS

### Minimum Requirements
- **OS:** Windows 10/11 or Linux/Mac
- **Python:** 3.7+
- **RAM:** 512 MB
- **Disk:** 50 MB

### Libraries
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `tabulate` - Table formatting

---

## TROUBLESHOOTING

### Check Log File
```bash
type scraper.log
```

### View Statistics
```bash
python utils.py
# Select "1" from menu
```

### Test System
```bash
python quickstart.py
# Select "5" from menu (Test Everything)
```

---

## SECURITY

- ✅ All data stored locally
- ✅ Internet connection only used for fetching articles
- ✅ No data sent to third-party servers
- ✅ CSV contains only article metadata

---

## PERFORMANCE

**Average Performance:**
- Scraping time: 10-30 seconds
- CSV size: ~100 KB (500 articles)
- Memory usage: ~50 MB
- CPU usage: Minimal

---

## LEARNING RESOURCES

### Techniques Used in Code
1. **Web Scraping** - BeautifulSoup4
2. **HTTP Requests** - Requests
3. **File Operations** - CSV, JSON
4. **Task Scheduling** - Windows Task Scheduler
5. **CLI Interface** - Interactive menus

### Extension Ideas
- [ ] Database (SQLite) integration
- [ ] Email notifications
- [ ] REST API creation
- [ ] Web interface (Flask)
- [ ] Telegram bot
- [ ] Twitter/X scraping

---

## SUPPORT & FAQ

### Frequently Asked Questions

**Q: Can I remove automatic scheduling?**
```bash
python setup_scheduler.py
# Select "3" from menu
```

**Q: Can I open articles in Excel?**
```
Yes! Double-click news.csv
```

**Q: How many articles can it store?**
```
Default 500, changeable in scraper.py
```

**Q: Which categories does it fetch?**
```
All categories (entire Hurriyet site)
```

---

## CONCLUSION

Congratulations!

You now have a fully functional news scraper system.

**Getting Started Checklist:**
- [ ] `pip install -r requirements.txt`
- [ ] `python scraper.py` (Fetch first articles)
- [ ] `python search.py` (Search)
- [ ] `python setup_scheduler.py` (Set up automation)

Good luck!

---

**Version:** 1.0
**Last Updated:** April 28, 2026
**Python:** 3.7+
**Platform:** Windows, Linux, macOS
