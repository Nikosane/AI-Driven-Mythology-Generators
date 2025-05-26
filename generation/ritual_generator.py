
from models.evolution_model import Culture

class RitualGenerator:
    def __init__(self, culture_name="Default Tribe"):
        self.culture = Culture(culture_name)

    def generate_rituals(self, steps=5):
        for _ in range(steps):
            self.culture.evolve_rituals()
        return self.culture.rituals

if __name__ == "__main__":
    ritual_gen = RitualGenerator("Sun Worshippers")
    rituals = ritual_gen.generate_rituals()
    print("Generated Rituals:\n", rituals)
