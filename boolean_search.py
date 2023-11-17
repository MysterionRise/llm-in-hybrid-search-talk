from collections import defaultdict

# Example tokenized documents
docs = {
    1: ["apple", "banana"],
    2: ["banana", "orange"],
    3: ["apple", "orange", "banana"],
}

# Create basic postings lists
basic_postings = defaultdict(set)
for doc_id, tokens in docs.items():
    for token in tokens:
        basic_postings[token].add(doc_id)


# Function to perform Boolean AND search
def boolean_and_search(term1, term2, postings):
    # Retrieve the set of documents for each term
    docs_term1 = postings.get(term1, set())
    docs_term2 = postings.get(term2, set())

    # Find the intersection (AND operation) of the two sets
    return docs_term1.intersection(docs_term2)


# Perform a search for documents that contain both "apple" and "banana"
matching_docs = boolean_and_search("apple", "banana", basic_postings)
print(f"Documents containing both 'apple' and 'banana': {matching_docs}")
