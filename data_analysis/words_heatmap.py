import random
from collections import defaultdict

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import typo
from sentence_transformers import SentenceTransformer, util


def get_model(model_name: str):
    return SentenceTransformer(model_name)


models = [
    "sentence-transformers/multi-qa-mpnet-base-dot-v1",
    "thenlper/gte-base",
    "BAAI/bge-base-en-v1.5",
    "intfloat/e5-base-v2",
]

words = [
    "thrombosis",
    "pregnancy",
    "symptoms",
    "hematology",
    "patient",
    "chronic",
    "fatigue",
    "treatment",
    "therapy",
    "diagnosis",
    "transfusions",
    "biomarkers",
    "epidemiology",
]

misspelled_words = {}

for word in words:
    error = typo.StrErrer(word, seed=2)
    misspelled_words[word] = random.choice(
        [
            error.nearby_char().result,
        ]
    )

print(misspelled_words)

results = defaultdict(lambda: defaultdict(dict))

for model_name in models:
    model = get_model(model_name)
    for word in misspelled_words:
        mis_word = misspelled_words[word]
        score = round(
            util.cos_sim(model.encode(word), model.encode(mis_word)).item(), 2
        )
        results[model_name][word + ": " + mis_word] = score
results = dict(results)
for key in results:
    results[key] = dict(results[key])

figure = plt.gcf()

figure.set_size_inches(8, 6)
ax = sns.heatmap(pd.DataFrame.from_dict(results), annot=True)
ax.set_title("Why spelling still matters?")
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right")
plt.savefig("spelling_mistakes_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()
