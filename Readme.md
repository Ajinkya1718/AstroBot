# AstroBot 🚀 : Space Trivia Chatbot

This is a space-themed chatbot that answers trivia questions related to space. The bot is built using HTML, JavaScript for the front end, and Python for the backend (assumed to be using Flask). The chatbot interacts with users, responding to questions about space in real-time. 🌌

## Features ✨

- Responsive user interface. 📱
- Handles user questions and responds via a Python backend. 💻
- Interactive conversation and real-time message handling. 🤖
  
## Prerequisites 📋

Make sure you have the following installed:

- Python 3.x 🐍
- Flask (or another Python web framework) 🌐
- Basic knowledge of HTML/CSS/JS 📄

## Setup Instructions ⚙️

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/space-trivia-chatbot.git
cd space-trivia-chatbot
```

### 2. Install Dependencies

Create a virtual environment and install the necessary Python packages.

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Running the Server 🚀

Start the Flask server by running the `server.py` file.

```bash
python server.py
```

The Flask server will start, and you can access the chatbot by navigating to the following base URL in your browser:

```
http://127.0.0.1:5000/
```

### 4. Interacting with the Chatbot 💬

- Type any space-related question in the chat input field. ❓
- The bot will respond with trivia answers fetched from the backend. 🎉

## File Structure 🗂️

```bash
.
├── server.py               # Python backend server (Flask)
├── templates
│   └── index.html          # Main chatbot HTML page
└── README.md               # Project instructions (this file)
```