from collections import defaultdict


def print_postings_list(postings):
    for term, docs in postings.items():
        print(f"Term: '{term}' \tDocument IDs: {docs}")


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

print_postings_list(basic_postings)
