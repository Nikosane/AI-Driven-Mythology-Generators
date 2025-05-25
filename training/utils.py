
import torch

def get_dummy_text_data(seq_length, vocab_size=5000, batch_size=1):
    x = torch.randint(0, vocab_size, (batch_size, seq_length))
    y = torch.roll(x, shifts=-1, dims=1)
    return x, y


def tokenize_text(text, vocab):
    return [vocab.get(c, 0) for c in text]


def detokenize_text(tokens, inv_vocab):
    return ''.join([inv_vocab.get(t, '?') for t in tokens])
