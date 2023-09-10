from flask import Flask, jsonify, request
import requests
import fitz  # PyMuPDF
from math import *
import numpy as np
import json

app = Flask(__name__)


    

# Define the URL of the PDF file
pdf_url = "https://web-as.tamu.edu/GradeReports/PDFReports/20231/grd20231AT.pdf"


# Function to extract text from the PDF URL
def extract_text_from_pdf(pdf_url):
    response = requests.get(pdf_url, stream=True)
    with fitz.open("pdf", response.content) as doc:
        pdf_text = ""
        for page in doc:
            pdf_text += page.get_text()
    return pdf_text

# Function to collect data between "CHEM-107" and "CHEM-117"
def collect_data_between_107_and_117(pdf_text):
    data_collected = False
    collected_data = []
    for line in pdf_text.split("\n"):
        if "CHEM-107" in line:
            data_collected = True
        elif "CHEM-117" in line:
            data_collected = False
            break

        if data_collected:
            collected_data.append(line)

    return collected_data

# Function to collect data between "CHEM-117" and "CHEM-119"
def collect_data_between_117_and_119(pdf_text):
    data_collected1 = False
    collected_data1 = []
    for line in pdf_text.split("\n"):
        if "CHEM-117" in line:
            data_collected1 = True
        elif "CHEM-119" in line:
            data_collected1 = False
            break

        if data_collected1:
            collected_data1.append(line)

    return collected_data1

# Function to collect data between "CHEM-119" and "CHEM-120"
def collect_data_between_119_and_120(pdf_text):
    data_collected2 = False
    collected_data2 = []
    for line in pdf_text.split("\n"):
        if "CHEM-119" in line:
            data_collected2 = True
        elif "CHEM-120" in line:
            data_collected2 = False
            break

        if data_collected2:
            collected_data2.append(line)

    return collected_data2

# Function to collect data between "CHEM-120" and "CHEM-222"
def collect_data_between_120_and_222(pdf_text):
    data_collected3 = False
    collected_data3 = []
    for line in pdf_text.split("\n"):
        if "CHEM-120" in line:
            data_collected3 = True
        elif "CHEM-222" in line:
            data_collected3 = False
            break

        if data_collected3:
            collected_data3.append(line)

    return collected_data3

# Function to collect data between "PHYS-206" and "PHYS-207"
def collect_data_between_206_and_207(pdf_text):
    data_collected4 = False
    collected_data4 = []
    for line in pdf_text.split("\n"):
        if "PHYS-206" in line:
            data_collected4 = True
        elif "PHYS-207" in line:
            data_collected4 = False
            break

        if data_collected4:
            collected_data4.append(line)

    return collected_data4

# Function to collect data between "PHYS-207" and "PHYS-216"
def collect_data_between_207_and_216(pdf_text):
    data_collected5 = False
    collected_data5 = []
    for line in pdf_text.split("\n"):
        if "PHYS-207" in line:
            data_collected5 = True
        elif "PHYS-216" in line:
            data_collected5 = False
            break

        if data_collected5:
            collected_data5.append(line)

    return collected_data5

# Function to collect data between "PHYS-216" and "PHYS-217"
def collect_data_between_216_and_217(pdf_text):
    data_collected6 = False
    collected_data6 = []
    for line in pdf_text.split("\n"):
        if "PHYS-216" in line:
            data_collected6 = True
        elif "PHYS-217" in line:
            data_collected6 = False
            break

        if data_collected6:
            collected_data6.append(line)

    return collected_data6

# Function to collect data between "MATH-150" and "MATH-151"
def collect_data_between_150_and_151(pdf_text):
    data_collected7 = False
    collected_data7 = []
    for line in pdf_text.split("\n"):
        if "MATH-150" in line:
            data_collected7 = True
        elif "MATH-151" in line:
            data_collected7 = False
            break

        if data_collected7:
            collected_data7.append(line)

    return collected_data7

