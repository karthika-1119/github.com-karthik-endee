from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("cybersecurity_data.txt") as f:
    docs = f.readlines()

embeddings = model.encode(docs)

data = []

for i, doc in enumerate(docs):
    data.append({
        "text": doc.strip(),
        "vector": embeddings[i].tolist()
    })

with open("vectors.json", "w") as f:
    json.dump(data, f)

print("Embeddings created successfully")
