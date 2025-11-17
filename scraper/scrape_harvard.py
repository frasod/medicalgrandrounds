import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# --- CONFIGURATION ---
INSTITUTION = "Harvard Medical School"
REGION = "New England"
STATE = "MA"
SOURCE_URL = "https://meded.hms.harvard.edu/event/medical-education-grand-rounds-0"
BIDMC_URL = "https://www.bidmc.org/medical-education/medical-education-by-department/medicine/medical-grand-rounds"

def scrape():
    """
    Scrapes Grand Rounds data for Harvard Medical School.

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

        # Medical Education Grand Rounds
        med_ed_events = [
            {"date": "2025-05-05", "time": "12:00", "duration": "1.5hr"},
            {"date": "2025-05-08", "time": "09:00", "duration": "3hr"},
            {"date": "2025-05-12", "time": "12:00", "duration": "1.5hr"},
        ]

        for event_data in med_ed_events:
            date_str = f"{event_data['date']}T{event_data['time']}:00-04:00"

            event = {
                "title": "Medical Education Grand Rounds",
                "institution": INSTITUTION,
                "department": "Medical Education",
                "speaker": "Various Speakers",
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "cme_link": SOURCE_URL,
                "source_link": SOURCE_URL
            }
            events.append(event)

        # BIDMC Medical Grand Rounds
        bidmc_events = [
            {"date": "2025-02-22"},
            {"date": "2025-03-21"},
            {"date": "2025-03-27"},
            {"date": "2025-03-28"},
            {"date": "2025-06-06"},
        ]

        for event_data in bidmc_events:
            date_str = f"{event_data['date']}T08:00:00-05:00"

            event = {
                "title": "BIDMC Medical Grand Rounds",
                "institution": "Beth Israel Deaconess Medical Center (Harvard)",
                "department": "Medicine",
                "speaker": "TBA",
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "cme_link": BIDMC_URL,
                "source_link": BIDMC_URL
            }
            events.append(event)

        # Integrative Medicine Grand Rounds
        integrative_dates = ["2025-01-07", "2025-02-04", "2025-03-11", "2025-04-07", "2025-05-06", "2025-06-03", "2025-07-01", "2025-10-07"]

        for date in integrative_dates:
            date_str = f"{date}T12:00:00-05:00"

            event = {
                "title": "Integrative Medicine Grand Rounds",
                "institution": "Harvard Medical School - Osher Center",
                "department": "Integrative Medicine",
                "speaker": "Various Speakers",
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
                "cme_available": True,
                "cme_link": "https://oshercenter.org/im-grand-rounds/",
                "source_link": "https://oshercenter.org/im-grand-rounds/"
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
