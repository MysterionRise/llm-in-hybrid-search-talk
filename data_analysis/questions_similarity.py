import matplotlib.pyplot as plt
import seaborn as sns
from sentence_transformers import SentenceTransformer, util
from tqdm.auto import tqdm


def get_model(model_name: str):
    return SentenceTransformer(model_name)


models = [
    "sentence-transformers/multi-qa-mpnet-base-dot-v1",
    "thenlper/gte-base",
    "BAAI/bge-base-en-v1.5",
    "intfloat/e5-base-v2",
]

q1 = "123"
q2 = "234"

sns.set(rc={"figure.figsize": (11.7, 8.27)})

for model_name in tqdm(models):
    model = get_model(model_name)
    q1_emb = model.encode(q1)
    q2_emb = model.encode(q2)

    data = util.cos_sim(q1_emb, q2_emb)

    ax = sns.heatmap(data=data, annot=True)
    ax.collections[0].set_clim(0.1, 1)

    ax.set_ylabel("questions 1")
    ax.set_xlabel("questions 2")
    ax.set_title(f"Model: {model_name}")
    model_name = model_name.split("/")[-1]
    plt.savefig("questions_similarity_{model_name}.png")
    plt.show()
