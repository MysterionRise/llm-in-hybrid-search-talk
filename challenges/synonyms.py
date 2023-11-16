from collections import defaultdict

# Synonym dictionary
synonyms = {
    "bank": ["financial institution", "riverbank"],
    "river": ["watercourse"],
    "money": ["currency", "cash"],
}

# Example tokenized documents
docs = {
    1: ["financial institution", "savings", "loans"],
    2: ["riverbank", "watercourse", "fishing"],
    3: ["currency", "investment", "financial institution"],
}


# Function to expand terms with synonyms
def expand_with_synonyms(term, synonym_dict):
    expanded_terms = [term]
    if term in synonym_dict:
        expanded_terms.extend(synonym_dict[term])
    return expanded_terms


# Create postings lists with synonyms
postings = defaultdict(set)
for doc_id, tokens in docs.items():
    for token in tokens:
        for term in expand_with_synonyms(token, synonyms):
            postings[term].add(doc_id)


def print_postings_with_synonyms(postings_list, synonym_dict):
    for term, docs in postings_list.items():
        print(f"Term: '{term}'")
        if term in synonym_dict:
            synonyms_str = ", ".join(synonym_dict[term])
            print(f"\tSynonyms: [{synonyms_str}]")
        doc_ids_str = ", ".join(map(str, docs))
        print(f"\tDocuments: [{doc_ids_str}]")
        print()


print_postings_with_synonyms(postings, synonyms)


# Function to perform search with synonyms
def search_with_synonyms(query, postings_list, synonym_dict):
    expanded_query = expand_with_synonyms(query, synonym_dict)
    matching_docs = set()
    for term in expanded_query:
        matching_docs.update(postings_list.get(term, set()))
    return matching_docs


# Search for "bank"
search_results = search_with_synonyms("bank", postings, synonyms)
print(f"Documents related to 'bank': {search_results}")
