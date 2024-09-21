# Philosopher Chatbot

This project is a chatbot that allows users to ask questions to famous philosophers and get their point of view using OpenAI's GPT models.

### Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/philosopher-chatbot.git
    cd philosopher-chatbot
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:
    - Create a `.env` file in the project root and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Open `http://127.0.0.1:5000/` in your web browser to use the chatbot.

### Deployment

To deploy this app to the web (e.g., using Heroku or any other PaaS), follow their instructions for deploying a Flask app.