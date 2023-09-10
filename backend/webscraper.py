from flask import Flask, jsonify, request
import requests
import fitz  # PyMuPDF
from math import *

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

# @app.route("/api/load-data", methods=["GET"])
# def load_data():
#     pdf_text = extract_text_from_pdf(pdf_url)
#     chem_107_to_117_data = collect_data_between_107_and_117(pdf_text)

#     # Print the collected data
#     lines_107 = [line.strip() for line in chem_107_to_117_data]
#     global chunks_107
#     chunks_107 = [lines_107[x:x + 15] for x in range(0, len(lines), 15)]
#     chunks_107 = chunks_107[:-1]

#     print(chunks_107)

#     i = -1
#     while i <= len(chunks_107):
#         i = i + 1
#         print(f"The course code is: {chunks_107[i][0]}")
#         print(f"The professor is: {chunks_107[i][14]}")
#         print(f"The percentage of A's in her class is: {chunks_107[i][2]}")
#         print(f"The percentage of B's in her class is: {chunks_107[i][4]}")
#         print(f"The percentage of C's in her class is: {chunks_107[i][6]}")
#         print(f"The percentage of D's in her class is: {chunks_107[i][8]}")
#         print(f"The percentage of F's in her class is: {chunks_107[i][10]}")
#         print(f"The average GPA in her class is: {chunks_107[i][12]}")
#         if i == (len(chunks_107)-1):
#             break
#     #return "Data loaded! Hooray!"

#     chem_117_to_119_data = collect_data_between_117_and_119(pdf_text)


#     # Print the collected data
#     lines = [line.strip() for line in chem_117_to_119_data]
#     global chunks_117
#     chunks_117 = [lines[x:x + 15] for x in range(0, len(lines), 15)]
#     chunks_117 = chunks_117[:-1]     

#     print(chunks_117)

#     i = -1
#     while i <= len(chunks_117):
#         i = i + 1
#         print(f"The course code is: {chunks_117[i][0]}")
#         print(f"The professor is: {chunks_117[i][14]}")
#         print(f"The percentage of A's in her class is: {chunks_117[i][2]}")
#         print(f"The percentage of B's in her class is: {chunks_117[i][4]}")
#         print(f"The percentage of C's in her class is: {chunks_117[i][6]}")
#         print(f"The percentage of D's in her class is: {chunks_117[i][8]}")
#         print(f"The percentage of F's in her class is: {chunks_117[i][10]}")
#         print(f"The average GPA in her class is: {chunks_117[i][12]}")
#         if i == (len(chunks_117)-1):
#             break
#     return "Data loaded! Hooray!"
 
#API for CHEM-107
@app.route('/api/data-chunks-107', methods=['GET'])
def get_data_chunks_107():
    my_dict = {
        }
    return jsonify(chunks_107)

#API for CHEM-117
@app.route('/api/data-chunks-117', methods=['GET'])
def get_data_chunks_117():
    return jsonify(chunks_117)

#API for CHEM-119
@app.route('/api/data-chunks-119', methods=['GET'])
def get_data_chunks_119():
    return jsonify(chunks_119)

#API for CHEM-120
@app.route('/api/data-chunks-120', methods=['GET'])
def get_data_chunks_120():
    return jsonify(chunks_120)

#API for PHYS-206
@app.route('/api/data-chunks-206', methods=['GET'])
def get_data_chunks_206():
    return jsonify(chunks_206)

#API for PHYS-207
@app.route('/api/data-chunks-207', methods=['GET'])
def get_data_chunks_207():
    return jsonify(chunks_207)

#API for PHYS-216
@app.route('/api/data-chunks-216', methods=['GET'])
def get_data_chunks_216():
    return jsonify(chunks_216)

#API for MATH-150
@app.route('/api/data-chunks-150', methods=['GET'])
def get_data_chunks_150():
    return jsonify(chunks_150)

#API for MATH-151
@app.route('/api/data-chunks-151', methods=['GET'])
def get_data_chunks_151():
    return jsonify(chunks_151)

#API for MATH-152
@app.route('/api/data-chunks-152', methods=['GET'])
def get_data_chunks_152():
    return jsonify(chunks_152)

#API for MATH-251
@app.route('/api/data-chunks-251', methods=['GET'])
def get_data_chunks_251():
    return jsonify(chunks_251)



