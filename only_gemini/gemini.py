#print("klaw app successfully made")

#program that contains function to get responses from gemini

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")



"""

this function is responsible for sending the gemini response. 
the input parameter is the question itself. 
the output or the return is the response

"""

def get_response(user_input):

    response = model.generate_content(user_input)
    #print(response.text)

    return response