# Function to collect data between "MATH-151" and "MATH-152"
def collect_data_between_151_and_152(pdf_text):
    data_collected8 = False
    collected_data8 = []
    for line in pdf_text.split("\n"):
        if "MATH-151" in line:
            data_collected8 = True
        elif "MATH-152" in line:
            data_collected8 = False
            break

        if data_collected8:
            collected_data8.append(line)

    return collected_data8

# Function to collect data between "MATH-152" and "MATH-167"
def collect_data_between_152_and_167(pdf_text):
    data_collected9 = False
    collected_data9 = []
    for line in pdf_text.split("\n"):
        if "MATH-152" in line:
            data_collected9 = True
        elif "MATH-167" in line:
            data_collected9 = False
            break

        if data_collected9:
            collected_data9.append(line)

    return collected_data9

# Function to collect data between "MATH-251" and "MATH-285"
def collect_data_between_251_and_285(pdf_text):
    data_collected10 = False
    collected_data10 = []
    for line in pdf_text.split("\n"):
        if "MATH-251" in line:
            data_collected10 = True
        elif "MATH-285" in line:
            data_collected10 = False
            break

        if data_collected10:
            collected_data10.append(line)

    return collected_data10

######

# Main program
if __name__ == "__main__":
    pass


# Sample data for demonstration
data = {'message': 'Hello from the backend!'}
chunks_107 = None 
chunks_117 = None 
chunks_119 = None 
chunks_120 = None 
chunks_206 = None
chunks_207 = None
chunks_216 = None
chunks_150 = None
chunks_151 = None
chunks_152 = None
chunks_251 = None
 
#API for CHEM-107
@app.route('/api/data-chunks-107', methods=['GET'])
def get_data_chunks_107():
    return json.dumps(dict_107)

#API for CHEM-117
@app.route('/api/data-chunks-117', methods=['GET'])
def get_data_chunks_117():
    return json.dumps(dict_117)

#API for CHEM-119
@app.route('/api/data-chunks-119', methods=['GET'])
def get_data_chunks_119():
    return json.dumps(dict_119)

#API for CHEM-120
@app.route('/api/data-chunks-120', methods=['GET'])
def get_data_chunks_120():
    return json.dumps(dict_120)

#API for PHYS-206
@app.route('/api/data-chunks-206', methods=['GET'])
def get_data_chunks_206():
    return json.dumps(dict_206)

#API for PHYS-207
@app.route('/api/data-chunks-207', methods=['GET'])
def get_data_chunks_207():
    return json.dumps(dict_207)

#API for PHYS-216
@app.route('/api/data-chunks-216', methods=['GET'])
def get_data_chunks_216():
    return json.dumps(dict_216)

#API for MATH-150
@app.route('/api/data-chunks-150', methods=['GET'])
def get_data_chunks_150():
    return json.dumps(dict_150)

#API for MATH-151
@app.route('/api/data-chunks-151', methods=['GET'])
def get_data_chunks_151():
    return json.dumps(dict_151)

#API for MATH-152
@app.route('/api/data-chunks-152', methods=['GET'])
def get_data_chunks_152():
    return json.dumps(dict_152)

#API for MATH-251
@app.route('/api/data-chunks-251', methods=['GET'])
def get_data_chunks_251():
    return json.dumps(dict_251)



