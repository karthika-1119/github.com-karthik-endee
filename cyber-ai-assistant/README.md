# AI Cybersecurity Knowledge Assistant

## Project Overview
The AI Cybersecurity Knowledge Assistant is an AI-powered application that helps users understand cybersecurity concepts by retrieving relevant knowledge using semantic vector search.

This project demonstrates how vector embeddings and semantic similarity search can be used to build an intelligent knowledge retrieval system.

Users can ask cybersecurity-related questions, and the system retrieves the most relevant information from a cybersecurity knowledge base.

This project was developed as part of the Endee AI/ML project evaluation.

---

## Key Features

- Semantic search for cybersecurity concepts
- Vector embedding based retrieval
- Retrieval-Augmented knowledge system
- Interactive web interface using Streamlit
- Lightweight and fully local AI pipeline

---

## System Architecture


User Query
↓
Sentence Transformer Embedding
↓
Vector Similarity Search
↓
Retrieve Top Cybersecurity Knowledge
↓
Display Answer in UI


---

## Tech Stack

- Python
- Streamlit
- Sentence Transformers
- NumPy
- Vector Similarity Search

---

## How the System Works

1. The user enters a cybersecurity question.
2. The query is converted into a vector embedding using the Sentence Transformer model.
3. The system compares the query vector with stored cybersecurity knowledge vectors.
4. The most relevant knowledge entries are retrieved based on similarity.
5. The retrieved knowledge is displayed to the user through a web interface.

---

## Use Case Demonstration

Example query:


What is phishing?


Example result:


Phishing is a social engineering attack where attackers trick users into revealing sensitive information such as passwords or financial data.


---

## Project Structure


cyber-ai-assistant
│
├── app.py
├── ingest.py
├── cybersecurity.txt
├── vectors.json
├── requirements.txt
└── README.md


---

## Setup Instructions

### 1 Clone the repository


git clone https://github.com/yourusername/your-repo-name.git


### 2 Navigate to project folder


cd cyber-ai-assistant


### 3 Install dependencies


pip install -r requirements.txt


### 4 Generate vector embeddings


python ingest.py


### 5 Run the application


python -m streamlit run app.py


---

## Future Improvements

- Integrate a vector database such as Endee
- Add large-scale cybersecurity datasets
- Implement LLM-based answer generation
- Build a conversational chat interface

---

## Author

Boya Karthik

LinkedIn: www.linkedin.com/in/boyakarthik

---

## License

This project is created for educational and research purposes.
