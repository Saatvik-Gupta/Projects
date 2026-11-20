import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

with open("input.txt", "r") as file:
    text = file.read()

# Tokenize the text into words
words = word_tokenize(text)

# Get English stopwords
stop_words = set(stopwords.words('english'))

filtered_words = list()

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

filtered_text = " ".join(filtered_words)

print("Original Text:")
print(text)

print("\nText after removing stopwords:")
print(filtered_text)

with open("output.txt", "w") as file:
    file.write(filtered_text)