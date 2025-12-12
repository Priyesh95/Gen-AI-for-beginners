# Tokenization

Tokenization is the process of breaking text into smaller units called **tokens**, which Large Language Models (LLMs) can understand and process numerically. Tokens can represent whole words, parts of words (subwords), characters, punctuation, or special symbols. LLMs work with these numeric representations, not raw text strings.

---

## Why Tokenization Matters

Tokenization serves several critical functions:

- **Reduces complexity**: Models learn patterns from smaller, consistent units rather than entire words.
- **Handles rare/new words**: Unknown words like "chatGPTify" split into familiar parts: `chat` + `GPT` + `ify`.
- **Enables efficiency**: Consistent token units compress massive datasets for faster training and inference.
- **Manages context limits**: LLMs have token budgets (8K, 32K, 128K+), so understanding token count optimizes prompts.

**Practical note**: ~1,000 English words ≈ 750 tokens due to subword splitting and punctuation.

---

## Types of Tokenization

### 1. Word-Level Tokenization

- Splits on spaces and punctuation into whole words.
- **Example**:
```
"Machine learning is fun"
→ ["Machine", "learning", "is", "fun"]
```

- **Issue**: Fails on unknown/out-of-vocabulary words (common in real-world text).

### 2. Character-Level Tokenization

- Breaks text into individual characters.
- **Example**:
```
"cat" → ["c", "a", "t"]
```

- **Issue**: Generates too many tokens, making sequences inefficiently long.

### 3. Subword Tokenization (Modern Standard)

- Splits words into meaningful chunks using algorithms like **BPE** (Byte Pair Encoding) or **WordPiece**.
- **Example**:
```
"unbelievable" → ["un", "believ", "able"]
"ChatGPT" → ["Chat", "G", "PT"]
```

- **Why best**: Balances vocabulary size (50K–100K tokens) with flexibility for rare words.

---

**Observations**:
- Proper nouns split into subwords.
- Spaces often attach to following tokens.
- Punctuation becomes separate tokens.

---

## Token IDs and Processing

After tokenization, each token maps to a unique numeric ID from the model's vocabulary.

### Simple Code Example (Python: GPT-2 Tokenizer)

```python
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text = "Tokenization helps LLMs understand text."

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Tokens:", tokens)
print("Token IDs:", token_ids)
```

**Expected output** (approximate):

```
Tokens: ['Token', 'ization', ' help', 's', ' LL', 'Ms', ' understand', ' text', '.']
Token IDs: [5680, 23624, 1792, 192, 9945, 20651, 4602, 2331,s
```

## Practical Implications

Token Limits Affect:
  - Cost: API billing by tokens (input + output).
  - Performance: Longer contexts = slower inference.
  - Prompt design: Concise prompts save tokens.
  
Token Count Rules of Thumb:
  - English: ~0.75 tokens per word.
  - Code: ~0.5–1 token per word (identifiers split).
  - Dense math: Higher token density.


