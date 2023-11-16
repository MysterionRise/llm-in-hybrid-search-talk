from collections import defaultdict

# Example tokenized documents
docs = {
    1: ["this", "is", "a", "sample"],
    2: ["this", "is", "another", "example", "sample"],
}

# Basic Postings Lists
basic_postings = defaultdict(set)
for doc_id, tokens in docs.items():
    for token in tokens:
        basic_postings[token].add(doc_id)

print("Basic Postings Lists:", dict(basic_postings))

# Postings Lists with Term Frequencies
tf_postings = defaultdict(lambda: defaultdict(int))
for doc_id, tokens in docs.items():
    for token in tokens:
        tf_postings[token][doc_id] += 1

print("Term Frequency Postings Lists:", dict(tf_postings))

# Positional Postings Lists
positional_postings = defaultdict(lambda: defaultdict(list))
for doc_id, tokens in docs.items():
    for pos, token in enumerate(tokens):
        positional_postings[token][doc_id].append(pos)

print("Positional Postings Lists:", dict(positional_postings))
