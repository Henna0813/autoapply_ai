import json
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

# Automatically installs the right version of ChromeDriver for you
chromedriver_autoinstaller.install()

def scrape_jobs():
    print("🚀 Opening browser to look for QA jobs...")
    driver = webdriver.Chrome()
    driver.get("https://remoteok.com/remote-qa-jobs")

    # Give the website a few seconds to load everything
    time.sleep(3)

    jobs = []

    print("🔍 Searching for job listings...")
    listings = driver.find_elements(By.CSS_SELECTOR, "tr.job")

    for job in listings:
        try:
            title = job.find_element(By.CSS_SELECTOR, "td.position h2").text
            company = job.find_element(By.CSS_SELECTOR, "td.company h3").text
            location = job.find_element(By.CSS_SELECTOR, "div.location").text
            link = job.find_element(By.CSS_SELECTOR, "a.preventLink").get_attribute("href")

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "link": link
            })

        except Exception as e:
            print("⚠️ Skipping one job posting due to an error:", e)
            continue

    driver.quit()

    # Save all the job data into a file
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2)

    print(f"✅ Done! Saved {len(jobs)} QA jobs to 'jobs.json'")

if __name__ == "__main__":
    scrape_jobs()

