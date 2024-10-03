from flask import Flask
from flask_cors import CORS
from utils import process_resume_and_jd
from flask import request, render_template
import os
import tempfile
from flask import jsonify

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

@app.route('/')
def home():
    return 'Home Page Route'

@app.route('/magic', methods=['GET'])
def magic_form():
    return "Resume Magic API"

@app.route('/magic', methods=['POST'])
def magic():
    resume_file = request.files['resume']
    jd = request.form.get('jd', 'Optimize Resume') 
    additional_info = request.form.get('additional_info', None)  
    
    with tempfile.NamedTemporaryFile(delete=False) as resume_temp:
        resume_temp.write(resume_file.read())
        resume_path = resume_temp.name
        
        response_data = process_resume_and_jd(resume_path, jd, 'pdf', additional_info)
    
    os.remove(resume_path)
    
    return jsonify(response_data)

@app.route('/staticjson', methods=['GET'])
def static_json():
    return jsonify({
    "certifications": [
        {
            "date": "",
            "name": "Computer Hardware Certification"
        },
        {
            "date": "",
            "name": "Java Course"
        }
    ],
    "education": [
        {
            "degree": {
                "gpa": "7.94",
                "name": "BE Computer Engineering",
                "passing_year": "2024",
                "university": "Mumbai University"
            },
            "high_school": {
                "gpa": "85.37%",
                "name": "Diploma In Computer Engineering",
                "passing_year": "2021",
                "university": "MSBTE University"
            },
            "school": {
                "gpa": "59.23%",
                "name": "HSC (Computer Science)",
                "passing_year": "2019",
                "university": "Konkan Board"
            }
        }
    ],
    "email": "panditsanket2211@gmail.com",
    "experience": [
        {
            "company": "PHN Technology Pvt. Ltd.",
            "description": "Assisted in web development projects using HTML, CSS, JavaScript, and PHP. Worked with MySQL databases.",
            "end_date": "",
            "location": "Pune",
            "start_date": "",
            "title": "Web Development Internship"
        }
    ],
    "github": "",
    "linkedin": "linkedin.com/in/sanket-pandit-7559861a3",
    "location": "India",
    "name": "Sanket Pandit",
    "phone": "9405618195",
    "projects": [
        {
            "description": "Performed end-to-end manual testing for a mock e-commerce website to validate functional requirements. Automated test cases for key features such as product search, shopping cart, and payment process using Selenium WebDriver and TestNG.",
            "link": "",
            "title": "E-Commerce Website Testing"
        },
        {
            "description": "Conducted comprehensive API testing for a user authentication system, covering login, registration, password reset, and token validation features.",
            "link": "",
            "title": "API Testing of Authentication Application"
        }
    ],
    "skills": [
        "Testing Tools: Selenium, JUnit, TestNG, Postman, JIRA",
        "Automation Frameworks: Selenium WebDriver, Cucumber",
        "Manual Testing: Test Case Design, Regression Testing, UAT, Bug Tracking",
        "SDLC and STLC",
        "API Testing: REST API, Postman",
        "Version Control: Git, GitHub",
        "Test plan",
        "CI/CD Tools: Jenkins (basic understanding)",
        "SQL"
    ],
    "summary": "To achieve a responsible position and efficiently contribute to the industry by leveraging new technologies. Aiming to expand my knowledge through hard work and continuous learning."
})
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000 )