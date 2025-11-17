# How to Add Events Manually

Since most academic medical centers block automated scraping, here's how to manually add upcoming grand rounds:

## Step 1: Find Events

Visit these URLs and look for upcoming grand rounds:

### Yale
- https://medicine.yale.edu/internal-medicine/genmed/education/medspirel/calendar/
- https://medicine.yale.edu/event/medical-grand-rounds-1-383/

### MGH  
- https://www.massgeneral.org/cancer-center/clinician-resources/grand-rounds
- https://lms.mghcme.org/PsychGrandRounds2025

### Dartmouth
- https://video.dartmouth-hitchcock.org/category/Grand+Rounds/69017661
- https://dh.cloud-cme.com/default.aspx?P=6&EID=150850

### Brigham
- https://www.bumc.bu.edu/gim/calendar/

### Brown
- https://brownim.org/2/conference-retreat-overview/

## Step 2: Add to manual_events.json

Edit `/scraper/manual_events.json` and add each event:

```json
{
  "title": "Exact lecture title",
  "speaker": "Speaker Name, MD",
  "date_time": "2025-12-01T12:00:00-05:00",
  "institution": "Institution Name",
  "department": "Medicine",
  "state": "MA",
  "region": "New England",
  "cme_available": true,
  "source_link": "https://...",
  "cme_link": "https://..."
}
```

## Step 3: Regenerate Data

```bash
python3 -m scraper.main
```

The site will automatically update with new events!

## Date Format

Use ISO 8601 format: `YYYY-MM-DDTHH:MM:SS-05:00`

Examples:
- December 15, 2025 at 12:00 PM EST: `2025-12-15T12:00:00-05:00`
- January 10, 2026 at 8:00 AM EST: `2026-01-10T08:00:00-05:00`

## Quick Add Script

Or run this to add an event quickly:

```bash
python3 << 'EOF'
import json

event = {
    "title": "YOUR_TITLE_HERE",
    "speaker": "SPEAKER_NAME",  
    "date_time": "2025-12-15T12:00:00-05:00",
    "institution": "INSTITUTION",
    "department": "Medicine",
    "state": "MA",
    "region": "New England",
    "cme_available": True,
    "source_link": "URL",
    "cme_link": "URL"
}

with open('scraper/manual_events.json', 'r+') as f:
    data = json.load(f)
    data['events'].append(event)
    f.seek(0)
    json.dump(data, f, indent=2)
    
print("✓ Event added!")
EOF

python3 -m scraper.main
```
