from ex0 import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str,
            attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not (isinstance(health, int)):
            raise TypeError("Health must be a positve integer")
        if health <= 0:
            raise TypeError("Health must be a positive integer")
        self.health = health
        if not (isinstance(attack, int)):
            raise TypeError("Attack must be a positive integer")
        if attack <= 0:
            raise TypeError("Attack must be a positive integer")
        self.attack = attack

    def play(self, game_state: dict) -> dict:
        game_state['card_played'] = self.name
        game_state['mana_used'] = self.cost
        game_state['effect'] = 'Creature summoned to battlefield'
        return (game_state)

    def attack_target(self, target: str) -> dict:
        result = {
            'attacker': self.name, 'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True}
        return (result)

    def get_card_info(self):
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return (info)
