import spacy

# Don't forget to run python3 -m spacy download en_core_web_sm

# Load English tokenizer
nlp = spacy.load("en_core_web_sm")


def spacy_tokenize(text):
    # Process the text
    doc = nlp(text)
    # Extract tokens
    tokens = [token.text for token in doc]
    return tokens


# Example usage
text = "spaCy also handles complex cases like contractions, e.g., don't."
tokens = spacy_tokenize(text)
print(tokens)
