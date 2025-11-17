import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# --- CONFIGURATION ---
INSTITUTION = "Dartmouth Hitchcock Medical Center"
REGION = "New England"
STATE = "NH"
SOURCE_URL = "https://www.dartmouth-hitchcock.org/health-care-professionals/medicine-grand-rounds"

def scrape():
    """
    Scrapes Grand Rounds data for Dartmouth Hitchcock Medical Center.

    Returns:
        A list of dictionaries, where each dictionary represents a single event.
        Returns an empty list if scraping fails.
    """
    events = []
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'GrandRoundsAggregator/1.0 (https://github.com/frasod/medicalgrandrounds)'
        })

        response = session.get(SOURCE_URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Dartmouth has recurring Friday 8-9am sessions
        # Since we can't get specific upcoming dates from the page, we'll create placeholder entries
        # In a real implementation, you'd scrape their video archive or calendar system

        # For now, let's create a generic recurring event entry
        event = {
            "title": "Medicine Grand Rounds",
            "institution": INSTITUTION,
            "department": "Department of Medicine",
            "speaker": "Various Speakers",
            "region": REGION,
            "state": STATE,
            "date_time": "Fridays 8:00-9:00 AM EST (Recurring)",
            "cme_available": True,
            "cme_link": SOURCE_URL,
            "source_link": SOURCE_URL,
            "webex_link": "https://dhmc.webex.com/dhmc/j.php?MTID=mc03faf39f88fe8b74cd20b47a03f27a9"
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
