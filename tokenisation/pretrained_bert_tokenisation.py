from transformers import BertTokenizer

bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
print(bert_tokenizer.tokenize("Everybody is an expert in LLMs now!🤗"))
