from PyPDF2 import PdfReader
import docx
from langchain_groq import ChatGroq
import json
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_json(response):
    json_marker = "```json"
    
    json_start_index = response.find(json_marker)
    
    if json_start_index != -1:
        json_string = response[json_start_index + len(json_marker):].strip()
        
        json_string = json_string.split('```')[0].strip()  
        
        json_start = json_string.find('{')
        
        if json_start != -1:
            json_string = json_string[json_start:]
            try:
                return json.loads(json_string)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
    
    return {}

def generate_ats_friendly_resume(resume_text, jd_text, additional_info=None):    
    prompt = f'''
    ### RESUME TEXT:
    {resume_text},
    ### JOB DESCRIPTION TEXT: 
    {jd_text},
    ### ADDITIONAL INFO:
    {additional_info}
    ### INSTRUCTION:
    Write ATS friendly Resume That Should Qualify for Above Job_Description\n
    Only return the valid JSON structured below.
    ### VALID JSON (NO PREAMBLE):
    ```json{{
        "name": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": "",
        "summary": "",
        "skills": [],
        "education": [
            {{
                "degree": {{
                    "name": "",
                    "passing_year": "",
                    "gpa": "",
                    "university": ""
                }},
                "high_school": {{
                    "name": "",
                    "passing_year": "",
                    "gpa": ""
                }},
                "school": {{
                    "name": "",
                    "passing_year": "",
                    "gpa": ""
                }}
            }}
        ],
        "experience": [
            {{
                "title": "",
                "company": "",
                "location": "",
                "start_date": "",
                "end_date": "",
                "description": ""
            }}
        ],
        "projects": [
            {{
                "title": "",
                "description": "",
                "link": ""
            }}
        ],
        "certifications": [
            {{
                "name": "",
                "date": ""
            }}
        ]
    }}
    ```
    '''
    llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key=groq_api_key,
    )

    response = llm.invoke(str(prompt))
    resume_data = extract_json(response.content)
    return resume_data

def process_resume_and_jd(resume_file_path, jd_text, resume_type, additional_info=None):
    resume_text = extract_text_from_pdf(resume_file_path)
    
    ats_friendly_resume = generate_ats_friendly_resume(resume_text, jd_text, additional_info)

    return ats_friendly_resume