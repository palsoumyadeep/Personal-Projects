import spacy
import pdfminer
import re
import os
import pandas as pd

import pdf2txt


def convert_pdf(f):
    output_filename = os.path.basename(os.path.splitext(f)[0]) + ".txt"
    output_filepath = os.path.join("output/txt/",output_filename)
    pdf2txt.main(args=[f, "--outfile", output_filepath])
    print(output_filepath + " file save successfully!!!")
    return open(output_filepath).read()


nlp = spacy.load("en_core_web_sm")

result_dict = {'name': [], 'phone' : [], 'email' : [], 'skills' : [] }
names = []
phones = []
emails = []
skills = []

def parse_content(text):
    t1 = "python"
    t2 = "java"
    t3 = "sql"
    t4 = "hadoop"
    t5 = "tableau"
    skill_combine = str(t1+'|'+t2+'|'+t3+'|'+t4+'|'+t5)
    skillset = re.compile(skill_combine)
    phone_num = re.compile("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ is "PERSON"][0]
    email = [word for word in doc if word.like_email == True][0]
    phone = str(re.findall(phone_num, text.lower()))
    skills_list = re.findall(skillset, text.lower())
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Extraction completed successfully")


for file in os.listdir('resumes/'):
    if file.endswith('.pdf'):
        print('Reading...'+file)
        text = convert_pdf(os.path.join('resumes/',file))
        parse_content(text)


result_dict['name'] = names
result_dict['phone'] = phones
result_dict['skills'] = skills
result_dict['email'] = emails

result_df = pd.DataFrame(result_dict)
result_df.to_excel('output/csv/parse_excel.xlsx')