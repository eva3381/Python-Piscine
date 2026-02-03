from ex3 import GameStrategy


class AggressiveStrategy (GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_available = 5
        mana_used = 0
        cards_played = []
        targets_attacked = []
        hand_sorted = sorted(hand, key=lambda card: card.cost)

        for card in hand_sorted:
            if card.is_playable(mana_available):
                cards_played.append(card.name)
                mana_used += card.cost
                mana_available -= card.cost
        available_targets = ["Enemy Player"]
        targets_attacked = self.prioritize_targets(available_targets)

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        prioritized = []
        for enemy in available_targets:
            if enemy == 'Enemy Player':
                prioritized.append(enemy)
                available_targets.remove(enemy)
        for enemy in available_targets:
            prioritized.append(enemy)
        return (prioritized)
