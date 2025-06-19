import json
import re

#Step 1 : Load job listings

with open("../job_scraper/jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

print(f"Total jobs loaded: {len(jobs)}")

# Step 2: Load resume text
with open("../resumes/sample_resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read().lower()

print(f"\nSample resume loaded. Length: {len(resume_text)} characters")

#Step 3: Extract keywords from resume
# we'll remove spl char and split the resume into words

cleaned_resume = re.sub(r"[^\w\s]","", resume_text) #removes punctuation
words = cleaned_resume.split() #split into words
keywords = set(words) #convert to set to avoid duplicates

print(f"\nTotal uniques keywords extracted from resume: {len(keywords)}")

#Step 4: Score each job based on keyword matches

for job in jobs:
    title = job.get("title", "").lower()
    company = job.get("company", "").lower()
    location = job.get("location", "").lower()
    description = job.get("description", "").lower() if "description" in job else ""

    combined_text = f"{title} {company} {location} {description}"

    # Count how many resume keywords are found in job content
    match_count = sum(1 for keyword in keywords if keyword in combined_text)
    job["match_score"] = match_count  # attach score to job

# Optional: Print top 3 matching jobs
sorted_jobs = sorted(jobs, key=lambda x: x["match_score"], reverse=True)
print("\nTop 3 Matching Jobs:")
for job in sorted_jobs[:3]:
    print(f"{job['title']} at {job['company']} - Score: {job['match_score']}")

# Step 5: Save top 10 matching jobs to a file
top_matches = sorted_jobs[:10]

with open("matched_jobs.json", "w", encoding="utf-8") as f:
    json.dump(top_matches, f, indent=4)

print("\nTop matches saved to matched_jobs.json ✅")

