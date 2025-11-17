# Grand Rounds Scraper Maintenance Guide

## Overview

Many academic medical centers block automated scraping. This document explains how to manually update the scrapers with current data.

## Last Updated
**2025-11-16**

## Institutions Covered

### 1. **Beth Israel Deaconess Medical Center** (`scrape_bidmc.py`)
- URL: https://www.bidmc.org/medical-education/medical-education-by-department/medicine/medical-grand-rounds
- Status: Manual curation required (SSL blocking)
- Update frequency: Monthly
- Focus: Internal Medicine Grand Rounds

### 2. **Yale School of Medicine** (`scrape_yale.py`)
- URL: https://medicine.yale.edu/internal-medicine/news/events/
- Status: Manual curation
- Focus: Medical Grand Rounds, Internal Medicine

### 3. **Massachusetts General Hospital** (`scrape_mgh.py`)
- URL: https://www.massgeneral.org/medicine/education/medical-grand-rounds
- Status: Manual curation
- Focus: Medical Grand Rounds, Cancer Grand Rounds

### 4. **Harvard Medical School** (`scrape_harvard.py`)
- URLs:
  - BIDMC: https://www.bidmc.org/medical-education/medical-education-by-department/medicine/medical-grand-rounds
  - Osher Center: https://oshercenter.org/im-grand-rounds/
- Focus: Medical Education, Integrative Medicine

### 5. **Brigham and Women's Hospital** (`scrape_brigham.py`)
- URL: https://www.brighamandwomens.org/neurology/neurology-grand-rounds
- Status: Connection issues
- Focus: Neurology Grand Rounds (expand to Medicine)

### 6. **Dartmouth Hitchcock Medical Center** (`scrape_dartmouth.py`)
- URL: https://www.dartmouth-hitchcock.org/health-care-professionals/medicine-grand-rounds
- Focus: Medicine Grand Rounds

### 7. **Rhode Island Hospital / Brown University** (`scrape_brown.py`)
- URL: https://brownim.org/2/conference-retreat-overview/
- Focus: Internal Medicine, Hematology/Oncology

## How to Update Scrapers

### Step 1: Visit the Institution's Website
Navigate to their Grand Rounds page and look for upcoming events.

### Step 2: Collect Required Data
For each event, gather:
- **Title**: Specific lecture topic (e.g., "Management of Hypertension in the Elderly")
- **Speaker**: Full name and credentials
- **Date**: In YYYY-MM-DD format
- **Time**: In HH:MM format (24-hour)
- **Direct Link**: URL to the specific event announcement (if available)
- **Department**: Medicine, Internal Medicine, etc.

### Step 3: Update the Scraper File
Edit the appropriate `scrape_*.py` file and add events to the schedule list:

```python
schedule = [
    {
        "date": "2025-12-15",
        "time": "12:00",
        "title": "Novel Approaches to Heart Failure Management",
        "speaker": "John Doe, MD, PhD",
        "type": "Medical Grand Rounds",
        "event_url": "https://example.com/events/12345"  # If available
    },
    # Add more events...
]
```

### Step 4: Test the Scraper
```bash
python3 scraper/scrape_bidmc.py
```

### Step 5: Run Full Aggregation
```bash
python3 -m scraper.main
```

### Step 6: Verify Output
Check `docs/data.json` for the new events.

## Data Requirements

### Must Have:
- **Specific lecture title** (not just "Medical Grand Rounds")
- **Speaker name**
- **Date and time**
- **Institution name**
- **Department**

### Nice to Have:
- Direct link to event page
- CME information
- Event description

## Update Schedule

- **Weekly**: Check for new events at all institutions
- **Monthly**: Verify all upcoming events are still accurate
- **Quarterly**: Review and clean up past events

## Adding New Institutions

To add a new academic medical center:

1. Create `scraper/scrape_[institution].py` using `template_scraper.py`
2. Add institution details (name, state, region, URL)
3. Manually curate initial event list
4. Test the scraper
5. Update this maintenance guide

## Tracking URL Database

`scraper/scraped_urls.json` tracks which URLs have been processed to avoid duplicates.

Update format:
```json
{
  "last_updated": "2025-11-16T19:50:00Z",
  "scraped_urls": {
    "https://example.com/event/123": {
      "title": "Event Title",
      "scraped_date": "2025-11-16",
      "status": "active"
    }
  }
}
```

## Notes

- Most academic sites update their schedules monthly
- Summer months (July-August) often have fewer events
- Check for special lecture series (e.g., visiting professors, named lectureships)
- Look for Medicine/Internal Medicine departments specifically
