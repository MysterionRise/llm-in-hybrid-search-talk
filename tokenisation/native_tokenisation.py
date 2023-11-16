def simple_tokenize(text):
    # Lowercase the text for consistency
    text = text.lower()
    # Replace non-alphanumeric characters with spaces
    text = "".join(char if char.isalnum() else " " for char in text)
    # Split the text into tokens based on whitespace
    tokens = text.split()
    return tokens


# Example usage
text = "Example text: Tokenization is essential."
tokens = simple_tokenize(text)
print(tokens)
