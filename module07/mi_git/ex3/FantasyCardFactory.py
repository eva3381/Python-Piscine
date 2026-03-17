from ex3 import CardFactory
from ex0 import Card, CreatureCard
from ex1 import ArtifactCard, SpellCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power.lower() == "dragon":
                return CreatureCard(
                    "Fire Dragon",
                    6,
                    "Legendary",
                    7,
                    6
                )
            elif name_or_power.lower() == "goblin":
                return CreatureCard(
                    "Goblin Warrior",
                    2,
                    "Common",
                    2,
                    2
                )

        elif isinstance(name_or_power, int):
            return CreatureCard(
                f"Scaled Creature {name_or_power}",
                name_or_power,
                "Rare" if name_or_power >= 5 else "Common",
                name_or_power,
                name_or_power
            )

    def create_spell(self, name_or_power) -> Card:
        if isinstance(name_or_power, str):
            spell = name_or_power.lower()

            if spell == "fire":
                return SpellCard(
                    "Fire Spell",
                    3,
                    "Rare",
                    "damage"
                )
            elif spell == "ice":
                return SpellCard(
                    "Ice Spell",
                    2,
                    "Common",
                    "freeze"
                )
            elif spell == "lightning":
                return SpellCard(
                    "Lightning Spell",
                    4,
                    "Epic",
                    "damage"
                )

        elif isinstance(name_or_power, int):
            return SpellCard(
                f"Elemental Spell {name_or_power}",
                name_or_power,
                "Rare" if name_or_power >= 5 else "Common",
                "damage"
            )

    def create_artifact(self, name_or_power) -> Card:
        if isinstance(name_or_power, str):
            artifact = name_or_power.lower()

            if artifact == "ring":
                return ArtifactCard(
                    "Magic Ring",
                    2,
                    "Rare",
                    5,
                    "+1 mana per turn"
                )
            elif artifact == "staff":
                return ArtifactCard(
                    "Wizard Staff",
                    3,
                    "Epic",
                    4,
                    "+2 spell damage"
                )
            elif artifact == "crystal":
                return ArtifactCard(
                    "Mana Crystal",
                    2,
                    "Uncommon",
                    6,
                    "+1 mana"
                )

        elif isinstance(name_or_power, int):
            return ArtifactCard(
                f"Ancient Relic {name_or_power}",
                name_or_power,
                "Rare",
                name_or_power,
                "+1 power to cards"
            )

    def create_themed_deck(self, size: int) -> dict:
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }

        for i in range(size):
            deck["creatures"].append(self.create_creature("goblin"))
            deck["spells"].append(self.create_spell("fire"))

            if i % 2 == 0:
                deck["artifacts"].append(self.create_artifact("ring"))

        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fire", "ice", "lightning"],
            "artifacts": ["ring", "staff", "crystal"]
        }