if __name__ == '__main__':
    pdf_text = extract_text_from_pdf(pdf_url)

                                          #107
    chem_107_to_117_data = collect_data_between_107_and_117(pdf_text)

    # Print the collected data
    lines_107 = [line.strip() for line in chem_107_to_117_data]
    chunks_107 = [lines_107[x:x + 15] for x in range(0, len(lines_107), 15)]
    chunks_107 = chunks_107[:-1]

    print(chunks_107)

    prof_107 = np.array([])
    course_107 = np.array([])
    a_107 = np.array([])
    b_107 = np.array([])
    c_107 = np.array([])
    d_107  = np.array([])
    f_107 = np.array([])
    agpa_107 = np.array([])

    prof_107 = prof_107.tolist()
    course_107 = course_107.tolist()
    a_107 = a_107.tolist()
    b_107 = b_107.tolist()
    c_107 = c_107.tolist()
    d_107  = d_107.tolist()
    f_107 = f_107.tolist()
    agpa_107 = agpa_107.tolist()
    
    i = -1
    dict_107 = {
                 "Professor": [],
                 "Course_Code": [], 
                 "A%": [], 
                 "B%": [],
                 "C%": [],
                 "D%": [],
                 "F%": [],
                 "AGPA": []
            }
    
    while i <= len(chunks_107):
        i = i + 1
        if "%" in str(chunks_107[i][2]) :
            dict_107['Professor'].append(chunks_107[i][14])
            dict_107['Course_Code'].append(chunks_107[i][0])
            dict_107['A%'].append(chunks_107[i][2])
            dict_107['B%'].append(chunks_107[i][4])
            dict_107['C%'].append(chunks_107[i][6])
            dict_107['D%'].append(chunks_107[i][8])
            dict_107['F%'].append(chunks_107[i][10])
            dict_107['AGPA'].append(chunks_107[i][12])
            
        print(dict_107)

        if i == (len(chunks_107)-1):
            break

                             #117
                                        
    chem_117_to_119_data = collect_data_between_117_and_119(pdf_text)


    # Print the collected data
    lines_117 = [line.strip() for line in chem_117_to_119_data]
    chunks_117 = [lines_117[x:x + 15] for x in range(0, len(lines_117), 15)]
    chunks_117 = chunks_117[:-1]   

    prof_117 = np.array([])
    course_117 = np.array([])
    a_117 = np.array([])
    b_117 = np.array([])
    c_117 = np.array([])
    d_117  = np.array([])
    f_117 = np.array([])
    agpa_117 = np.array([])

    prof_117 = prof_117.tolist()
    course_117 = course_117.tolist()
    a_117 = a_117.tolist()
    b_117 = b_117.tolist()
    c_117 = c_117.tolist()
    d_117  = d_117.tolist()
    f_117 = f_117.tolist()
    agpa_117 = agpa_117.tolist()
    
    i = -1
    dict_117 = {
                 "Professor": [],
                 "Course_Code": [], 
                 "A%": [], 
                 "B%": [],
                 "C%": [],
                 "D%": [],
                 "F%": [],
                 "AGPA": []
            }
    
    while i <= len(chunks_117):
        i = i + 1
        if "%" in str(chunks_117[i][2]) :
            dict_117['Professor'].append(chunks_117[i][14])
            dict_117['Course_Code'].append(chunks_117[i][0])
            dict_117['A%'].append(chunks_117[i][2])
            dict_117['B%'].append(chunks_117[i][4])
            dict_117['C%'].append(chunks_117[i][6])
            dict_117['D%'].append(chunks_117[i][8])
            dict_117['F%'].append(chunks_117[i][10])
            dict_117['AGPA'].append(chunks_117[i][12])
            
            print(dict_117)

        if i == (len(chunks_117)-1):
            break

     




                    #Chem 119

        chem_119_to_120_data = collect_data_between_119_and_120(pdf_text)

