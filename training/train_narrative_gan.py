import torch
import torch.nn as nn
import torch.optim as optim
from models.narrative_gan import NarrativeGAN

# Configs
EPOCHS = 1000
BATCH_SIZE = 16
NOISE_DIM = 100
OUTPUT_DIM = 500

# Fake dataset for now
def get_fake_data(batch_size, output_dim):
    return torch.randn(batch_size, output_dim)

# Training loop (simplified)
def train():
    gan = NarrativeGAN(NOISE_DIM, OUTPUT_DIM)
    criterion = nn.BCELoss()
    optimizer_G = optim.Adam(gan.generator.parameters(), lr=0.0002)
    optimizer_D = optim.Adam(gan.discriminator.parameters(), lr=0.0002)

    for epoch in range(EPOCHS):
        real_data = get_fake_data(BATCH_SIZE, OUTPUT_DIM)
        real_labels = torch.ones(BATCH_SIZE, 1)
        fake_labels = torch.zeros(BATCH_SIZE, 1)

        # Train Discriminator
        gan.discriminator.zero_grad()
        outputs = gan.discriminator(real_data)
        d_loss_real = criterion(outputs, real_labels)

        noise = torch.randn(BATCH_SIZE, NOISE_DIM)
        fake_data = gan.generator(noise)
        outputs = gan.discriminator(fake_data.detach())
        d_loss_fake = criterion(outputs, fake_labels)

        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_D.step()

        # Train Generator
        gan.generator.zero_grad()
        noise = torch.randn(BATCH_SIZE, NOISE_DIM)
        fake_data = gan.generator(noise)
        outputs = gan.discriminator(fake_data)
        g_loss = criterion(outputs, real_labels)

        g_loss.backward()
        optimizer_G.step()

        if epoch % 100 == 0:
            print(f"Epoch {epoch}: D Loss = {d_loss.item():.4f}, G Loss = {g_loss.item():.4f}")

if __name__ == "__main__":
    train()
