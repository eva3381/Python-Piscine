from ex4 import TournamentPlatform, TournamentCard


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 5)

    wizard.rating = 1150

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"\nFire Dragon (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print(f"\nIce Wizard (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()

    for i, entry in enumerate(leaderboard, start=1):
        print(
            f"{i}. {entry['name']} - Rating: {entry['rating']} "
            f"({entry['wins']}-{entry['losses']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
