# Hurriyet News Scraper

A Python application that automatically fetches current news from hurriyet.com.tr, saves it to a CSV file, and provides search functionality.

## Features

✅ **Web Scraping** - Automatically fetches current news from hurriyet.com.tr
✅ **CSV Storage** - Saves articles to news.csv
✅ **Auto Scheduling** - Runs automatically every morning at 09:00
✅ **Search** - Keyword search across all articles
✅ **Interactive Interface** - Easy to use from the command line
✅ **Logging** - All operations logged to scraper.log

---

## Setup

### 1. Install Required Libraries

**Automatic installation (Recommended):**
```bash
python setup_scheduler.py
```
Select "1" from the menu to install libraries and configure scheduling at once.

**Manual installation:**
```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Fetch Articles (Scraping)

**One-time run:**
```bash
python scraper.py
```

**Output:**
```
Fetching news from hurriyet.com.tr...
45 articles found!
✓ 23 new articles saved!
```

### 2. Search Articles

**Interactive menu:**
```bash
python search.py
```

Menu:
```
==================================================
NEWS SEARCH INTERFACE
==================================================
1. Search by keyword
2. Show recent articles
3. Export search results
4. Exit
==================================================
```

**Direct keyword search from command line:**
```bash
python search.py technology
```

**Example Search Results:**
```
Found 12 results for 'technology':

╒═════╤════════════╤═════════════════════════════════╤═══════════════════════╕
│   # │ Date       │ Title                           │ Link                  │
╞═════╪════════════╪═════════════════════════════════╪═══════════════════════╡
│   1 │ 2026-04-28 │ New technology article...       │ https://hurriyet...  │
│   2 │ 2026-04-27 │ AI revolution begins...         │ https://hurriyet...  │
└─────┴────────────┴─────────────────────────────────┴───────────────────────┘
```

### 3. Automatic Scheduling (Daily at 09:00)

**Set up scheduling:**
```bash
python setup_scheduler.py
```

Menu:
```
1. Set up daily task (at 9:00 AM)
2. Check task status
3. Remove task
4. Exit
```

Select "1" to activate automatic scheduling.

**Check scheduling:**
```bash
python setup_scheduler.py
```
Select "2" to check task status.

**Remove scheduling:**
```bash
python setup_scheduler.py
```
Select "3" to remove the task from Windows Task Scheduler.

---

## File Structure

```
Python Web Scraper System/
│
├── scraper.py                 # Main web scraper
├── search.py                  # Search and listing interface
├── setup_scheduler.py         # Windows Task Scheduler setup
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── news.csv                   # Stored articles (auto-created)
└── scraper.log                # Operation log (auto-created)
```

---

## CSV File Format

`news.csv` contains the following columns:

```csv
Date,Title,Link
2026-04-28 09:15:30,"Article Title",https://www.hurriyet.com.tr/article-link
2026-04-28 09:15:22,"Another Article",https://www.hurriyet.com.tr/other-article
```

**Features:**
- Stores maximum 500 articles
- Automatically filters duplicate articles
- Newest articles appear at the top
- UTF-8 encoding supports all characters

---

## Search Features

### Keyword Search
```bash
python search.py economy
```
Finds all articles containing "economy" (case-insensitive).

### List Recent Articles
```bash
python search.py
# Select 2 from menu
```
Shows the latest 10 articles (customizable).

### Export Search Results
```bash
python search.py
# Select 3 from menu
# Enter keyword: technology
```
Saves results to `search_results.csv`.

---

## Log File

All operations are logged in `scraper.log`:

```
2026-04-28 09:15:45 - INFO - 15 new articles saved. Total: 287 articles
2026-04-28 09:16:12 - ERROR - Scraping error: Connection timeout
2026-04-28 10:30:22 - WARNING - Error processing link: NoneType
```

To view the log:
```bash
type scraper.log
```
or
```bash
Get-Content scraper.log -Tail 20  # Show last 20 lines
```

---

## Technical Details

### Scraper Libraries
- `requests` - HTTP requests
- `BeautifulSoup4` - HTML parsing
- `csv` - CSV file operations

### Features
- **User-Agent:** Mozilla/5.0 (recognized as desktop browser)
- **Timeout:** 10 seconds
- **Error Handling:** All errors logged to log file
- **Task Scheduler:** Uses Windows Task Scheduler (Windows 10/11)

---

## Troubleshooting

### 1. "news.csv not found" error
```bash
# Solution: Run the scraper first
python scraper.py
```

### 2. Scheduling not working
```bash
# Check:
python setup_scheduler.py
# Select "2" to check status
```

### 3. Cannot fetch articles (connection error)
```bash
# Check log file
type scraper.log

# Check internet connection
ping hurriyet.com.tr
```

### 4. Characters not displaying correctly
- `search.py` uses UTF-8 encoding, supported by most terminals
- If issues in PowerShell, try Command Prompt

---

## Security Notes

**Important:**
- Python must be installed on the device running this script
- Internet connection is required
- Administrator privileges may be required for Windows Task Scheduler
- Use the scraper responsibly (don't overload the server)

---

## Command Reference

| Command | Description |
|---------|-------------|
| `python scraper.py` | Fetches and saves articles to CSV |
| `python search.py` | Opens interactive search menu |
| `python search.py [keyword]` | Direct keyword search |
| `python setup_scheduler.py` | Shows scheduling options |

---

## Advanced Usage

### Changing the Schedule Time
Find and change this line in `setup_scheduler.py`:
```xml
<StartBoundary>2026-04-28T09:00:00</StartBoundary>
```
Replace `09:00` with your desired time (e.g., `14:30`).

### Search Sensitivity
In `search.py`, this line does case-insensitive search:
```python
if keyword.lower() in row['Title'].lower():
```
For exact matching, change to:
```python
if keyword.lower() == row['Title'].lower():
```

---

## Version
- **Version:** 1.0
- **Date:** April 28, 2026
- **Python:** 3.7+

---

## Tips

1. **Quick search:** `python search.py politics | findstr "minister"`
2. **Open CSV in Excel:** Right-click `news.csv` -> Open with Excel
3. **Delete old articles:** Delete `news.csv`, the scraper will create a new one automatically
4. **Log check:** If scheduling issues occur, check `scraper.log`

---

Happy researching!
