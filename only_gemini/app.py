import os
from flask import Flask, request, render_template, jsonify

#function written in main.py for getting response from gemini
from gemini import get_response


# Initialize the Flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    
    # Generate a response using Google Gemini
    response = get_response(user_input)

    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
