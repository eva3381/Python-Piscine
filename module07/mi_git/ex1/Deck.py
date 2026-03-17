from ex1 import Card, CreatureCard, SpellCard, ArtifactCard
import random


class Deck():
    def __init__(self):
        self.deck = []

    def add_card(self, card: Card) -> None:
        if (isinstance(card, Card)):
            self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card_name == card.name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if self.deck == []:
            return None
        else:
            draw = self.deck[0]
            self.deck.remove(draw)
            return (draw)

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        cost = 0
        for t in self.deck:
            if isinstance(t, CreatureCard):
                creatures += 1
                cost += t.cost
            elif isinstance(t, SpellCard):
                spells += 1
                cost += t.cost
            elif isinstance(t, ArtifactCard):
                artifacts += 1
                cost += t.cost
        if self.deck == []:
            avg_cost = 0
        else:
            avg_cost = cost / len(self.deck)
        stats = {
            'total_cards': len(self.deck),
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(avg_cost, 2)
        }
        return (stats)
