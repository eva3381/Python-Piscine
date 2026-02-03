from ex2 import EliteCard, Combatable, Magical
from ex0 import Card


def get_interface_methods(interface):
    return sorted(interface.__abstractmethods__)


def main():
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print(f"- Card: {get_interface_methods(Card)}")
    print(f"- Combatable: {get_interface_methods(Combatable)}")
    print(f"- Magical: {get_interface_methods(Magical)}")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=6,
        rarity="Legendary",
        health=10,
        damage=5,
        combat_type="melee",
        mana=4
    )

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    print("Combat phase:")
    attack_result = elite.attack("Enemy")
    print("Attack result:", attack_result)

    defend_result = elite.defend(2)
    print("Defense result:", defend_result)

    print("\nMagic phase:")
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell_result)

    mana_result = elite.channel_mana(3)
    print("Mana channel:", mana_result)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
