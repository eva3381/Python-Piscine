from ex3 import GameEngine, FantasyCardFactory, AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    dragon = factory.create_creature("dragon")
    goblin = factory.create_creature("goblin")
    lightning = factory.create_spell("lightning")

    hand = [dragon, goblin, lightning]
    battlefield = [dragon]

    print(
        f"Hand: [{dragon.name} ({dragon.cost}), {goblin.name} "
        f"({goblin.cost}), {lightning.name} ({lightning.cost})]")

    turn_result = strategy.execute_turn(hand, battlefield)

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {turn_result}")

    engine.turns_simulated += 1
    engine.cards_created += len(hand)

    print("\nGame Report:")
    print(engine.get_engine_status())
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
