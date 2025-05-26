from models.hierarchy_rnn import StoryGenerator
from models.evolution_model import Culture

class MythGenerator:
    def __init__(self):
        self.story_gen = StoryGenerator()
        self.culture = Culture("Primordial Tribe")

    def generate_myth(self):
        # Evolve culture
        evolution = self.culture.evolve()

        # Generate story
        myth = self.story_gen.generate(seed_sequence=None)

        return {
            "myth": myth,
            "culture": evolution
        }

if __name__ == "__main__":
    generator = MythGenerator()
    full_myth = generator.generate_myth()
    print("Generated Myth:\n")
    print(full_myth["myth"])
    print("\nCultural Snapshot:\n", full_myth["culture"])
