<img width="1031" height="564" alt="image" src="https://github.com/user-attachments/assets/f495ac5c-b6f3-4efb-91b1-70b381cd6dae" />


# Chatbot Architecture (RAG System)

This describes a **Retrieval-Augmented Generation (RAG)** chatbot that answers questions based on uploaded documents (PDFs). The system converts documents into searchable embeddings, retrieves relevant chunks for user queries, and generates grounded responses using an LLM.

---

## High-Level Architecture

User Query → Embedding → Vector Search → LLM Generation → Answer
↑ ↓
PDFs → Chunks → Embeddings → Vector Store ← Similarity Search

**Two phases**:
1. **Indexing** (offline): PDFs → chunks → embeddings → vector store
2. **Querying** (online): Query → embedding → retrieve → LLM answer
