import streamlit as st
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load stored vectors
with open("vectors.json") as f:
    data = json.load(f)

vectors = np.array([x["vector"] for x in data])

st.title("AI Cybersecurity Knowledge Assistant")

query = st.text_input("Ask a cybersecurity question")

if query:

    # Convert query to embedding
    query_vec = embed_model.encode([query])

    # Compute similarity
    similarity = np.dot(vectors, query_vec.T).flatten()

    # Retrieve top 3 documents
    top_indices = similarity.argsort()[-3:][::-1]

    st.subheader("Relevant Cybersecurity Knowledge")

    for i in top_indices:
        st.write(data[i]["text"])