# Print the collected data
    lines_119 = [line.strip() for line in chem_119_to_120_data]
    chunks_119 = [lines_119[x:x + 15] for x in range(0, len(lines_119), 15)]
    chunks_119 = chunks_119[:-1]     

    prof_119 = np.array([])
    course_119 = np.array([])
    a_119 = np.array([])
    b_119 = np.array([])
    c_119 = np.array([])
    d_119  = np.array([])
    f_119 = np.array([])
    agpa_119 = np.array([])

    prof_119 = prof_119.tolist()
    course_119 = course_119.tolist()
    a_119= a_119.tolist()
    b_119 = b_119.tolist()
    c_119 = c_119.tolist()
    d_119  = d_119.tolist()
    f_119 = f_119.tolist()
    agpa_119 = agpa_119.tolist()
    
    i = -1
    dict_119 = {   "Professor": [],
                 "Course_Code": [], 
                 "A%": [], 
                 "B%": [],
                 "C%": [],
                 "D%": [],
                 "F%": [],
                 "AGPA": []
            }
    
    while i <= len(chunks_119):
        i = i + 1
        if "%" in str(chunks_119[i][2]) :
            dict_119['Professor'].append(chunks_119[i][14])
            dict_119['Course_Code'].append(chunks_119[i][0])
            dict_119['A%'].append(chunks_119[i][2])
            dict_119['B%'].append(chunks_119[i][4])
            dict_119['C%'].append(chunks_119[i][6])
            dict_119['D%'].append(chunks_119[i][8])
            dict_119['F%'].append(chunks_119[i][10])
            dict_119['AGPA'].append(chunks_119[i][12])
            
            print(dict_119)

        if i == (len(chunks_119)-1):
            break
    
    
    

    
                        #Chem 120
    chem_120_to_222_data = collect_data_between_120_and_222(pdf_text)

# Print the collected data
    lines_120 = [line.strip() for line in chem_120_to_222_data]
    chunks_120 = [lines_120[x:x + 15] for x in range(0, len(lines_120), 15)]
    chunks_120 = chunks_120[:-1]     

    prof_120 = np.array([])
    course_120 = np.array([])
    a_120 = np.array([])
    b_120 = np.array([])
    c_120 = np.array([])
    d_120  = np.array([])
    f_120 = np.array([])
    agpa_120 = np.array([])

    prof_120 = prof_120.tolist()
    course_120 = course_120.tolist()
    a_120= a_120.tolist()
    b_120 = b_120.tolist()
    c_120 = c_120.tolist()
    d_120  = d_120.tolist()
    f_120 = f_120.tolist()
    agpa_120 = agpa_120.tolist()
    
    i = -1
    dict_120 = {   "Professor": [],
                 "Course_Code": [], 
                 "A%": [], 
                 "B%": [],
                 "C%": [],
                 "D%": [],
                 "F%": [],
                 "AGPA": []
            }
    
    while i <= len(chunks_120):
        i = i + 1
        if "%" in str(chunks_120[i][2]) :
            dict_120['Professor'].append(chunks_120[i][14])
            dict_120['Course_Code'].append(chunks_120[i][0])
            dict_120['A%'].append(chunks_120[i][2])
            dict_120['B%'].append(chunks_120[i][4])
            dict_120['C%'].append(chunks_120[i][6])
            dict_120['D%'].append(chunks_120[i][8])
            dict_120['F%'].append(chunks_120[i][10])
            dict_120['AGPA'].append(chunks_120[i][12])
            
            print(dict_120)

        if i == (len(chunks_120)-1):
            break


                #Physics 206
    phys_206_to_207_data = collect_data_between_206_and_207(pdf_text)


# Print the collected data
    lines_206 = [line.strip() for line in phys_206_to_207_data]
    chunks_206 = [lines_206[x:x + 15] for x in range(0, len(lines_206), 15)]
    chunks_206 = chunks_206[:-1]     

    prof_206 = np.array([])
    course_206 = np.array([])
    a_206 = np.array([])
    b_206 = np.array([])
    c_206 = np.array([])
    d_206  = np.array([])
    f_206 = np.array([])
    agpa_206 = np.array([])

    prof_206 = prof_206.tolist()
    course_206= course_206.tolist()
    a_206= a_206.tolist()
    b_206= b_206.tolist()
    c_206 = c_206.tolist()
    d_206  = d_206.tolist()
    f_120 = f_206.tolist()
    agpa_120 = agpa_206.tolist()
    
    i = -1
    dict_206 = {   "Professor": [],
                 "Course_Code": [], 
                 "A%": [], 
                 "B%": [],
                 "C%": [],
                 "D%": [],
                 "F%": [],
                 "AGPA": []
            }
    
    while i <= len(chunks_206):
        i = i + 1
        if "%" in str(chunks_206[i][2]) :
            dict_206['Professor'].append(chunks_206[i][14])
            dict_206['Course_Code'].append(chunks_206[i][0])
            dict_206['A%'].append(chunks_206[i][2])
            dict_206['B%'].append(chunks_206[i][4])
            dict_206['C%'].append(chunks_206[i][6])
            dict_206['D%'].append(chunks_206[i][8])
            dict_206['F%'].append(chunks_206[i][10])
            dict_206['AGPA'].append(chunks_206[i][12])
            
            print(dict_206)

        if i == (len(chunks_206)-1):
            break


                #Physics 207
    phys_207_to_216_data = collect_data_between_207_and_216(pdf_text)


