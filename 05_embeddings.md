# Embeddings

Embeddings are numerical vector representations of text, images, or other data types. They transform words, sentences, or documents into lists of numbers (dense vectors) that capture meaning, context, and relationships between concepts. Similar items cluster close together in this high-dimensional space, while unrelated ones remain distant.

---

## Why Do We Need Embeddings?

Computers process numbers, not raw text, so embeddings bridge this gap by encoding:

- **Semantic meaning**: "king" relates closely to "queen" but far from "apple".
- **Context**: "bank" as finance vs. riverbank gets different vectors in contextual models.
- **Similarity**: Measures how alike two sentences or documents are.
- **Relationships**: Supports analogies like king - man + woman ≈ queen.

Embeddings power semantic search, recommendations, chatbots, RAG systems, and LLM reasoning.

---

## How Embeddings Work

Text passes through an embedding model (e.g., Word2Vec, BERT, OpenAI embeddings) to produce a dense vector like `[0.12, -0.54, 0.88, 0.31, ...]`. These live in high-dimensional space (256–3072 dimensions typically).

### Properties of Good Embeddings

- Similar meanings → vectors close in space (high cosine similarity).
- Opposite meanings → vectors far apart (low/negative similarity).
- Analogies → arithmetic works:  
  `vector("King") - vector("Man") + vector("Woman") ≈ vector("Queen")`.

---

## Types of Embeddings

### 1. Word Embeddings

- Fixed vector per word, regardless of context.
- Examples: Word2Vec, GloVe.
- Limitation: "bank" always gets the same vector.

### 2. Contextual Embeddings

- Vector varies by surrounding context.
- Examples: BERT, GPT, RoBERTa.
- Example sentences yielding different "bank" vectors:  
  - "He sat by the **bank** of the river."  
  - "She deposited money in the **bank**."

### 3. Sentence & Document Embeddings

- Single vector for entire sentences/paragraphs.
- Used for:  
  - Semantic search and similarity.  
  - Clustering documents.  
  - RAG (Retrieval-Augmented Generation).

---

## Measuring Embedding Similarity

**Cosine similarity** is standard:  
\[ \text{similarity} = \cos(\vec{A}, \vec{B}) = \frac{\vec{A} \cdot \vec{B}}{||\vec{A}|| \cdot ||\vec{B}||} \]  

- 1: identical.  
- 0: unrelated.  
- -1: opposite.


---

## Where Embeddings Are Used

### 1. Semantic Search

- Matches meaning, not keywords.  
- Query: "How to fix a slow laptop?"  
- Matches: "Tips to improve computer performance".

### 2. RAG (Retrieval-Augmented Generation)

- Embed query → find similar docs via vector search → feed to LLM for grounded answers.

### 3. Recommendations

- Suggest similar items (movies, products) by vector proximity.

### 4. Clustering & Categorization

- Group reviews, emails, or tickets automatically.

### 5. Fraud & Anomaly Detection

- Flag outliers (unusual transaction patterns).

---

## Visual Example of Embedding Space

Similar concepts naturally cluster:  
- Animals: dog, cat, tiger.  
- Royalty: king, queen, prince.  
- Emotions: happy, joyful, cheerful.  

Models learn these groupings from data patterns.

---

## Summary

Embeddings turn complex data into numerical vectors preserving meaning and relationships. They enable semantic search, RAG, recommendations, clustering, and modern NLP/LLM applications. Mastering embeddings is key to building intelligent AI systems.


