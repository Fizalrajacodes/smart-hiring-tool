from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf
from skill_matcher import match_skills

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']
    job_skills = request.form['skills']

    resume_text = extract_text_from_pdf(file)
    score, missing = match_skills(resume_text, job_skills)

    return render_template("result.html", score=round(score,2), missing=missing)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
