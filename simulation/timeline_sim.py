import random

class TimelineSimulator:
    def __init__(self):
        self.timeline = []

    def simulate_event(self, year):
        events = [
            "Great Flood",
            "Divine War",
            "Golden Age",
            "Demon Invasion",
            "Celestial Eclipse",
            "Empire Collapse"
        ]
        event = random.choice(events)
        self.timeline.append({"year": year, "event": event})

    def run_simulation(self, start=0, end=1000, step=100):
        for year in range(start, end + 1, step):
            self.simulate_event(year)
        return self.timeline

if __name__ == "__main__":
    sim = TimelineSimulator()
    result = sim.run_simulation()
    print("Mythos Timeline:\n")
    for e in result:
        print(f"Year {e['year']}: {e['event']}")