# Print the collected data
    lines_207 = [line.strip() for line in phys_207_to_216_data]
    chunks_207 = [lines_207[x:x + 15] for x in range(0, len(lines_207), 15)]
    chunks_207 = chunks_207[:-1]     

    print(chunks_207)

    i = -1
    while i <= len(chunks_207):
        i = i + 1
        dict_216 = {
            "lists": chunks_207[i]
        }
        if i == (len(chunks_207)-1):
            break
        
    
    phys_216_to_217_data = collect_data_between_216_and_217(pdf_text)


# Print the collected data
    lines_216 = [line.strip() for line in phys_216_to_217_data]
    chunks_216 = [lines_216[x:x + 15] for x in range(0, len(lines_216), 15)]
    chunks_216 = chunks_216[:-1]     

    print(chunks_216)

    i = -1
    while i <= len(chunks_216):
        i = i + 1
        dict_216 = {
            "lists": chunks_216[i]
        }
        if i == (len(chunks_216)-1):
            break

    math_150_to_151_data = collect_data_between_150_and_151(pdf_text)

# Print the collected data
    lines_150 = [line.strip() for line in math_150_to_151_data]
    chunks_150 = [lines_150[x:x + 15] for x in range(0, len(lines_150), 15)]
    chunks_150 = chunks_150[:-1]     

    print(chunks_150)

    i = -1
    while i <= len(chunks_150):
        i = i + 1
        dict_150 = {
            "lists": chunks_150[i]
        }
        if i == (len(chunks_150)-1):
            break

    math_151_to_152_data = collect_data_between_151_and_152(pdf_text)


# Print the collected data
    lines_151 = [line.strip() for line in math_151_to_152_data]
    chunks_151 = [lines_151[x:x + 15] for x in range(0, len(lines_151), 15)]
    chunks_151 = chunks_151[:-1]     

    print(chunks_151)

    i = -1
    while i <= len(chunks_151):
        i = i + 1
        dict_151 = {
            "lists": chunks_151[i]
        }
        if i == (len(chunks_151)-1):
            break

    math_152_to_167_data = collect_data_between_152_and_167(pdf_text)


# Print the collected data
    lines_152 = [line.strip() for line in math_152_to_167_data]
    chunks_152 = [lines_152[x:x + 15] for x in range(0, len(lines_152), 15)]
    chunks_152 = chunks_152[:-1]     

    print(chunks_152)

    i = -1
    while i <= len(chunks_152):
        i = i + 1
        dict_152 = {
            "lists": chunks_152[i]
        }
        if i == (len(chunks_152)-1):
            break

    math_251_to_285_data = collect_data_between_251_and_285(pdf_text)


# Print the collected data
    lines_251 = [line.strip() for line in math_251_to_285_data]
    chunks_251 = [lines_251[x:x + 15] for x in range(0, len(lines_251), 15)]
    chunks_251 = chunks_251[:-1]     

    print(chunks_251)

    i = -1
    while i <= len(chunks_251):
        i = i + 1
        dict_251 = {
            "lists": chunks_251[i]
        }
        if i == (len(chunks_251)-1):
            break

    app.run(debug=True)
