import argparse
from generation.myth_generator import MythGenerator


def main():
    parser = argparse.ArgumentParser(description="AI-Driven Mythology Generator")
    parser.add_argument("--generate", action="store_true", help="Generate a new mythology")
    parser.add_argument("--pantheon", type=int, default=5, help="Number of gods to include")
    args = parser.parse_args()

    if args.generate:
        print("\n--- Generating AI-Driven Mythology ---\n")
        mg = MythGenerator()
        myth = mg.generate_full_myth(pantheon_size=args.pantheon)

        print("\n--- Pantheon ---")
        for god in myth["pantheon"]:
            print(god)

        print("\n--- Rituals ---")
        for ritual in myth["rituals"]:
            print(f"- {ritual}")

        print("\n--- Culture Snapshot ---")
        print(myth["culture"])

        print("\n--- Timeline ---")
        for event in myth["timeline"]:
            print(f"Year {event['year']}: {event['event']}")

if __name__ == "__main__":
    main()
