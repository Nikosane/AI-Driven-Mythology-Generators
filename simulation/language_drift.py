
import random

class LanguageDriftSimulator:
    def __init__(self, base_lexicon):
        self.history = [base_lexicon]

    def mutate_word(self, word):
        if len(word) > 1:
            idx = random.randint(0, len(word)-1)
            return word[:idx] + random.choice("abcdefghijklmnopqrstuvwxyz") + word[idx+1:]
        return word

    def simulate_drift(self, generations=10):
        current = self.history[-1].copy()
        for _ in range(generations):
            next_gen = [self.mutate_word(word) for word in current]
            self.history.append(next_gen)
            current = next_gen
        return self.history

if __name__ == "__main__":
    lexicon = ["akra", "dolo", "serin", "mukti"]
    drift_sim = LanguageDriftSimulator(lexicon)
    timeline = drift_sim.simulate_drift()
    for i, lex in enumerate(timeline):
        print(f"Gen {i}: {lex}")
