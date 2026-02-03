from ex1 import CreatureCard, SpellCard, ArtifactCard, Deck


def main():
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")

    spell = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2, "Rare",
                            "Permanent: +1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 10)

    deck = Deck()

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")

    while True:
        card = deck.draw_card()
        if card is None:
            break

        print(
            f"\nDrew: {card.name} "
            f"({card.__class__.__name__.replace('Card', '')})")

        result = card.play({})
        print("Play result:", result)
    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
