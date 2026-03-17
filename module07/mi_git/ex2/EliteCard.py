from ex0.Card import Card
from ex2 import Combatable, Magical


class EliteCard (Card, Combatable, Magical):
    def __init__(
        self, name: str, cost: int, rarity: str,
            health: int, damage: int, combat_type: str, mana: int):
        super().__init__(name, cost, rarity)
        self.health = health
        self.damage = damage
        self.combat_type = combat_type
        self.mana = mana
        self.count_spell = 0

    def play(self, game_state: dict) -> dict:
        game_state['card_played'] = self.name
        game_state['mana_used'] = self.cost
        return (game_state)

    def attack(self, target) -> dict:
        result = {
            'attacker': self.name, 'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type}
        return (result)

    def defend(self, incoming_damage: int) -> dict:
        alive = True
        damage_taken = self.health - incoming_damage
        if damage_taken <= 0:
            alive = False
        result = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.health - incoming_damage,
            'still_alive': alive
        }
        self.health -= incoming_damage
        return (result)

    def get_combat_stats(self) -> dict:
        stats = {
            'health': self.health,
            'attack': self.damage
        }
        return (stats)

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.count_spell += 1
        spell = {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.mana
        }
        return (spell)

    def channel_mana(self, amount: int) -> dict:
        mana = {
            'channeled': amount,
            'total_mana': self.mana + amount
        }
        self.mana += amount
        return (mana)

    def get_magic_stats(self) -> dict:
        magic_stats = {
            'mana': self.mana,
            'total_spell': self.count_spell
        }
        return (magic_stats)
