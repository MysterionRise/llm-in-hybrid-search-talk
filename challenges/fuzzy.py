import Levenshtein as lev

# Example tokenized documents
docs = {
    1: ["apple", "banana", "citrus"],
    2: ["berry", "cherry", "date"],
    3: ["elderberry", "fig", "grape"],
}

# Create a basic postings list
postings = {}
for doc_id, tokens in docs.items():
    for token in tokens:
        postings.setdefault(token, set()).add(doc_id)


# Fuzzy matching function
def fuzzy_search(query, postings_list, max_distance=2):
    matching_docs = set()
    for term in postings_list.keys():
        if lev.distance(query, term) <= max_distance:
            matching_docs.update(postings_list[term])
    return matching_docs


# Query reformulation suggestion
def suggest_query_reformulation(query):
    suggestions = []
    # Basic implementation: suggesting AND/OR operators
    words = query.split()
    if len(words) > 1:
        suggestions.append(" AND ".join(words))
        suggestions.append(" OR ".join(words))
    return suggestions


# Test fuzzy search
# search_query = "appl"  # Intentional misspelling
search_query = "bamama"  # Intentional misspelling

fuzzy_results = fuzzy_search(search_query, postings)
print(f"Fuzzy search results for '{search_query}': {fuzzy_results}")

# Test query reformulation
query = "apple banana"
suggestions = suggest_query_reformulation(query)
print(f"Suggestions for reformulating '{query}': {suggestions}")
