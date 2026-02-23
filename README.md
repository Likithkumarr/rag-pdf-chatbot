# rag-pdf-chatbot
🔥 Project Description
This project implements a fully offline Retrieval-Augmented Generation (RAG) system that allows users to chat with PDF documents without using any paid APIs or cloud services.
The system loads a PDF file, splits it into chunks, converts the text into vector embeddings using HuggingFace models, stores them in ChromaDB, and retrieves relevant information to generate context-aware responses using a local LLM powered by Ollama.

🧠 Key Features
   📄 PDF Document Loader
   ✂ Text Chunking & Splitting
   🧠 Local HuggingFace Embeddings
   🗄 Chroma Vector Database
   🔎 Semantic Search & Retrieval
   🤖 Local LLM (Ollama - Llama3 / Phi / TinyLlama)
   💻 Fully Offline (No API Keys Required)
   💰 100% Free Setup

⚙️ Tech Stack
     Python
     LangChain (0.2.x architecture)
     ChromaDB
     HuggingFace Sentence Transformers
     Ollama (Local LLM)

🔄 How It Works
    PDF → Text Splitting → Embeddings → ChromaDB → Retriever → LLM → Answer

🎯 Use Cases
    Document Question Answering
    Resume Chatbot
    Research Paper Assistant
    Knowledge Base Chatbot
    Offline AI Applications
