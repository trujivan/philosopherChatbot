from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

philosophers = {
    "Seneca": "Seneca was a Roman Stoic philosopher. Please answer this question as Seneca would.",
    "Aristotle": "Aristotle was a Greek philosopher and polymath. Please answer this question as Aristotle would.",
    "Plato": "Plato was a student of Socrates and a teacher of Aristotle. Please answer this question as Plato would.",
    "Socrates": "Socrates was a classical Greek philosopher credited as one of the founders of Western philosophy. Please answer this question as Socrates would.",
    "Nietzsche": "Nietzsche was a German philosopher, cultural critic, and philologist. Please answer this question as Nietzsche would."
}

def get_philosopher_response(philosopher, question):
    prompt = f"{philosophers[philosopher]} {question}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    philosopher = data['philosopher']
    question = data['question']
    answer = get_philosopher_response(philosopher, question)
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True)
