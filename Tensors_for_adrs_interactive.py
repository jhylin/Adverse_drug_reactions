## Code below extracted from ADR_test.ipynb
## A function code has already been saved in adr_tensors.py to generate tensors for multiple drugs

## Example - trial generating tensors on ADRs for ONE drug e.g. terfenadine
# ref. re. PyTorch embeddings - https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html
# Adding # %% to initiate jupyter-like code cells that can be run interactively in VS Code

# %%
import pandas as pd
print(pd.__version__)
import torch
print(torch.__version__)
import torch.nn as nn
from collections import Counter

torch.manual_seed(1)

sentence = "dizziness^^, syncopal_episodes^^, palpitations^, ventricular_arrhythmias^^, cardiac_arrest^^, cardiac_death^^, headaches^"
words = sentence.split(', ')
words

# %%
# create a dictionary
vocab = Counter(words) 
vocab

# %%
vocab = sorted(vocab)
vocab

# %%
vocab_size = len(vocab)
vocab_size

# %%
# create a word to index dictionary from the vocab
word2idx = {word: ind for ind, word in enumerate(vocab)} 
word2idx

# %%
for word in words:
    word2idx[word]
    print(word)

# %%
# Create a list of words from the word2idx dictionary
encoded_sentences = [word2idx[word] for word in words]
encoded_sentences

# %%
## docs: https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding
# assign a value to embedding_dim - the size of each embedding vector (usually embedding_dim << no. of words)
embedding_dim = 5

## initialise an embedding layer from Torch
# padding_idx - padding an input at the set index and insert zero, meaning not going to contribute to the gradient
# vocab_size = num_embeddings - size of the dictionary of embeddings
emb = nn.Embedding(vocab_size, embedding_dim)
word_vectors = torch.LongTensor(encoded_sentences)
emb(word_vectors)
