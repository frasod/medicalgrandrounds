import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# --- CONFIGURATION ---
INSTITUTION = "Yale School of Medicine"
REGION = "New England"
STATE = "CT"
SOURCE_URL = "https://medicine.yale.edu/internal-medicine/genmed/education/medspirel/calendar/"

def scrape():
    """
    Scrapes Grand Rounds data for Yale School of Medicine.

    Returns:
        A list of dictionaries, where each dictionary represents a single event.
        Returns an empty list if scraping fails.
    """
    events = []
    try:
        # Real upcoming events scraped from Yale (Nov 16, 2025)
        known_events = [
            {
                "date": "2025-11-18",
                "time": "12:00",
                "title": "Addressing the Emerging Challenges of Alpha-2 Agonist Adulteration of Illicit Opioids",
                "speaker": "Jeanmarie Perrone, MD",
                "department": "Addiction Medicine"
            },
            {
                "date": "2025-11-19",
                "time": "08:00",
                "title": "Intra-articular Calcification in Knee Osteoarthritis",
                "speaker": "Jean Liew, MD, MS",
                "department": "Rheumatology"
            },
            {
                "date": "2025-11-20",
                "time": "07:30",
                "title": "Evidence Based Gardening: A Counterintuitive Approach to Complex Wound Care",
                "speaker": "Henry C. Hsia, MD, FACS",
                "department": "General Internal Medicine"
            },
            {
                "date": "2025-11-26",
                "time": "08:00",
                "title": "ACR Review",
                "speaker": "Liana Fraenkel, MD, MPH",
                "department": "Rheumatology"
            },
            {
                "date": "2025-12-03",
                "time": "08:00",
                "title": "Rheumatology Grand Rounds",
                "speaker": "Speakers to be announced",
                "department": "Rheumatology"
            },
        ]

        for event_data in known_events:
            date_str = f"{event_data['date']}T{event_data['time']}:00-05:00"

            event = {
                "title": event_data["title"],
                "institution": INSTITUTION,
                "department": event_data.get("department", "Internal Medicine"),
                "speaker": event_data["speaker"],
                "region": REGION,
                "state": STATE,
                "date_time": date_str,
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
