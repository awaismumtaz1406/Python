import requests
import csv
import time
import random
import argparse
from datetime import datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class JobScraper:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0 Safari/537.36"
            )
        }

    def fetch_page(self, keyword, page):
        # Fake Jobs site does not support pagination or search
        url = self.base_url

        print(f"[SCRAPING] {url}")

        time.sleep(random.uniform(1, 2))

        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return self.parse_html(response.text)

        except Exception as e:
            print(f"[ERROR] {e}")
            return []

    def parse_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        jobs = []

        job_cards = soup.select(".card-content")

        print(f"[INFO] Found {len(job_cards)} jobs")

        for card in job_cards:
            try:
                title = card.select_one("h2.title").get_text(strip=True)
                company = card.select_one("h3.company").get_text(strip=True)
                location = card.select_one("p.location").get_text(strip=True)

                link_tag = card.find("a")
                job_url = urljoin(self.base_url, link_tag["href"]) if link_tag else "N/A"

                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "url": job_url
                })

            except Exception as e:
                print(f"[PARSE ERROR] {e}")

        return jobs


def save_to_csv(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"jobs_{timestamp}.csv"

    keys = ["title", "company", "location", "url"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"\n[SUCCESS] Saved {len(data)} jobs to {filename}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", help="Search keyword (not used in demo site)")
    args = parser.parse_args()

    scraper = JobScraper("https://realpython.github.io/fake-jobs")

    all_jobs = []

    jobs = scraper.fetch_page(args.keyword, 1)
    all_jobs.extend(jobs)

    if all_jobs:
        save_to_csv(all_jobs)
    else:
        print("[INFO] No jobs found")


if __name__ == "__main__":
    main()

// requirements.txt
requests==2.33.1
beautifulsoup4==4.14.3






