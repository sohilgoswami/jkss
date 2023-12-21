import fitz
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
engrPdfSpring23Url = 'https://web-as.tamu.edu/GradeReports/PDFReports/20231/grd20231EN.pdf'
artAndScienceSpring23Url = "https://web-as.tamu.edu/GradeReports/PDFReports/20231/grd20231AT.pdf"
engrPdfFall22Url = 'https://web-as.tamu.edu/GradeReports/PDFReports/20223/grd20223EN.pdf'
artAndScienceFall22Url = 'https://web-as.tamu.edu/GradeReports/PDFReports/20223/grd20223AT.pdf'


def extract_text_from_pdf(pdf_url):
    response = requests.get(pdf_url, stream=True)
    with fitz.open("pdf", response.content) as doc:
        pdf_text = ""
        for page in doc:
            pdf_text += page.get_text()
    return pdf_text

# Function to collect data for all classes
def collect_data_for_all_classes(pdf_text):
    data_collected = False
    collected_data = []
    for line in pdf_text.split("\n"):
        collected_data.append(line)
    return collected_data

# Function to collect data between "CSCE_120" and "CSCE_121"
def collect_data_between_120_and_121(pdf_text):
    data_collected = False
    collected_data = []
    for line in pdf_text.split("\n"):
        if "CSCE-120" in line:
            data_collected = True
        elif "CSCE-121" in line:
            data_collected = False
            break
        if data_collected:
            collected_data.append(line)
    return collected_data

# Function to collect data between "ENGR_102" and "ENGR_216"
def collect_data_between_102_and_216(pdf_text):
    data_collected = False
    collected_data = []
    for line in pdf_text.split("\n"):
        if "ENGR-102" in line:
            data_collected = True
        elif "ENGR-216" in line:
            data_collected = False
            break
        if data_collected:
            collected_data.append(line)
    return collected_data

# Function to collect data between "ENGR_216" and "ENGR_217"
def collect_data_between_216_and_217(pdf_text):
    data_collected = False
    collected_data = []
    for line in pdf_text.split("\n"):
        if "ENGR-216" in line:
            data_collected = True
        elif "ENGR-217" in line:
            data_collected = False
            break
        if data_collected:
            collected_data.append(line)
    return collected_data

# Function to collect data between "MATH_152" and "MATH_167"
def collect_data_between_152_and_167(pdf_text):
    data_collected = False
    collected_data = []
    for line in pdf_text.split("\n"):
        if "MATH-152" in line:
            data_collected = True
        elif "MATH-167" in line:
            data_collected = False
            break
        if data_collected:
            collected_data.append(line)
    return collected_data

# Function to collect data between "MATH_308" and "MATH_309"
def collect_data_between_308_and_309(pdf_text):
    data_collected = False
    collected_data = []
    for line in pdf_text.split("\n"):
        if "MATH-308" in line:
            data_collected = True
        elif "MATH-309" in line:
            data_collected = False
            break
        if data_collected:
            collected_data.append(line)
    return collected_data

engr_pdf_spring23_text = extract_text_from_pdf(engrPdfSpring23Url)
art_science_spring23_text = extract_text_from_pdf(artAndScienceSpring23Url)
engr_pdf_fall22_text = extract_text_from_pdf(engrPdfFall22Url)
art_science_fall22_text = extract_text_from_pdf(artAndScienceFall22Url)

#formatting data for all classes
def format_all_classes(engr_pdf, art_science_pdf):
    engr_class_data = collect_data_for_all_classes(engr_pdf)
    lines_engr_classes = [line.strip() for line in engr_class_data]
    filter_lines_classes = []
    for i in lines_engr_classes:
        if ("SECTION" in i):
            append = False
        if ("DEPARTMENT" in i):
            append = False
        if('Undergraduate' in i):
            append = True
            continue
        if append: 
            filter_lines_classes.append(i)
    art_science_class_data = collect_data_for_all_classes(art_science_pdf)
    lines_art_science_classes = [line.strip() for line in art_science_class_data]
    for i in lines_art_science_classes:
        if ("SECTION" in i):
            append = False
        if ("DEPARTMENT" in i):
            append = False
        if('ASTR-102' in i):
            append = False
        if('Undergraduate' in i):
            append = True
            continue
        if append: 
            filter_lines_classes.append(i)
    chunks_classes = [filter_lines_classes[x:x + 15] for x in range(0, len(filter_lines_classes), 15)]
    chunks_classes = chunks_classes[:-1]
    for i in chunks_classes:
        i.pop(13)
    return chunks_classes

