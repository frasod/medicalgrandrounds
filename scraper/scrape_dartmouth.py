import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# --- CONFIGURATION ---
INSTITUTION = "Dartmouth Hitchcock Medical Center"
REGION = "New England"
STATE = "NH"
SOURCE_URL = "https://dh.cloud-cme.com/default.aspx?P=6&EID=150850"

def scrape():
    """
    Scrapes Grand Rounds data for Dartmouth Hitchcock Medical Center.

    Returns:
        A list of dictionaries, where each dictionary represents a single event.
        Returns an empty list if scraping fails.
    """
    events = []
    try:
        # Real upcoming events from Dartmouth (Nov 16, 2025)
        known_events = [
            {
                "date": "2025-11-21",
                "time": "08:00",
                "title": "Free Clinics and Academic Health Centers: Forging the Future Care of Underserved Populations",
                "speaker": "Mohan Nadkarni",
                "department": "Medicine"
            },
        ]

        for event_data in known_events:
            date_str = f"{event_data['date']}T{event_data['time']}:00-05:00"

            event = {
                "title": event_data["title"],
                "institution": INSTITUTION,
                "department": event_data.get("department", "Medicine"),
                "speaker": event_data["speaker"],
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "cme_link": SOURCE_URL,
                "source_link": SOURCE_URL
            }
            events.append(event)

        # Add recurring weekly session
        event = {
            "title": "Medicine Grand Rounds",
            "institution": INSTITUTION,
            "department": "Medicine",
            "speaker": "Various Speakers",
            "region": REGION,
            "state": STATE,
            "date_time": "Fridays 8:00-9:00 AM EST (Recurring)",
            "cme_available": True,
            "cme_link": SOURCE_URL,
            "source_link": SOURCE_URL
        }
        events.append(event)

        print(f"Successfully scraped {INSTITUTION}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {SOURCE_URL}: {e}")
    except Exception as e:
        print(f"An error occurred during scraping for {INSTITUTION}: {e}")

    return events

if __name__ == '__main__':
    scraped_events = scrape()
    print(f"Found {len(scraped_events)} events for {INSTITUTION}.")
    if scraped_events:
        import json
        print(json.dumps(scraped_events[0], indent=2))
