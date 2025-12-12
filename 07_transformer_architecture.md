# Transformer Architecture

The Transformer is the foundational architecture behind modern Large Language Models (LLMs) like GPT, BERT, Claude, and Gemini. Introduced in the 2017 paper *"Attention Is All You Need"*, it revolutionized deep learning by enabling parallel processing and superior handling of long-range dependencies in text. Transformers replaced older sequence models like RNNs and LSTMs, achieving dramatically better performance on language tasks.

---

## Why Transformers?

**Pre-Transformer limitations**:
- RNNs processed text sequentially (one token at a time) → slow training.
- LSTMs struggled with long sentences → lost distant context (vanishing gradients).
- Difficult to parallelize across GPUs → expensive to scale.

**Transformer advantages**:
- Self-attention processes **all tokens simultaneously**.
- Captures relationships across arbitrary distances.
- Highly parallelizable → scales to billions of parameters.

---

## High-Level Transformer Structure

A Transformer consists of two main components (used independently or together):

### 1. Encoder
- Processes input text into rich representations.
- Used in bidirectional models like BERT.
- Stack of identical encoder layers.

### 2. Decoder  
- Generates output tokens autoregressively.
- Used in generative models like GPT.
- Stack of identical decoder layers.

### Encoder-Decoder (Combined)
- Used in sequence-to-sequence tasks like translation.
- Decoder attends to encoder outputs via cross-attention.

---

## Core Components

### 1. Self-Attention Mechanism
**The heart of Transformers**. For each token, computes:

```
Query (Q), Key (K), Value (V) matrices
Attention(Q, K, V) = softmax(Q · Kᵀ / √dₖ) · V
```

**Intuition**: Each token "queries" all others to determine relevance weights.

**Example**:
`"The dog that chased the cat was fast."`

- "dog" attends strongly to "was fast" (subject-verb).
- "cat" attends to "chased" (object relation).

### 2. Multi-Head Attention
- Runs **h parallel attention heads** (typically 8–64).
- Each head learns different relationships:
  - Head 1: syntax/grammar
  - Head 2: semantics/meaning  
  - Head 3: long-range coreference
- Concatenate + project: richer representations.

### 3. Feed-Forward Network (FFN)
After attention, each token independently passes through:


- Position-wise transformation.
- Typically 4x wider than embedding dimension.

### 4. Positional Encoding
Transformers are **permutation-invariant** (no order awareness). Solution:

**Example effect**:
- "cat sat mat" vs "mat sat cat" → different positional encodings → model learns order.

### 5. Residual Connections & Layer Normalization
**Stabilizes deep networks**:

**Key**: Causal mask prevents attending to future tokens.

---

## Why Transformers Scale

| Advantage | Impact |
|-----------|--------|
| **Parallelizable** | All tokens processed simultaneously → GPU-friendly |
| **Long-range dependencies** | Attention spans entire context (32K–2M tokens) |
| **Multimodal** | Vision Transformers (ViT), audio, video |
| **Deep stacking** | 100+ layers with residual connections |
| **Transfer learning** | Pretrain once, finetune everywhere |

**Result**: GPT-4 (1.7T+ params), PaLM 2 (340B), LLaMA 3 (405B).

---

## Summary

Transformers combine:
- **Self-attention**: Global context understanding
- **Multi-head**: Multiple relationship types  
- **Positional encoding**: Order awareness
- **Residuals/Norm**: Deep training stability
- **Parallelism**: Massive scaling

They power **all** modern LLMs and form the foundation of generative AI systems.


