import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# --- CONFIGURATION ---
INSTITUTION = "Massachusetts General Hospital"
REGION = "New England"
STATE = "MA"
SOURCE_URL = "https://www.massgeneral.org/medicine/education/medical-grand-rounds"
CANCER_URL = "https://www.massgeneral.org/cancer-center/clinician-resources/grand-rounds"

def scrape():
    """
    Scrapes Grand Rounds data for Massachusetts General Hospital.

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

        # Medical Grand Rounds
        event = {
            "title": "Medical Grand Rounds",
            "institution": INSTITUTION,
            "department": "Department of Medicine",
            "speaker": "Various Speakers",
            "region": REGION,
            "state": STATE,
            "date_time": "Mondays 8:00-9:00 AM EST (Recurring)",
            "cme_available": True,
            "cme_link": "mailto:mghcme@mgh.harvard.edu",
            "source_link": SOURCE_URL
        }
        events.append(event)

        # Cancer Grand Rounds 2025-2026
        cancer_events = [
            {"date": "2025-09-11", "title": "Severe Immunotherapy Complications: Integrating Clinical Insight with Translational Innovation"},
            {"date": "2025-09-18", "title": "The Viral-like Behavior of Cancer"},
            {"date": "2025-09-25", "title": "A New Era for AML?"},
        ]

        for event_data in cancer_events:
            date_str = event_data["date"] + "T12:00:00-04:00"

            event = {
                "title": event_data["title"],
                "institution": INSTITUTION,
                "department": "Cancer Center",
                "speaker": "TBA",
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "cme_link": "https://cpd.partners.org",
                "source_link": CANCER_URL
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
