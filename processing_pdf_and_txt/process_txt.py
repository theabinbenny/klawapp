
def read_txt_file(txt_filename):
    # Reading text from a text file
    with open(txt_filename, 'r') as file:
        text_data = file.read()
    print(text_data)


#sample usage
read_txt_file("processing_pdf_and_txt/files/sample.txt")