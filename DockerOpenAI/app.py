import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return jsonify(response.choices[0].message.content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

