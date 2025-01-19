# train_model.py
import os
import re
import pickle
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.utils.class_weight import compute_class_weight

nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text

if __name__ == "__main__":
    
    csv_path = os.path.join(os.path.dirname(__file__), 'resources', 'spam_NLP.csv')
    df = pd.read_csv(csv_path)

    df = df.rename(columns={'CATEGORY': 'label', 'MESSAGE': 'text'})
    df['text'] = df['text'].apply(preprocess_text)
    df['label'] = df['label'].map({0: 'Brak spamu', 1: 'Spam'})
    df = df.dropna(subset=['label', 'text'])

    X = df['text']
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=42)

    class_weights = compute_class_weight(
        class_weight='balanced',
        classes=np.unique(y_train),
        y=y_train
    )

    pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 3))),
        ('classifier', MultinomialNB())
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print("Raport klasyfikacji:")
    print(classification_report(y_test, y_pred))

    model_path = os.path.join(os.path.dirname(__file__), 'spam_classifier.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(pipeline, f)

    print(f"Model wytrenowany i zapisany do {model_path}")
