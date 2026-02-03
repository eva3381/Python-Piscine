

class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card) -> str:
        formating = card.name.lower().replace(' ', '_')
        card_id = f"{formating}_{len(self.cards) + 1:03d}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)

        if not card1 or not card2:
            raise ValueError("Invalid card IDs")

        if card1.rating >= card2.rating:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        leaderboard = sorted(
            self.cards.items(),
            key=lambda item: item[1].rating,
            reverse=True
        )

        return [
            {
                "id": card_id,
                **card.get_rank_info()
            }
            for card_id, card in leaderboard
        ]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        avg_rating = (
            sum(card.rating for card in self.cards.values()) / total_cards
            if total_cards > 0 else 0
        )

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": int(avg_rating),
            "platform_status": "active"
        }
