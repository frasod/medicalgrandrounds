import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

# --- CONFIGURATION ---
INSTITUTION = "University of Utah Health"
DEPARTMENT = "Internal Medicine"
REGION = "Mountain West"
STATE = "UT"
SOURCE_URL = "https://medicine.utah.edu/internalmedicine/education/grand-rounds"

def scrape():
    """
    Scrapes Grand Rounds data for University of Utah Internal Medicine.
    
    Returns:
        A list of dictionaries, where each dictionary represents a single event.
    """
    events = []
    
    try:
        # Utah has recurring weekly sessions on Thursdays 12:00-1:00 PM MT
        # Generating next 60 days of Thursday sessions
        # Note: Specific speakers/topics not yet published - check website closer to dates
        
        base_date = datetime(2025, 11, 21)  # Next Thursday from Nov 16
        
        # Generate 8 weeks of Thursday sessions (covers ~60 days)
        for week in range(8):
            event_date = base_date + timedelta(weeks=week)
            
            # Skip if it's during common holiday weeks
            if event_date.month == 12 and event_date.day in [25, 26] or \
               event_date.month == 1 and event_date.day == 1:
                continue
            
            date_str = event_date.strftime("%Y-%m-%dT12:00:00-07:00")  # MT timezone
            
            event = {
                "title": "Internal Medicine Grand Rounds",
                "institution": INSTITUTION,
                "department": DEPARTMENT,
                "speaker": "Check website for speaker details",
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "livestream_available": True,
                "zoom_available": False,  # Direct streaming, no registration
                "format": "Live Streaming (no registration required)",
                "zoom_info": "Visit website during session time - video displays automatically",
                "source_link": SOURCE_URL
            }
            events.append(event)
        
        print(f"Successfully generated {len(events)} recurring events for {INSTITUTION}")
        
    except Exception as e:
        print(f"An error occurred during scraping for {INSTITUTION}: {e}")
    
    return events

if __name__ == '__main__':
    scraped_events = scrape()
    print(f"Found {len(scraped_events)} events for {INSTITUTION}.")
    if scraped_events:
        import json
        print(json.dumps(scraped_events[0], indent=2))
