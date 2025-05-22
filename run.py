import argparse
from generation import myth_generator, ritual_generator, pantheon_builder
from simulation import timeline_sim, god_conflict_sim
from memory import myth_db
import utils.logger as logger

def main():
    parser = argparse.ArgumentParser(description="AI-Driven Mythology Generator")
    parser.add_argument('--generate', action='store_true', help="Generate a new mythology")
    parser.add_argument('--simulate', action='store_true', help="Run simulation of mythology evolution")
    parser.add_argument('--explore', action='store_true', help="Print existing mythological data")

    args = parser.parse_args()

    if args.generate:
        logger.log("🔮 Generating a new mythology...")
        pantheon = pantheon_builder.generate_pantheon()
        rituals = ritual_generator.generate_rituals(pantheon)
        mythos = myth_generator.generate_myths(pantheon, rituals)
        myth_db.save_mythology(pantheon, rituals, mythos)
        logger.log("✅ Mythology generation complete and saved.")

    elif args.simulate:
        logger.log("🧬 Starting mythology evolution simulation...")
        timeline_sim.run_timeline_simulation()
        god_conflict_sim.simulate_conflicts()
        logger.log("✅ Simulation completed.")

    elif args.explore:
        logger.log("📖 Exploring saved mythology...")
        saved_data = myth_db.load_mythology()
        print(saved_data)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
