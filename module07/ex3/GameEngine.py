

class GameEngine():
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory, strategy):
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self):
        creature = self.factory.create_creature("goblin")
        spell = self.factory.create_spell("fireball")
        hand = [creature, spell]
        battelfield = [creature]
        self.cards_created += len(hand)
        turn_result = self.strategy.execute_turn(hand, battelfield)
        self.turns_simulated += 1
        self.total_damage += turn_result.get("damage_dealt", 0)
        return (turn_result)

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
            if self.strategy else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
