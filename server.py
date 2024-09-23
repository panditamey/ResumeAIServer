from flask import Flask
from utils import process_resume_and_jd
from flask import request, render_template
import os
import tempfile
from flask import jsonify

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(debug=True)