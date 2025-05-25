import torch
import torch.nn as nn
import torch.optim as optim
from models.hierarchy_rnn import StoryGenerator
from training.utils import get_dummy_text_data

# Configs
EPOCHS = 10
VOCAB_SIZE = 5000
SEQ_LENGTH = 30

# Training loop

def train():
    story_gen = StoryGenerator(VOCAB_SIZE)
    model = story_gen.model
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(EPOCHS):
        inputs, targets = get_dummy_text_data(SEQ_LENGTH)
        outputs, _ = model(inputs)
        loss = criterion(outputs.view(-1, VOCAB_SIZE), targets.view(-1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch}: Loss = {loss.item():.4f}")

if __name__ == "__main__":
    train()
