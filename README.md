# Rank Gazer: Daily App Store Ranking Scraper

This repository contains a Python script and a GitHub Actions workflow that automates the process of scraping data from multiple Apple App Store app pages. The workflow runs daily at a predefined time (09:00 UTC) or can be triggered manually, and it collects information such as:

- App ranking in the Medical category.
- App star rating.
- Total number of ratings.

The scraped data is appended to a CSV file stored in a separate branch (`data-branch`) to keep the main branch clean.

## Features

- Scrapes data from multiple App Store app pages.
- Runs automatically every day at 09:00 UTC.
- Stores data in a CSV file (`apps_ranking.csv`) in the `data-branch`.
- Easily extendable to scrape additional apps by editing the workflow matrix.

## How It Works

1. The **GitHub Actions workflow** is configured to run daily using a cron job (`cron: '0 9 * * *'`) or can be manually triggered from the "Actions" tab in the repository.
2. For each app URL defined in the workflow, the script will scrape the app's ranking, star rating, and the total number of reviews.
3. The scraped data is then appended to the `apps_ranking.csv` file in the `data-branch`.
4. Each job runs in parallel for faster scraping of multiple apps.

## Running the Scraper Locally

If you want to test the scraper locally before running it on GitHub Actions, you can follow these steps:

### Prerequisites

- Python 3.x installed on your local machine.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Install the required dependencies: The dependencies are listed in the `requirements.txt` file. To install them, run:

```bash
pip install -r requirements.txt
```

3. **Run the scraper**: You can run the scraper for a specific app URL by executing the `run_scraper.py` script and passing the app URL as a parameter:

```bash
python run_scraper.py --app_url "https://apps.apple.com/us/app/google/id284815942"
```

4. **Check the output**: The scraped data will be appended to `apps_ranking.csv`, which will be created in the local directory if it doesn't already exist.


## Setup

### Prerequisites

- Python 3.x
- GitHub repository

### Workflow Configuration

The workflow is defined in `.github/workflows/scraper.yml`. The workflow uses a matrix strategy to run the scraping job for multiple app URLs in parallel.

To modify the list of apps being scraped:
1. Edit the `matrix.app_url` section in the `.github/workflows/scraper.yml` file.
2. Add or remove app URLs in the list:
   ```yaml
   matrix:
     app_url: [
       "https://apps.apple.com/us/app/google/id284815942",
     ]

### Running the Workflow
There are two ways to run the scraping workflow:

1. Automatic Daily Runs: The workflow will run automatically every day at 09:00 UTC based on the cron schedule.
2. Manual Trigger: You can manually trigger the workflow via the "Actions" tab in the GitHub repository:
    - Go to the Actions tab.
    - Select the "Daily Scraper" workflow.  
    - Click on the "Run workflow" button to start the scraper immediately.

### Modifying the Scraper Script
The Python script `run_scraper.py` is designed to take an `--app_url` argument, which is passed by the GitHub Actions workflow for each app in the matrix. The script scrapes the app's ranking, rating, and total number of reviews and appends it to the CSV file.

Feel free to modify the scraping logic or add additional data points to be extracted as needed.

### CSV Output
- The scraped data is stored in a CSV file (scraped_data.csv) in the data-branch.
- Each row in the CSV contains the following columns:
    - Timestamp: The date and time of the scraping run.
    - App URL: The URL of the scraped app.
    - Ranking: The app's ranking in its category.
    - Star Rating: The app's star rating.
    - Total Number of Ratings: The total number of user ratings.


### Data Branch
All scraped data is committed to the data-branch to keep the main branch clean. You can access the data-branch directly or fetch the CSV file from there.