#formatting csce_120_to_121_data
csce_120_to_121_data = collect_data_between_120_and_121(engr_pdf_spring23_text)
lines_120 = [line.strip() for line in csce_120_to_121_data]
filter_lines_120 = []
for i in lines_120:
    if ("SECTION" in i):
        append = False
    if('CSCE-120' in i):
        append = True
    if append: 
        filter_lines_120.append(i)
chunks_120 = [filter_lines_120[x:x + 15] for x in range(0, len(filter_lines_120), 15)]
chunks_120 = chunks_120[:-1]
for i in chunks_120:
    i.pop(13)

#Formatting ENGR 102 Data
engr_102_to_216_data = collect_data_between_102_and_216(engr_pdf_spring23_text)
lines_102 = [line.strip() for line in engr_102_to_216_data]
filter_lines_102 = []
for i in lines_102:
    if ("SECTION" in i):
        append = False
    if('ENGR-102' in i):
        append = True
    if append: 
        filter_lines_102.append(i)
chunks_102 = [filter_lines_102[x:x + 15] for x in range(0, len(filter_lines_102), 15)]
chunks_102 = chunks_102[:-1]
for i in chunks_102:
    i.pop(13)

#Formatting ENGR 216 Data
engr_216_to_217_data = collect_data_between_216_and_217(engr_pdf_spring23_text)
lines_216 = [line.strip() for line in engr_216_to_217_data]
filter_lines_216 = []
for i in lines_216:
    if ("SECTION" in i):
        append = False
    if('ENGR-216' in i):
        append = True
    if append: 
        filter_lines_216.append(i)
chunks_216 = [filter_lines_216[x:x + 15] for x in range(0, len(filter_lines_216), 15)]
chunks_216 = chunks_216[:-1]
for i in chunks_216:
    i.pop(13)

#Formatting MATH 152 Data
math_152_to_167_data = collect_data_between_152_and_167(art_science_spring23_text)
lines_152 = [line.strip() for line in math_152_to_167_data]
filter_lines_152 = []
for i in lines_152:
    if ("SECTION" in i):
        append = False
    if('MATH-152' in i):
        append = True
    if append: 
        filter_lines_152.append(i)
chunks_152 = [filter_lines_152[x:x + 15] for x in range(0, len(filter_lines_152), 15)]
chunks_152 = chunks_152[:-1]
for i in chunks_152:
    i.pop(13)

#Formatting MATH 308 Data
math_308_to_309_data = collect_data_between_308_and_309(art_science_spring23_text)
lines_308 = [line.strip() for line in math_308_to_309_data]
filter_lines_308 = []
for i in lines_308:
    if ("SECTION" in i):
        append = False
    if('MATH-308' in i):
        append = True
    if append: 
        filter_lines_308.append(i)
chunks_308 = [filter_lines_308[x:x + 15] for x in range(0, len(filter_lines_308), 15)]
chunks_308 = chunks_308[:-1]
for i in chunks_308:
    i.pop(13)

#setting up routes
@app.route('/get-courses')
def get_courses():
    courses_list = []
    count = 0
    chunks_classes = format_all_classes(engr_pdf_spring23_text, art_science_spring23_text)
    for i in chunks_classes:
        if("COURSE" in i[0]):
            continue
        courses_list.append({'id': count, 'term': 'Spring 2023', "course": i[0], 'professor': i[13], 'perA': i[2], 'perB': i[4], 'perC': i[6], 'perD': i[8], 'perF': i[10], 'GPA': i[12] })
        count = count + 1
    chunks_classes2 = format_all_classes(engr_pdf_fall22_text, art_science_fall22_text)
    for i in chunks_classes2:
        if("COURSE" in i[0]):
            continue
        courses_list.append({'id': count, 'term': 'Fall 2022', "course": i[0], 'professor': i[13], 'perA': i[2], 'perB': i[4], 'perC': i[6], 'perD': i[8], 'perF': i[10], 'GPA': i[12] })
        count = count + 1
    return jsonify(courses_list)
