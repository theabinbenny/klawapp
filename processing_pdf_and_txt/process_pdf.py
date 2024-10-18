import pdfplumber

#function to print contents of pdf files
def read_pdf_file(pdf_filename):

    with pdfplumber.open(pdf_filename) as pdf:
        text_data = ''
        for page in pdf.pages:
            text_data += page.extract_text()
    print(text_data)

#function to find images in a pdf page

def find_images(pdf_filename):

    print("find_images")

#sample usage
read_pdf_file("processing_pdf_and_txt/files/sample.pdf")