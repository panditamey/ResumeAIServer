from flask import Flask
from utils import process_resume_and_jd
from flask import request, render_template
import os
import tempfile

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
        
        with tempfile.NamedTemporaryFile(delete=False) as resume_temp:
            resume_temp.write(resume_file.read())
            resume_path = resume_temp.name
            
            response = process_resume_and_jd(resume_path, jd, 'pdf',  additional_info)
        
        os.remove(resume_path)
        
        return response
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)