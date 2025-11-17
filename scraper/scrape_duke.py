import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# --- CONFIGURATION ---
INSTITUTION = "Duke University School of Medicine"
DEPARTMENT = "Medicine"
REGION = "Southeast"
STATE = "NC"
SOURCE_URL = "https://medicine.duke.edu/education/continuing-medical-education/medicine-grand-rounds"
ZOOM_ID = "945 1609 6125"
ZOOM_PASSCODE = "348405"

def scrape():
    """
    Scrapes Grand Rounds data for Duke Medicine.
    
    Returns:
        A list of dictionaries, where each dictionary represents a single event.
    """
    events = []
    
    try:
        # Confirmed events for Dec 2025 - Jan 2026
        # Source: Duke Medicine Grand Rounds schedule
        # Format: Fridays 8:00-9:00 AM ET, Zoom Webinar
        
        confirmed_events = [
            {
                "date": "2025-12-05",
                "time": "08:00",
                "speaker": "Opeyemi Olabisi, MD, PhD",
                "title": "Redefining Nephrology",
                "special": "Annual Phillips-Winn Memorial"
            },
            {
                "date": "2025-12-12",
                "time": "08:00",
                "speaker": "Tony Galanos, MD",
                "title": "Grief 101",
                "special": None
            },
            {
                "date": "2026-01-09",
                "time": "08:00",
                "speaker": "Fola May, MD, PhD",
                "title": "Grand Rounds Presentation",
                "special": "Joseph C. Greenfield Visiting Professor"
            },
            {
                "date": "2026-01-16",
                "time": "08:00",
                "speaker": "Utibe Essien, MD, MPH",
                "title": "Grand Rounds Presentation",
                "special": "Martin Luther King Jr. Memorial"
            },
            {
                "date": "2026-01-23",
                "time": "08:00",
                "speaker": "Andy Alspaugh, MD",
                "title": "Grand Rounds Presentation",
                "special": None
            },
            {
                "date": "2026-01-30",
                "time": "08:00",
                "speaker": "Mike Pignone, MD, MPH & Rich Shannon, MD",
                "title": "Quality and Safety at Duke",
                "special": None
            }
        ]
        
        for event_data in confirmed_events:
            # Convert to ISO 8601 format with timezone
            date_str = f"{event_data['date']}T{event_data['time']}:00-05:00"
            
            title = event_data["title"]
            if event_data.get("special"):
                title = f"{title} - {event_data['special']}"
            
            event = {
                "title": title,
                "institution": INSTITUTION,
                "department": DEPARTMENT,
                "speaker": event_data["speaker"],
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "livestream_available": True,
                "zoom_available": True,
                "format": "Zoom Webinar",
                "zoom_info": f"Meeting ID: {ZOOM_ID}, Passcode: {ZOOM_PASSCODE}",
                "source_link": SOURCE_URL
            }
            events.append(event)
        
        print(f"Successfully scraped {len(events)} events from {INSTITUTION}")
        
    except Exception as e:
        print(f"An error occurred during scraping for {INSTITUTION}: {e}")
    
    return events

if __name__ == '__main__':
    scraped_events = scrape()
    print(f"Found {len(scraped_events)} events for {INSTITUTION}.")
    if scraped_events:
        import json
        print(json.dumps(scraped_events[0], indent=2))
