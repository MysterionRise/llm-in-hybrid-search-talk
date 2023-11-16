from collections import defaultdict

docs = {
    1: ["apple", "banana", "apple"],
    2: ["banana", "orange"],
    3: ["apple", "orange", "orange", "banana"],
}

# Create positional postings lists
positional_postings = defaultdict(lambda: defaultdict(list))
for doc_id, tokens in docs.items():
    for pos, token in enumerate(tokens):
        positional_postings[token][doc_id].append(pos)


# Function to print postings list in a formatted way
def print_positional_postings_list(postings):
    for term, docs in postings.items():
        print(f"Term: '{term}'")
        for doc_id, positions in docs.items():
            positions_str = ", ".join(map(str, positions))
            print(f"\tDocument ID: {doc_id}, Positions: [{positions_str}]")
        print()


print_positional_postings_list(positional_postings)


# Function to find documents containing a specific phrase
def search_phrase(phrase, postings):
    phrase_tokens = phrase.split()
    candidate_docs = set(postings[phrase_tokens[0]].keys())

    for doc_id in candidate_docs:
        positions = [
            postings[token][doc_id]
            for token in phrase_tokens
            if doc_id in postings[token]
        ]
        if any(
            all(
                p + offset in pos_list
                for p, pos_list in zip(positions[0], positions[offset:])
            )
            for offset in range(1, len(positions))
        ):
            yield doc_id


# Search for the phrase "apple banana"
matching_docs = list(search_phrase("apple banana", positional_postings))
print(f"Documents with the phrase 'apple banana': {matching_docs}")
