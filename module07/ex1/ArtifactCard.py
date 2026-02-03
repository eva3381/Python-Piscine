from ex1 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect: str):
        super().__init__(name, cost, rarity)
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        game_state['card_played'] = self.name
        game_state['mana_used'] = self.cost
        game_state['effect'] = self.effect
        return (game_state)

    def activate_ability(self) -> dict:
        result = {
            'artifact_name': self.name,
            'effect': self.effect,
            'artifact_resolved': True}
        return (result)
