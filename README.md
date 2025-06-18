# 🧠 AutoApply AI – Resume + Job Automation Toolkit

This is a smart, personal automation toolkit built by **Henna Taneja** to help simplify the job application process. It uses **Python, Selenium, and Pytest** to extract resume data, match job templates, and scrape remote job listings.

---

## 📁 Project Structure

```
autoapply_ai/
├── resume_parser/          # Day 1: Extracts raw text from a resume file
├── resume_screener/        # Day 2: Matches your resume with a job template
├── job_scraper/            # Day 3: Scrapes remote QA jobs from a website
```

---

## 🔧 How Each Part Works

### ✅ Day 1: Resume Parser
- Reads plain text from `.txt` or `.pdf` resumes
- Converts it into structured data for screening

### ✅ Day 2: Resume Screener
- Compares your resume with a job description template
- Uses keyword matching to calculate a score
- Saves match results to `result.json`

### ✅ Day 3: Job Scraper
- Uses Selenium to open [remoteok.com](https://remoteok.com/remote-qa-jobs)
- Collects job title, company, location, and link
- Saves output to `jobs.json`
- Includes `pytest` tests to validate scraping success

---

## 📦 Technologies Used

- Python 3.10+
- Selenium WebDriver
- Chromedriver Auto Installer
- Pytest (for basic test automation)
- JSON, Regex, and File Handling
- Git & GitHub for version control

---

## 🚀 How to Run

> Make sure you’re inside the project folder!

### Install dependencies:
```bash
pip install selenium chromedriver-autoinstaller pytest
```

### Run the job scraper:
```bash
cd job_scraper
python scraper.py
```

### Run the resume screener:
```bash
cd resume_screener
python screener.py
```

---

## 💼 Built With Love By:

**Henna Taneja**  
`QA Engineer | Python Automation | Learning Generative AI`   
📂 [GitHub Portfolio](https://github.com/Henna0813)

---

## ⭐️ Want to Contribute?

Feel free to fork the repo and make improvements! Future versions may include:
- Chatbot to answer job-related questions
- Integration with job boards APIs
- Flask UI to make it more interactive
