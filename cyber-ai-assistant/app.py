import streamlit as st
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

genai.configure(api_key="Geminiapikey")

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

with open("vectors.json") as f:
    data = json.load(f)

vectors = np.array([x["vector"] for x in data])

st.title("AI Cybersecurity Knowledge Assistant")

query = st.text_input("Ask a cybersecurity question")

if query:

    query_vec = embed_model.encode([query])

    similarity = np.dot(vectors, query_vec.T).flatten()

    top_indices = similarity.argsort()[-3:][::-1]

    context = ""

    for i in top_indices:
        context += data[i]["text"] + "\n"

    prompt = f"""
    You are a cybersecurity assistant.

    Context:
    {context}

    Question:
    {query}

    Explain clearly.
    """

    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(prompt)

    st.write(response.text)



