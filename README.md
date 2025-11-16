# Grand Rounds Aggregator

## Project Goal

The goal of this project is to develop a public-facing, minimal static website that aggregates and displays Grand Rounds schedules from various medical institutions. The initial focus is on facilities in New England, with a plan to scale nationwide.

## Core Architecture

This project uses a serverless architecture automated with GitHub Actions.

1.  **Scraper**: A Python script (`scraper/main.py`) runs on a daily schedule via a GitHub Action. It dynamically executes individual scraper modules (e.g., `scraper/scrape_yale.py`) to collect event data from target websites.
2.  **Centralized Data**: The scraper aggregates all event information into a single `docs/data.json` file.
3.  **Auto-Update**: The GitHub Action automatically commits the updated `data.json` file back to this repository.
4.  **Static Frontend**: The `docs/index.html` page uses Alpine.js to fetch the `data.json` file and dynamically render the event list. It includes UI for filtering events by region, state, and keywords.
5.  **Auto-Deploy**: A second GitHub Action detects when new code (including the updated data file) is pushed to the `main` branch and automatically deploys the contents of the `/docs` directory as a static website using GitHub Pages.

## Project Structure

```
/
├── .github/
│   └── workflows/
│       ├── scrape_data.yml   # Workflow to run the scraper and commit data
│       └── deploy_site.yml   # Workflow to deploy the site to GitHub Pages
├── scraper/
│   ├── __init__.py
│   ├── main.py             # Main runner for all scrapers
│   └── template_scraper.py # Template for adding new institution scrapers
└── docs/
    ├── index.html          # Main frontend file
    ├── script.js           # Frontend logic with Alpine.js
    └── data.json           # Aggregated event data
```

## What Has Been Done

This repository contains the complete boilerplate structure for the project as described above. All the necessary files for the scraper, the frontend, and the automation workflows have been created.

## Next Steps

1.  **Customize Scrapers**: Copy the `scraper/template_scraper.py` for each target institution and customize the scraping logic to match the institution's website structure.
2.  **Enable GitHub Pages**: In the repository settings, enable GitHub Pages and set the source to deploy from the `/docs` folder.
3.  **Monetization**: Replace the placeholder affiliate links and ad slots in `docs/index.html` with actual monetization content.
