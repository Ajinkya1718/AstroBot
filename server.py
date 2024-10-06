
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from llm import chat_with_llm

app = Flask(__name__,static_folder='templates/static')
CORS(app)  # Enable CORS for all routes


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data.get('message')
    
    response = chat_with_llm(user_input)
    return jsonify({'response': response})






if __name__ == "__main__":
    app.run(debug=True)
