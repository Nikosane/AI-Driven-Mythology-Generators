import random

class PantheonBuilder:
    def __init__(self):
        self.gods = []

    def create_god(self):
        name = f"Deity_{random.randint(1000, 9999)}"
        domain = random.choice(["war", "love", "sea", "sun", "death", "dreams"])
        power = random.randint(1, 100)
        god = {
            "name": name,
            "domain": domain,
            "power_level": power,
            "relationships": {}
        }
        self.gods.append(god)
        return god

    def create_relationships(self):
        for god in self.gods:
            others = [g for g in self.gods if g != god]
            if others:
                related = random.choice(others)
                god['relationships'][related['name']] = random.choice(["sibling", "rival", "parent", "lover"])

    def build_pantheon(self, count=5):
        for _ in range(count):
            self.create_god()
        self.create_relationships()
        return self.gods

if __name__ == "__main__":
    pb = PantheonBuilder()
    pantheon = pb.build_pantheon()
    print("Generated Pantheon:\n")
    for god in pantheon:
        print(god)
