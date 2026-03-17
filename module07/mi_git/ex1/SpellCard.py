from ex1 import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state['card_played'] = self.name
        game_state['mana_used'] = self.cost
        game_state['effect'] = self.effect_type
        return (game_state)

    def resolved_effect(self, target: list) -> dict:
        result = {
            'spell_name': self.name, 'target': target,
            'effect_type': self.effect_type,
            'spell_resolved': True}
        return (result)
