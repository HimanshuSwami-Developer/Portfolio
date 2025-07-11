from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for local testing

# Load Gemini API key (use env or set directly here for demo)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask-gemini', methods=['POST'])
def ask_gemini():
    data = request.get_json()
    prompt = data.get('prompt', '')
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return jsonify({ 'reply': response.text })
    except Exception as e:
        print(e)
        return jsonify({ 'reply': 'Error communicating with Gemini.' }), 500

if __name__ == '__main__':
    app.run(debug=True)
