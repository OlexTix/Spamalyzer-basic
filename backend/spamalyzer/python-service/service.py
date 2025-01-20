# service.py
import os
import re
import sys
import pickle
import nltk
from flask import Flask, request, jsonify
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

app = Flask(__name__)
MODEL = None

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text

@app.route('/classify', methods=['POST'])
def classify_endpoint():
    """
    Oczekuje JSON:
    {
      "emailText": "Hello..."
    }
    Zwraca JSON:
    {
      "prediction": "Spam" albo "Brak spamu"
    }
    """
    data = request.get_json()
    if not data or 'emailText' not in data:
        return jsonify({"error": "emailText is required"}), 400

    email_text = data['emailText']
    email_text = preprocess_text(email_text)

    global MODEL
    if MODEL is None:
        return jsonify({"error": "Model not loaded"}), 500

    prediction = MODEL.predict([email_text])[0]
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    
    model_path = os.path.join(os.path.dirname(__file__), 'spam_classifier.pkl')
    if not os.path.exists(model_path):
        print(f"Model file not found at {model_path}")
        sys.exit(1)

    with open(model_path, 'rb') as f:
        MODEL = pickle.load(f)
        print("Model loaded!")

    app.run(host='0.0.0.0', port=9243, debug=True)
