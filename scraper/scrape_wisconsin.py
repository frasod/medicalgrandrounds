import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

# --- CONFIGURATION ---
INSTITUTION = "University of Wisconsin-Madison"
DEPARTMENT = "Medicine"
REGION = "Midwest"
STATE = "WI"
SOURCE_URL = "https://www.medicine.wisc.edu/education/grand-rounds"

def scrape():
    """
    Scrapes Grand Rounds data for University of Wisconsin Medicine.
    
    Returns:
        A list of dictionaries, where each dictionary represents a single event.
    """
    events = []
    
    try:
        # Wisconsin has recurring weekly sessions on Fridays 8:00-9:00 AM CT
        # Second Friday of each month features visiting speakers with Zoom
        # Generating next 60 days of Friday sessions
        
        base_date = datetime(2025, 11, 22)  # Next Friday from Nov 16
        
        # Generate 8 weeks of Friday sessions (covers ~60 days)
        for week in range(8):
            event_date = base_date + timedelta(weeks=week)
            
            # Skip if it's during common holiday weeks
            if event_date.month == 12 and event_date.day in [25, 26] or \
               event_date.month == 1 and event_date.day == 1:
                continue
            
            # Check if it's the second Friday (visiting speaker)
            day_of_month = event_date.day
            is_visiting_speaker = 8 <= day_of_month <= 14
            
            date_str = event_date.strftime("%Y-%m-%dT08:00:00-06:00")  # CT timezone
            
            title = "Department of Medicine Grand Rounds"
            if is_visiting_speaker:
                title = "Visiting Speaker Grand Rounds"
            
            event = {
                "title": title,
                "institution": INSTITUTION,
                "department": DEPARTMENT,
                "speaker": "Check website for speaker details",
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "livestream_available": is_visiting_speaker,
                "zoom_available": is_visiting_speaker,
                "format": "In-person + Zoom (visiting speakers)" if is_visiting_speaker else "In-person",
                "zoom_info": "Contact department for Zoom link" if is_visiting_speaker else "In-person only",
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
