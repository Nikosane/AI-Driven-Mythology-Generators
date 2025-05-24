import random
import string

class LanguageGenerator:
    def __init__(self):
        self.consonants = "ptkbdgmnŋfszʃʒhvrlwj"
        self.vowels = "aeiouyɪɛʊɔæʌ"
        self.structures = ["CVC", "CVVC", "CVCC", "CVCV"]

    def generate_word(self):
        structure = random.choice(self.structures)
        word = ""
        for symbol in structure:
            if symbol == "C":
                word += random.choice(self.consonants)
            elif symbol == "V":
                word += random.choice(self.vowels)
        return word

    def generate_language(self, word_count=100):
        lexicon = [self.generate_word() for _ in range(word_count)]
        return {
            "phonemes": list(set(self.consonants + self.vowels)),
            "lexicon": lexicon
        }
