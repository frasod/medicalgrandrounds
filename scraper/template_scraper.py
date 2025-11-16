import requests
from bs4 import BeautifulSoup
from datetime import datetime

# --- CONFIGURATION ---
# It's good practice to keep these at the top for easy updates.
INSTITUTION = "Example University"
REGION = "New England"
STATE = "MA"
SOURCE_URL = "http://example.com/grand-rounds"

def scrape():
    """
    Scrapes Grand Rounds data for a single institution.
    
    Returns:
        A list of dictionaries, where each dictionary represents a single event.
        Returns an empty list if scraping fails.
    """
    events = []
    try:
        # Use a session for potential cookie handling and connection pooling
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'GrandRoundsAggregator/1.0 (https://github.com/your-repo/grandrounds-aggregator)'
        })
        
        response = session.get(SOURCE_URL, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # --- SCRAPING LOGIC ---
        # This is the part you will customize for each institution's website structure.
        # The following is a placeholder example.
        
        event_containers = soup.find_all('div', class_='event-listing')
        
        for item in event_containers:
            title = item.find('h2', class_='event-title').text.strip()
            speaker = item.find('p', class_='speaker-name').text.strip()
            
            # Date and time parsing requires careful handling
            date_str = item.find('span', class_='event-date').text.strip() # e.g., "November 25, 2025, 8:00 AM"
            # Example parsing - this will need to be adjusted for each site's format
            parsed_datetime = datetime.strptime(date_str, "%B %d, %Y, %I:%M %p")
            iso_datetime = parsed_datetime.isoformat() + "-05:00" # Assuming EST, adjust as needed

            event = {
                "title": title,
                "institution": INSTITUTION,
                "department": "General Medicine", # Or scrape this if available
                "speaker": speaker,
                "region": REGION,
                "state": STATE,
                "date_time": iso_datetime,
                "cme_available": "CME" in item.text, # Simple check, can be improved
                "cme_link": item.find('a', href=True, string="CME Info")['href'] if item.find('a', string="CME Info") else None,
                "source_link": SOURCE_URL
            }
            events.append(event)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {SOURCE_URL}: {e}")
    except Exception as e:
        print(f"An error occurred during scraping for {INSTITUTION}: {e}")
        
    return events

if __name__ == '__main__':
    # For testing the individual scraper
    scraped_events = scrape()
    print(f"Found {len(scraped_events)} events for {INSTITUTION}.")
    # Print first event if available, for quick inspection
    if scraped_events:
        import json
        print(json.dumps(scraped_events[0], indent=2))
