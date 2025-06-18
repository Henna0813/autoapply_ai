import json
import os

def test_jobs_file_exists():
    assert os.path.exists("jobs.json"), "jobs.json file not found."

def test_jobs_file_valid_json():
    with open("jobs.json", "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            assert False, "jobs.json is not valid JSON"

def test_jobs_not_empty():
    with open("jobs.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) > 0, "jobs.json is empty"

