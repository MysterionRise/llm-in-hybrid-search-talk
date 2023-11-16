import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download("punkt")


def nltk_tokenize(text):
    # Tokenize text using NLTK
    tokens = word_tokenize(text)
    return tokens


# Example usage
text = (
    "NLTK's tokenizer is more advanced: It handles punctuation, for instance."
)
tokens = nltk_tokenize(text)
print(f"Input text: {text}")
print("")
print(f"Tokens: {tokens}")
