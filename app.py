from flask import Flask, render_template, request, jsonify
import cohere

app = Flask(__name__)

co = cohere.Client("y3GazrLCXd6TfacRSUi2vXSBCa7ALJy5uvb3sNo3")  # Replace with your own API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('message', '').strip()

    if not user_input:
        return jsonify({'response': "I'm here to help. Please share what's on your mind."})

    response = co.chat(
        model='command-r',
        message=user_input,
        temperature=0.65,
        chat_history=[],
    )

    chatbot_response = response.text.strip()

    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
