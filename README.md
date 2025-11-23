# 🎓 LLM-Powered Educational Q&A: Machine Learning Fundamentals

This project is a **RAG (Retrieval-Augmented Generation)** application designed to act as an intelligent tutor for **Machine Learning Fundamentals**.

It serves as an interactive study assistant for students and job seekers, answering technical questions ranging from basic algorithms to advanced **Deep Learning** and **NLP** concepts. It uses **Google Gemini 2.0/1.5** as the reasoning engine and **FAISS** as the vector database to retrieve accurate, verified answers from a curated technical knowledge base.

## 🚀 Features
- **Domain-Specific Knowledge:** Specialized in Machine Learning, Deep Learning, NLP, and Interview Preparation questions.
- **RAG Architecture:** Retrieves context from a structured knowledge base to ensure technical accuracy and zero hallucinations.
- **Vector Search:** Uses HuggingFace embeddings (`all-MiniLM-L6-v2`) and FAISS for semantic similarity search.
- **Google Gemini Integration:** Leverages the latest Gemini models for high-quality, natural language explanations.
- **Streamlit UI:** A clean, user-friendly web interface for real-time interaction.

## 🛠️ Tech Stack
- **Language:** Python
- **LLM:** Google Gemini 2.0 Flash / 1.5 Pro
- **Framework:** LangChain
- **Vector DB:** FAISS (Facebook AI Similarity Search)
- **Embeddings:** HuggingFace
- **Frontend:** Streamlit

## 📂 Project Structure

├── main.py # The main application script
├── data.csv # The knowledge base (ML & DL Interview Questions)
├── requirements.txt # Python dependencies
├── .env # API keys (Not included in repo)
└── README.md # Documentation
