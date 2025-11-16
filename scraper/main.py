import os
import importlib
import json
from datetime import datetime, timezone

def run_scrapers():
    """
    Dynamically discovers and runs all scraper modules in the 'scraper' directory.
    A module is considered a scraper if it has a 'scrape()' function.
    """
    all_events = []
    scraper_dir = os.path.dirname(__file__)

    for filename in os.listdir(scraper_dir):
        if filename.startswith("scrape_") and filename.endswith(".py"):
            module_name = f"scraper.{filename[:-3]}"
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, 'scrape') and callable(module.scrape):
                    print(f"Running scraper: {module_name}...")
                    events = module.scrape()
                    if events:
                        all_events.extend(events)
                    print(f"Finished scraper: {module_name}, found {len(events)} events.")
                else:
                    print(f"Warning: {module_name} does not have a callable 'scrape' function.")
            except Exception as e:
                print(f"Error running scraper {module_name}: {e}")

    return all_events

def save_data(events):
    """
    Saves the aggregated event data to the /docs/data.json file.
    """
    output_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'data.json')
    
    # Get current UTC time for the 'last_updated' timestamp
    last_updated_utc = datetime.now(timezone.utc).isoformat()

    data = {
        "last_updated": last_updated_utc,
        "events": events
    }

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved {len(events)} events to {output_path}")
    except IOError as e:
        print(f"Error writing to file {output_path}: {e}")


if __name__ == "__main__":
    print("Starting the Grand Rounds aggregation process...")
    aggregated_events = run_scrapers()
    
    # Optional: Sort events by date before saving
    aggregated_events.sort(key=lambda x: x.get('date_time', ''))

    save_data(aggregated_events)
    print("Aggregation process finished.")
