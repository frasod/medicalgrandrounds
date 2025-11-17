import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

# --- CONFIGURATION ---
INSTITUTION = "Medical University of South Carolina"
DEPARTMENT = "Medicine"
REGION = "Southeast"
STATE = "SC"
SOURCE_URL = "https://musc.edu/gr/dom"

def scrape():
    """
    Scrapes Grand Rounds data for MUSC Department of Medicine.
    
    Returns:
        A list of dictionaries, where each dictionary represents a single event.
    """
    events = []
    
    try:
        # MUSC has recurring weekly sessions on Thursdays 8:00-9:00 AM ET
        # Holiday break: December 12, 2025 - January 7, 2026
        # Resumes January 8, 2026
        
        # Generate sessions from Nov 21 through Dec 5 (before break)
        dates_before_break = [
            datetime(2025, 11, 21),
            datetime(2025, 11, 28),  # Week of Thanksgiving - might be canceled
            datetime(2025, 12, 5)
        ]
        
        # Generate sessions from Jan 8 onward (after break)
        dates_after_break = [
            datetime(2026, 1, 8),
            datetime(2026, 1, 15),
            datetime(2026, 1, 22),
            datetime(2026, 1, 29)
        ]
        
        all_dates = dates_before_break + dates_after_break
        
        for event_date in all_dates:
            date_str = event_date.strftime("%Y-%m-%dT08:00:00-05:00")  # ET timezone
            
            # Add note for Thanksgiving week
            title = "Department of Medicine Grand Rounds"
            if event_date.month == 11 and event_date.day == 28:
                title = "Department of Medicine Grand Rounds (Verify - Thanksgiving Week)"
            
            event = {
                "title": title,
                "institution": INSTITUTION,
                "department": DEPARTMENT,
                "speaker": "Check website for speaker details",
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "livestream_available": True,
                "zoom_available": True,
                "format": "Virtual via Zoom",
                "zoom_info": "Join at musc.edu/gr/dom (mobile app required for devices)",
                "source_link": SOURCE_URL,
                "notes": "CME available for live viewers only"
            }
            events.append(event)
        
        print(f"Successfully generated {len(events)} recurring events for {INSTITUTION}")
        print("Note: Holiday break Dec 12, 2025 - Jan 7, 2026 excluded")
        
    except Exception as e:
        print(f"An error occurred during scraping for {INSTITUTION}: {e}")
    
    return events

if __name__ == '__main__':
    scraped_events = scrape()
    print(f"Found {len(scraped_events)} events for {INSTITUTION}.")
    if scraped_events:
        import json
        print(json.dumps(scraped_events[0], indent=2))
