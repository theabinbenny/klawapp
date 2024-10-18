from PIL import Image
import pytesseract


# Load an image from file
img = Image.open('processing_pdf_and_txt/files/sample_image_to_txt.jpg')

# Extract text from the image using pytesseract
text = pytesseract.image_to_string(img)

# Print the extracted text
print("Extracted Text:")
print(text)