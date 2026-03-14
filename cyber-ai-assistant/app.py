import streamlit as st
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Cybersecurity Knowledge Assistant",
    page_icon="🔐",
    layout="centered"
)

# -------------------------------
# Load Embedding Model
# -------------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

embed_model = load_model()

# -------------------------------
# Load Vector Knowledge Base
# -------------------------------
@st.cache_data
def load_vectors():
    with open("vectors.json") as f:
        return json.load(f)

data = load_vectors()
vectors = np.array([x["vector"] for x in data])

# -------------------------------
# Title
# -------------------------------
st.title("🔐 AI Cybersecurity Knowledge Assistant")
st.write(
    "Ask cybersecurity questions and retrieve relevant knowledge using **semantic vector search**."
)

# -------------------------------
# Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# User Input
# -------------------------------
query = st.chat_input("Ask a cybersecurity question...")

if query:

    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    # -------------------------------
    # Semantic Search
    # -------------------------------
    query_vec = embed_model.encode([query])

    similarity = np.dot(vectors, query_vec.T).flatten()

    top_indices = similarity.argsort()[-3:][::-1]

    # Build response
    response_text = "### Relevant Cybersecurity Knowledge\n\n"

    for i in top_indices:
        response_text += f"- {data[i]['text']}\n"

    response_text += "\n*Retrieved using semantic vector similarity search.*"

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response_text)

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": response_text}
    )
