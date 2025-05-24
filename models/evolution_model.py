
import random

class Culture:
    def __init__(self, name):
        self.name = name
        self.beliefs = {}
        self.gods = []
        self.rituals = []

    def evolve_beliefs(self):
        change = random.choice(["peace", "war", "harvest", "sacrifice"])
        self.beliefs[change] = self.beliefs.get(change, 0) + 1

    def evolve_gods(self):
        if random.random() < 0.3:
            new_god = f"God_{random.randint(100, 999)}"
            self.gods.append(new_god)

    def evolve_rituals(self):
        if random.random() < 0.4:
            new_ritual = f"Ritual_{random.randint(1000, 9999)}"
            self.rituals.append(new_ritual)

    def evolve(self):
        self.evolve_beliefs()
        self.evolve_gods()
        self.evolve_rituals()
        return {
            "culture": self.name,
            "beliefs": self.beliefs,
            "gods": self.gods,
            "rituals": self.rituals
        }
