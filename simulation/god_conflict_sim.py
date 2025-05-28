import random

class GodConflictSimulator:
    def __init__(self, gods):
        self.gods = gods
        self.conflicts = []

    def simulate_conflict(self):
        if len(self.gods) < 2:
            return
        attacker, defender = random.sample(self.gods, 2)
        result = random.choice(["wins", "loses", "forms alliance with"])
        self.conflicts.append({
            "attacker": attacker["name"],
            "defender": defender["name"],
            "outcome": result
        })

    def run_simulation(self, rounds=5):
        for _ in range(rounds):
            self.simulate_conflict()
        return self.conflicts

if __name__ == "__main__":
    gods = [
        {"name": "Auron"},
        {"name": "Nyx"},
        {"name": "Velth"},
        {"name": "Zara"}
    ]
    sim = GodConflictSimulator(gods)
    outcome = sim.run_simulation()
    print("God Conflicts:\n")
    for conflict in outcome:
        print(conflict)
