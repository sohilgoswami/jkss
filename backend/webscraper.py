import requests
import fitz  # PyMuPDF
from math import *

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

# Main program
if __name__ == "__main__":
    pdf_text = extract_text_from_pdf(pdf_url)
    chem_107_to_117_data = collect_data_between_107_and_117(pdf_text)

# Print the collected data
lines = [line.strip() for line in chem_107_to_117_data]
chunks = [lines[x:x + 15] for x in range(0, len(lines), 15)]
chunks = chunks[:-1]

print(chunks)

i = -1
while i <= len(chunks):
    i = i + 1
    print(f"The course code is: {chunks[i][0]}")
    print(f"The professor is: {chunks[i][14]}")
    print(f"The percentage of A's in her class is: {chunks[i][2]}")
    print(f"The percentage of B's in her class is: {chunks[i][4]}")
    print(f"The percentage of C's in her class is: {chunks[i][6]}")
    print(f"The percentage of D's in her class is: {chunks[i][8]}")
    print(f"The percentage of F's in her class is: {chunks[i][10]}")
    print(f"The average GPA in her class is: {chunks[i][12]}")
    if i == (len(chunks)-1):
        break






