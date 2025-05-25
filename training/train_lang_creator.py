from models.lang_creator import LanguageGenerator


def train():
    generator = LanguageGenerator()
    lang = generator.generate_language(word_count=50)
    print("Generated Language:\n")
    print("Phonemes:", lang['phonemes'])
    print("Lexicon:", lang['lexicon'])


if __name__ == "__main__":
    train()
