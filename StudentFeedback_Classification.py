# Student's Feedback Classification System

import nltk
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# python -m pip install scikit-learn
# To check--> python -c "from sklearn.feature_extraction.text import TfidfVectorizer; from sklearn.linear_model import LogisticRegression; from sklearn.pipeline import Pipeline; print('All libraries imported successfully!')"

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# Step 1: Load stopwords
stop_words = set(stopwords.words("english"))

# Keep negative words because they affect sentiment
stop_words.discard("not")
stop_words.discard("no")

# Step 2: Text preprocessing
def preprocess_text(text):

    # Convert text into lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-z\s]", " ", text)

    # Tokenization
    words = word_tokenize(text)

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    # Join words into a sentence
    return " ".join(words)

# Step 3: Create a small training dataset
feedback_data = [

    # Positive feedback
    "The teacher is excellent",
    "The teaching is very good",
    "The faculty is helpful",
    "I enjoy the lectures",
    "The classroom is comfortable",

    # Negative feedback
    "The teacher is terrible",
    "The teaching is very bad",
    "The faculty is unhelpful",
    "I hate the lectures",
    "The classroom is uncomfortable",

    # Neutral feedback
    "The lecture starts at ten",
    "The examination is on Monday",
    "The class has forty students",
    "The assignment is due Friday",
    "The course has five units"
]

# Step 4: Create sentiment labels
# labels =  ["Positive"] * 5 + ["Negative"] * 5 + ["Neutral"] * 5
labels = [
    "Positive", "Positive", "Positive", "Positive", "Positive",
    "Negative", "Negative", "Negative", "Negative", "Negative",
    "Neutral", "Neutral", "Neutral", "Neutral", "Neutral"
]

# Step 5: Preprocess training data
processed_feedback = [
    preprocess_text(text) for text in feedback_data
]

# Step 6: Create the ML pipeline
model = Pipeline([

    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),

    ("classifier", LogisticRegression(max_iter=1000))
])

# Step 7: Train the model
model.fit(processed_feedback, labels)

print("\n======================================")
print(" STUDENT FEEDBACK CLASSIFICATION SYSTEM")
print("======================================")

print("NLP preprocessing completed.")
print("Machine Learning model trained successfully!")

# Step 8: Function to analyze feedback
def analyze_feedback(feedback):

    # Preprocess user feedback
    processed_text = preprocess_text(feedback)

    if not processed_text.strip():
        print("Please enter meaningful text.")
        return

    # Predict sentiment
    prediction = model.predict([processed_text])[0]

    # Calculate prediction probabilities
    probabilities = model.predict_proba([processed_text])[0]

    confidence = max(probabilities) * 100

    # Display results
    print("\n---------- ANALYSIS RESULT ----------")

    print("Original Feedback:", feedback)

    print("Processed Feedback:", processed_text)

    print("Predicted Sentiment:", prediction)

    print(f"Model Confidence: {confidence:.2f}%")

    print("-------------------------------------")


# Step 9: Take input from the student
while True:

    feedback = input(
        "\nEnter student feedback (or type 'exit' to stop): "
    ).strip()

    if feedback.lower() == "exit":
        print("\nThank you for using the system!")
        break

    if not feedback:
        print("Feedback cannot be empty.")
        continue

    analyze_feedback(feedback)


