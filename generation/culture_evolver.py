import random

class CultureEvolver:
    def __init__(self, name):
        self.name = name
        self.beliefs = ["Ancestor Worship", "Totem Spirits"]
        self.rituals = ["Blood Sacrifice", "Harvest Festival"]

    def evolve(self):
        if random.random() < 0.5:
            new_belief = random.choice(["Sun Worship", "Underworld Travel", "Divine Kingship"])
            self.beliefs.append(new_belief)
        else:
            new_ritual = random.choice(["Moon Dance", "Feast of Shadows", "Initiation Trial"])
            self.rituals.append(new_ritual)

    def get_snapshot(self):
        return {
            "name": self.name,
            "beliefs": self.beliefs,
            "rituals": self.rituals
        }

if __name__ == "__main__":
    ce = CultureEvolver("Ashen Tribe")
    for _ in range(5):
        ce.evolve()
    print("Culture Snapshot:\n", ce.get_snapshot())

