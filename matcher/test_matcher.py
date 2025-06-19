import os
import json

def test_matched_jobs_file_exists():
    assert os.path.exists("matched_jobs.json"), "matched_jobs.json was not created"

def test_matched_jobs_structure():
    with open("matched_jobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)

    assert isinstance(jobs, list), "Expected a list of jobs"
    assert len(jobs) > 0, "No jobs found in matched_jobs.json"
    for job in jobs:
        assert "match_score" in job, "Missing match_score in job data"
