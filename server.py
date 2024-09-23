from flask import Flask
from utils import process_resume_and_jd
from flask import request, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route'

@app.route('/magic', methods=['GET', 'POST'])
def magic():
    if request.method == 'POST':
        resume_file = request.files['resume']
        jd = request.form['jd']
        additional_info = request.form['additional_info']
        if additional_info == '':
            additional_info = None
        
        resume_path = 'temp/' + resume_file.filename
        resume_file.save(resume_path)
        
        response = process_resume_and_jd(resume_path, jd, 'pdf', 'txt', additional_info)
        
        os.remove(resume_path)
        
        return response
    
    return render_template('index.html')

app.run(port=5000, debug=True)