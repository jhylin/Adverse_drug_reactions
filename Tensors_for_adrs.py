## Code below extracted from ADR_test.ipynb
## A function code has already been saved in adr_tensors.py to generate tensors for a single drug

## Example - trial generating tensors on ADRs for ONE drug e.g. terfenadine
# https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html

import pandas as pd
import torch
print(torch.__version__)
import torch.nn as nn
from collections import Counter

torch.manual_seed(1)

sentence = "dizziness^^, syncopal_episodes^^, palpitations^, ventricular_arrhythmias^^, cardiac_arrest^^, cardiac_death^^, headaches^"

words = sentence.split(', ')

# create a dictionary
vocab = Counter(words) 

vocab = sorted(vocab)

vocab_size = len(vocab)

# create a word to index dictionary from the vocab
word2idx = {word: ind for ind, word in enumerate(vocab)} 

for word in words:
    word2idx[word]
    print(word)

# Create a list of words from the word2idx dictionary
encoded_sentences = [word2idx[word] for word in words]

## docs: https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding
# assign a value to embedding_dim - the size of each embedding vector (usually embedding_dim << no. of words)
embedding_dim = 5

## initialise an embedding layer from Torch
# padding_idx - padding an input at the set index and insert zero, meaning not going to contribute to the gradient
# vocab_size = num_embeddings - size of the dictionary of embeddings
emb = nn.Embedding(vocab_size, embedding_dim)
word_vectors = torch.LongTensor(encoded_sentences)
emb(word_vectors)



## save all ADRs from common ADRs column as a list & join separate strings into one string
data = pd.read_csv("CYP3A4_strong_substrates")
adr_str = data["common_adverse_effects^^"].tolist()
adr_string = ",".join(adr_str)

# Converting all common ADRs into Torch tensors (using a work-in-progress function script - adr_tensors.py)
from adr_tensors import adr_tensors
adr = adr_tensors(adr_string)