@app.route('/get-course-numbers')
def get_course_numbers():
    course_numbers_list = []
    course_list = []
    count = 0
    chunks_classes = format_all_classes(engr_pdf_spring23_text, art_science_spring23_text)
    chunks_classes2 = format_all_classes(engr_pdf_fall22_text, art_science_fall22_text)
    for i in chunks_classes:
        if("COURSE" in i[0]):
            continue
        course = i[0].split('-')
        course = course[0:2]
        if course not in course_list:
            course_list.append(course)
            course_numbers_list.append({'id': count,'subject': course[0], 'number': course[1]})
            count = count + 1
    for i in chunks_classes2:
        if("COURSE" in i[0]):
            continue
        course = i[0].split('-')
        course = course[0:2]
        if course not in course_list:
            course_list.append(course)
            course_numbers_list.append({'id': count,'subject': course[0], 'number': course[1]})
            count = count + 1
    return jsonify(course_numbers_list)
@app.route('/get-professors')
def get_professors():
    professor_list = []
    professors = []
    count = 0
    chunks_classes = format_all_classes(engr_pdf_spring23_text, art_science_spring23_text)
    chunks_classes2 = format_all_classes(engr_pdf_fall22_text, art_science_fall22_text)
    for i in chunks_classes:
        if("COURSE" in i[0]):
            continue
        if i[13] not in professor_list:
            professor_list.append(i[13])
            professors.append({'id': count, 'name': i[13]})
            count = count + 1
    for i in chunks_classes2:
        if("COURSE" in i[0]):
            continue
        if i[13] not in professor_list:
            professor_list.append(i[13])
            professors.append({'id': count, 'name': i[13]})
            count = count + 1
    return jsonify(professors)
@app.route('/get-course/120')
def get_course_120():
    csce_120_list = []
    for i in chunks_120:
        if("COURSE" in i[0]):
            break
        csce_120_list.append({"course": i[0], 'professor': i[13], 'perA': i[2], 'perB': i[4], 'perC': i[6], 'perD': i[8], 'perF': i[10], 'GPA': i[12] })
    return jsonify(csce_120_list)
@app.route('/get-course/102')
def get_course_102():
    engr_102_list = []
    for i in chunks_102:
        if("COURSE" in i[0]):
            break
        engr_102_list.append({"course": i[0], 'professor': i[13], 'perA': i[2], 'perB': i[4], 'perC': i[6], 'perD': i[8], 'perF': i[10], 'GPA': i[12] })
    return jsonify(engr_102_list)
@app.route('/get-course/216')
def get_course_216():
    engr_216_list = []
    for i in chunks_216:
        if("COURSE" in i[0]):
            break
        engr_216_list.append({"course": i[0], 'professor': i[13], 'perA': i[2], 'perB': i[4], 'perC': i[6], 'perD': i[8], 'perF': i[10], 'GPA': i[12] })
    return jsonify(engr_216_list)
@app.route('/get-course/308')
def get_course_308():
    math_308_list = []
    for i in chunks_308:
        if("COURSE" in i[0]):
            break
        math_308_list.append({"course": i[0], 'professor': i[13], 'perA': i[2], 'perB': i[4], 'perC': i[6], 'perD': i[8], 'perF': i[10], 'GPA': i[12] })
    return jsonify(math_308_list)
@app.route('/get-course/152')
def get_course_152():
    math_152_list = []
    for i in chunks_152:
        if("COURSE" in i[0]):
            break
        math_152_list.append({"course": i[0], 'professor': i[13], 'perA': i[2], 'perB': i[4], 'perC': i[6], 'perD': i[8], 'perF': i[10], 'GPA': i[12] })
    return jsonify(math_152_list)

if __name__ == "__main__":
    app.run(debug = True)