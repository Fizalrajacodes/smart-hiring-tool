import re

def normalize(text):
    return re.sub(r'[^a-z0-9\s]', ' ', text.lower())

def match_skills(resume_text, job_skills):
    resume_text = normalize(resume_text)
    skills = [s.strip() for s in job_skills.split(',') if s.strip()]
    if not skills:
        return 0.0, []
    matched = 0
    missing = []
    for skill in skills:
        # match words or short phrases
        if skill and skill.lower() in resume_text:
            matched += 1
        else:
            missing.append(skill)
    score = (matched / len(skills)) * 100
    return score, missing
