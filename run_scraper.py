import argparse
import csv
import os
from datetime import datetime
from typing import List

import requests
from bs4 import BeautifulSoup


# Function to scrape the data
def scrape_data(app_url: str) -> List[str]:
    # Headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"  # noqa E501
    }

    # Fetching the main page content
    print(f"Scraping app URL: {app_url}")
    response = requests.get(app_url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    # Extracting ranking in Medical category
    ranking_tag = soup.find(
        "a", {"class": "inline-list__item"}, string=lambda text: "Medical" in text
    )
    ranking = ranking_tag.get_text(strip=True) if ranking_tag else "N/A"

    # Extracting star rating
    rating = soup.find(
        "span", {"class": "we-customer-ratings__averages__display"}
    ).get_text(strip=True)

    # Extracting total number of ratings
    num_ratings = soup.find("div", {"class": "we-customer-ratings__count"}).get_text(
        strip=True
    )

    # Get the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return [timestamp, app_url, ranking, rating, num_ratings]


# Function to append data to CSV
def append_to_csv(data: List[str], file_path: str = "apps_ranking.csv") -> None:
    # Column headers for the CSV
    headers = [
        "Timestamp",
        "App URL",
        "Ranking",
        "Star Rating",
        "Total Number of Ratings",
    ]

    try:
        # Ensure the file exists before opening it
        if not os.path.exists(file_path):
            with open(file_path, mode="w", newline="") as file:
                pass  # Create the file

        # Open the file in append mode, or create it if it doesn't exist
        with open(file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            # Check if the file is empty (add headers if it is)
            if file.tell() == 0:
                writer.writerow(headers)

            # Append the scraped data
            writer.writerow(data)

    except Exception as e:
        print(f"Error writing to CSV: {e}")


# Main function to run the scraper and update CSV
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rank Gazer: App Store Ranking Scraper"
    )
    parser.add_argument(
        "--app_urls",
        type=str,
        nargs="+",
        help="List of app URLs to scrape",
        required=True,
    )
    args = parser.parse_args()

    for app_url in args.app_urls:
        data = scrape_data(app_url)
        append_to_csv(data)
