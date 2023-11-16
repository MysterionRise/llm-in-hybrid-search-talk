import math
from collections import defaultdict

# Example tokenized documents
docs = {
    1: ["apple", "banana", "apple"],
    2: ["banana", "orange"],
    3: ["apple", "orange", "orange", "banana"],
}

# Create postings lists with term frequencies
tf_postings = defaultdict(lambda: defaultdict(int))
for doc_id, tokens in docs.items():
    for token in tokens:
        tf_postings[token][doc_id] += 1


# Function to print postings list in a formatted way
def print_postings_list(postings):
    for term, docs in postings.items():
        print(f"Term: '{term}'")
        for doc_id, freq in docs.items():
            print(f"\tDocument ID: {doc_id}, Frequency: {freq}")
        print()


print_postings_list(tf_postings)


# Function to calculate TF-IDF score for a term in a document
def tf_idf(term, doc_id, postings, total_docs):
    tf = postings[term][doc_id]
    idf = math.log(total_docs / len(postings[term]))
    return tf * idf


# Calculate TF-IDF score for 'apple' in document 1
score = tf_idf("apple", 1, tf_postings, len(docs))
print(f"TF-IDF score for 'apple' in document 1: {score}")