if __name__ == '__main__':
    pdf_text = extract_text_from_pdf(pdf_url)
    chem_107_to_117_data = collect_data_between_107_and_117(pdf_text)

    # Print the collected data
    lines_107 = [line.strip() for line in chem_107_to_117_data]
    chunks_107 = [lines_107[x:x + 15] for x in range(0, len(lines_107), 15)]
    chunks_107 = chunks_107[:-1]

    print(chunks_107)

    i = -1
    while i <= len(chunks_107):
        i = i + 1
        # print(f"The course code is: {chunks_107[i][0]}")
        # print(f"The professor is: {chunks_107[i][14]}")
        # print(f"The percentage of A's in her class is: {chunks_107[i][2]}")
        # print(f"The percentage of B's in her class is: {chunks_107[i][4]}")
        # print(f"The percentage of C's in her class is: {chunks_107[i][6]}")
        # print(f"The percentage of D's in her class is: {chunks_107[i][8]}")
        # print(f"The percentage of F's in her class is: {chunks_107[i][10]}")
        # print(f"The average GPA in her class is: {chunks_107[i][12]}")
        dict_107 = {
            # "course code": chunks_107[i][0],
            # "professor": chunks_107[i][14],
            # "a_percentage": chunks_107[i][2],
            # "b_percentage": chunks_107[i][4],
            # "c_percentage": chunks_107[i][6],
            # "d_percentage": chunks_107[i][8],
            # "f_percentage": chunks_107[i][10],
            # "average_GPA": chunks_107[i][12]
            "lists": chunks_107[i]
        }

        if i == (len(chunks_107)-1):
            break
    #return "Data loaded! Hooray!"

    chem_117_to_119_data = collect_data_between_117_and_119(pdf_text)


    # Print the collected data
    lines_117 = [line.strip() for line in chem_117_to_119_data]
    chunks_117 = [lines_117[x:x + 15] for x in range(0, len(lines_117), 15)]
    chunks_117 = chunks_117[:-1]     

    print(chunks_117)

    i = -1
    while i <= len(chunks_117):
        i = i + 1
        # print(f"The course code is: {chunks_117[i][0]}")
        # print(f"The professor is: {chunks_117[i][14]}")
        # print(f"The percentage of A's in her class is: {chunks_117[i][2]}")
        # print(f"The percentage of B's in her class is: {chunks_117[i][4]}")
        # print(f"The percentage of C's in her class is: {chunks_117[i][6]}")
        # print(f"The percentage of D's in her class is: {chunks_117[i][8]}")
        # print(f"The percentage of F's in her class is: {chunks_117[i][10]}")
        # print(f"The average GPA in her class is: {chunks_117[i][12]}")
        dict_117 = {
            # "course code": chunks_117[i][0],
            # "professor": chunks_117[i][14],
            # "a_percentage": chunks_117[i][2],
            # "b_percentage": chunks_117[i][4],
            # "c_percentage": chunks_117[i][6],
            # "d_percentage": chunks_117[i][8],
            # "f_percentage": chunks_117[i][10],
            # "average_GPA": chunks_117[i][12]
            "lists": chunks_117[i]
        }
        if i == (len(chunks_117)-1):
            break

    chem_119_to_120_data = collect_data_between_119_and_120(pdf_text)

# Print the collected data
    lines_119 = [line.strip() for line in chem_119_to_120_data]
    chunks_119 = [lines_119[x:x + 15] for x in range(0, len(lines_119), 15)]
    chunks_119 = chunks_119[:-1]     

    print(chunks_119)

    i = -1
    while i <= len(chunks_119):
        i = i + 1
        # print(f"The course code is: {chunks_119[i][0]}")
        # print(f"The professor is: {chunks_119[i][14]}")
        # print(f"The percentage of A's in her class is: {chunks_119[i][2]}")
        # print(f"The percentage of B's in her class is: {chunks_119[i][4]}")
        # print(f"The percentage of C's in her class is: {chunks_119[i][6]}")
        # print(f"The percentage of D's in her class is: {chunks_119[i][8]}")
        # print(f"The percentage of F's in her class is: {chunks_119[i][10]}")
        # print(f"The average GPA in her class is: {chunks_119[i][12]}")
        dict_117 = {
            # "course code": chunks_119[i][0],
            # "professor": chunks_119[i][14],
            # "a_percentage": chunks_119[i][2],
            # "b_percentage": chunks_119[i][4],
            # "c_percentage": chunks_119[i][6],
            # "d_percentage": chunks_119[i][8],
            # "f_percentage": chunks_119[i][10],
            # "average_GPA": chunks_119[i][12]
            "lists": chunks_119[i]
        }
        if i == (len(chunks_119)-1):
            break

    chem_120_to_222_data = collect_data_between_120_and_222(pdf_text)

# Print the collected data
    lines_120 = [line.strip() for line in chem_120_to_222_data]
    chunks_120 = [lines_120[x:x + 15] for x in range(0, len(lines_120), 15)]
    chunks_120 = chunks_120[:-1]     

    print(chunks_120)

    i = -1
    while i <= len(chunks_120):
        i = i + 1
        # print(f"The course code is: {chunks_120[i][0]}")
        # print(f"The professor is: {chunks_120[i][14]}")
        # print(f"The percentage of A's in her class is: {chunks_120[i][2]}")
        # print(f"The percentage of B's in her class is: {chunks_120[i][4]}")
        # print(f"The percentage of C's in her class is: {chunks_120[i][6]}")
        # print(f"The percentage of D's in her class is: {chunks_120[i][8]}")
        # print(f"The percentage of F's in her class is: {chunks_120[i][10]}")
        # print(f"The average GPA in her class is: {chunks_120[i][12]}")
        dict_120 = {
            # "course code": chunks_120[i][0],
            # "professor": chunks_120[i][14],
            # "a_percentage": chunks_120[i][2],
            # "b_percentage": chunks_120[i][4],
            # "c_percentage": chunks_120[i][6],
            # "d_percentage": chunks_120[i][8],
            # "f_percentage": chunks_120[i][10],
            # "average_GPA": chunks_120[i][12]
            "lists": chunks_120[i]
        }
        if i == (len(chunks_120)-1):
            break


    
    phys_206_to_207_data = collect_data_between_206_and_207(pdf_text)


# Print the collected data
    lines_206 = [line.strip() for line in phys_206_to_207_data]
    chunks_206 = [lines_206[x:x + 15] for x in range(0, len(lines_206), 15)]
    chunks_206 = chunks_206[:-1]     

    print(chunks_206)

    i = -1
    while i <= len(chunks_206):
        i = i + 1
        dict_206 = {
            "lists": chunks_206[i]
        }
        if i == (len(chunks_206)-1):
            break


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
