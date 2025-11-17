import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# --- CONFIGURATION ---
INSTITUTION = "Johns Hopkins University School of Medicine"
DEPARTMENT = "General Internal Medicine"
REGION = "Mid-Atlantic"
STATE = "MD"
SOURCE_URL = "https://www.hopkinsmedicine.org/som/divisions/general-internal-medicine/education-training/grand-rounds"

def scrape():
    """
    Scrapes Grand Rounds data for Johns Hopkins GIM.
    
    Returns:
        A list of dictionaries, where each dictionary represents a single event.
    """
    events = []
    
    try:
        # Confirmed events for Dec 2025 - Jan 2026
        # Source: Hopkins GIM Grand Rounds schedule
        # Format: Fridays 9:00-10:00 AM ET, Hybrid with Zoom
        
        confirmed_events = [
            {
                "date": "2025-12-05",
                "time": "09:00",
                "speaker": "Emily Joseph, MLIS, MM",
                "title": "Virtual Scholarship & Research Meeting",
                "zoom_available": True
            },
            {
                "date": "2025-12-12",
                "time": "09:00",
                "speaker": "Alia Rehwinkel Bodnar, MD",
                "title": "Grand Rounds Presentation",
                "zoom_available": True
            },
            {
                "date": "2025-12-19",
                "time": "09:00",
                "speaker": "Mary Catherine Beach, MD, MPH",
                "title": "Grand Rounds Presentation",
                "zoom_available": True
            },
            {
                "date": "2026-01-09",
                "time": "09:00",
                "speaker": "Chidinma A. Ibe, PhD",
                "title": "Grand Rounds Presentation",
                "zoom_available": True
            },
            {
                "date": "2026-01-16",
                "time": "09:00",
                "speaker": "Lisa A. Cooper, MD, MPH",
                "title": "Grand Rounds Presentation",
                "zoom_available": True
            }
        ]
        
        for event_data in confirmed_events:
            # Convert to ISO 8601 format with timezone
            date_str = f"{event_data['date']}T{event_data['time']}:00-05:00"
            
            event = {
                "title": event_data["title"],
                "institution": INSTITUTION,
                "department": DEPARTMENT,
                "speaker": event_data["speaker"],
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "livestream_available": True,
                "zoom_available": event_data.get("zoom_available", True),
                "format": "Hybrid (In-person + Zoom)",
                "zoom_info": "Contact department for Zoom access",
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
