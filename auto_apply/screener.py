import re
import json
import os

def load_resume_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_fields(text):
    fields = {}
    fields['name'] = re.findall(r'Name:\s*(.*)', text)
    fields['email'] = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    fields['phone'] = re.findall(r'\+?\d[\d\s\-]{8,}', text)
    fields['skills'] = re.findall(r'Skills:\s*(.*)', text)
    fields['experience'] = re.findall(r'Experience:\s*(.*)', text)
    fields['education'] = re.findall(r'Education:\s*(.*)', text)
    return {
        "name": fields['name'][0] if fields['name'] else "",
        "email": fields['email'][0] if fields['email'] else "",
        "phone": fields['phone'][0] if fields['phone'] else "",
        "skills": [skill.strip() for skill in fields['skills'][0].split(',')] if fields['skills'] else [],
        "experience": int(re.findall(r'\d+', fields['experience'][0])[0]) if fields['experience'] else 0,
        "education": fields['education'][0] if fields['education'] else ""
    }

def load_job_template(template_path):
    with open(template_path, "r") as f:
        return json.load(f)

def score_resume(resume_data, job_template):
    skill_match_count = len(set(resume_data["skills"]).intersection(set(job_template["required_skills"])))
    total_required_skills = len(job_template["required_skills"])

    skill_score = (skill_match_count / total_required_skills) * 60 if total_required_skills > 0 else 0
    experience_score = 25 if resume_data["experience"] >= job_template["min_experience"] else 10
    education_score = 15 if job_template["education"].lower() in resume_data["education"].lower() else 5

    total_score = round(skill_score + experience_score + education_score, 2)

    return {
        "name": resume_data["name"],
        "email": resume_data["email"],
        "score": total_score,
        "skills_matched": skill_match_count,
        "total_skills_required": total_required_skills
    }

def run_screener(resume_path, job_template_path):
    text = load_resume_text(resume_path)
    resume_data = extract_fields(text)
    job_template = load_job_template(job_template_path)
    result = score_resume(resume_data, job_template)
    return result

if __name__ == "__main__":
    # ⬇️ Dynamically create paths regardless of OS
    current_dir = os.path.dirname(os.path.abspath(__file__))         # auto_apply/
    base_dir = os.path.dirname(current_dir)                          # autoapply_ai/

    resume_file = os.path.join(base_dir, "resumes", "sample_resume.txt")
    template_file = os.path.join(base_dir, "templates", "qa_job_template.json")

    result = run_screener(resume_file, template_file)
    print("\n✅ Screening Result:")
    print(json.dumps(result, indent=2))

