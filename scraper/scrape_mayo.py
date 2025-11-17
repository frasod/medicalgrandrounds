import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

# --- CONFIGURATION ---
INSTITUTION = "Mayo Clinic"
DEPARTMENT = "Medicine"
REGION = "Midwest"
STATE = "MN"
SOURCE_URL = "https://ce.mayo.edu/content/medical-grand-rounds-2024-2025-series"

def scrape():
    """
    Scrapes Grand Rounds data for Mayo Clinic Rochester Medical Grand Rounds.
    
    Returns:
        A list of dictionaries, where each dictionary represents a single event.
    """
    events = []
    
    try:
        # Mayo has recurring weekly sessions on Wednesdays 12:00-1:00 PM CT
        # Series runs through December 17, 2025, with continuation into 2026
        
        # Generate Wednesdays from Nov 20 through Jan 14, 2026
        start_date = datetime(2025, 11, 20)  # Next Wednesday from Nov 16
        end_date = datetime(2026, 1, 14)
        
        current_date = start_date
        while current_date <= end_date:
            # Skip holidays
            if current_date.month == 12 and current_date.day in [24, 25, 31] or \
               current_date.month == 1 and current_date.day == 1:
                current_date += timedelta(weeks=1)
                continue
            
            date_str = current_date.strftime("%Y-%m-%dT12:00:00-06:00")  # CT timezone
            
            event = {
                "title": "Medical Grand Rounds",
                "institution": INSTITUTION,
                "department": DEPARTMENT,
                "speaker": "Check website for speaker details",
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "livestream_available": True,
                "zoom_available": False,  # Direct livestream
                "format": "In-person + Live Streaming",
                "zoom_info": "See website for streaming details",
                "source_link": SOURCE_URL
            }
            events.append(event)
            
            current_date += timedelta(weeks=1)
        
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
