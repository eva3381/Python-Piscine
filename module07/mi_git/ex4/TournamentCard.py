from ex4 import Rankable
from ex2 import Combatable
from ex0 import Card


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        game_state['card_played'] = self.name
        game_state['effect'] = "Tournament card enters the arena"
        return (game_state)

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - 1)
        return {
            "defender": self.name,
            "incoming_damage": incoming_damage,
            "damage_taken": damage_taken
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "wins": self.wins,
            "losses": self.losses
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            'name': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }

    def get_tournament_stats(self) -> dict:
        return self.get_rank_info()
