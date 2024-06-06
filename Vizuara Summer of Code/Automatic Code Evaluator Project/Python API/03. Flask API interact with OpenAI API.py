from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'your_openai_api_key' with your actual OpenAI API key
OPENAI_API_KEY = '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'

# Function to call OpenAI's ChatGPT API
def call_openai_api(messages):
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',  # Using the ChatGPT model
        'messages': messages
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    return response.json()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if 'messages' not in data:
        return jsonify({'error': 'Messages are required'}), 400

    messages = data['messages']
    response = call_openai_api(messages)
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
