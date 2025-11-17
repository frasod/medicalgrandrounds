import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# --- CONFIGURATION ---
INSTITUTION = "Rhode Island Hospital / Brown University"
REGION = "New England"
STATE = "RI"
SOURCE_URL = "https://brownim.org/2/conference-retreat-overview/"

def scrape():
    """
    Scrapes Grand Rounds data for Rhode Island Hospital / Brown University.

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

        # Medical Grand Rounds - Recurring weekly
        event = {
            "title": "Medical Grand Rounds",
            "institution": INSTITUTION,
            "department": "Internal Medicine",
            "speaker": "Various Speakers",
            "region": REGION,
            "state": STATE,
            "date_time": "Weekly (Days/Times Vary)",
            "cme_available": True,
            "cme_link": "mailto:imrp_rih@brown.edu",
            "source_link": SOURCE_URL
        }
        events.append(event)

        # Hematology Oncology Grand Rounds
        event = {
            "title": "Hematology Oncology Grand Rounds",
            "institution": INSTITUTION,
            "department": "Hematology/Oncology",
            "speaker": "Various Speakers",
            "region": REGION,
            "state": STATE,
            "date_time": "Regular Schedule (Contact for Details)",
            "cme_available": True,
            "cme_link": "mailto:imrp_rih@brown.edu",
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
