#!/usr/bin/env python3

from ex4.TournamentCard import TournamentCard

"""
Tournament platform to manage and run matches between TournamentCards.
"""


class TournamentPlatform:
    def __init__(self):
        """
        Initialize the tournament platform with an empty card registry,
        zero matches played, and active status.
        """
        self.cards = {}
        self.matches_played = 0
        self.platform_status = "active"

    def register_card(self, card: TournamentCard) -> str:
        # Register a card to the platform.
        if card.card_id in self.cards:
            return f"Card already registered: {card.name} ({card.card_id})"
        self.cards[card.card_id] = card
        return f"Card registered: {card.name} ({card.card_id})"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        # Simulate a match between two cards.
        # Ensure both cards exist
        if card1_id not in self.cards or card2_id not in self.cards:
            return {"error": "One or both cards not found in the platform."}

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        # Card1 attacks → Card2 defends
        damage1 = card1.attack(card2.card_id)
        card2.defend(damage1["damage"])

        # Card2 attacks → Card1 defends
        damage2 = card2.attack(card1.card_id)
        card1.defend(damage2["damage"])

        # Determine winner based on remaining health
        if card1.health > card2.health:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        # Update wins and losses
        winner.update_wins(1)
        loser.update_losses(1)

        # Increment total matches played
        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        # Retrieve a leaderboard ordered by card rating (descending).
        cards = self.cards.values()

        # Sort cards by rating from highest to lowest
        def get_rating(card):
            return card.calculate_rating()

        cards_ordered = sorted(cards, key=get_rating, reverse=True)

        # Build the leaderboard
        leaderboard = []
        for card in cards_ordered:
            leaderboard.append({
                "name": card.name,
                "rating": card.calculate_rating(),
                "wins": card.wins,
                "losses": card.losses
            })

        return leaderboard

    def generate_tournament_report(self) -> dict:
        # Generate a summary report of the tournament platform.
        avg_rating = 0
        for card in self.cards.values():
            avg_rating += card.calculate_rating()

        if len(self.cards) > 0:
            avg_rating = round(avg_rating / len(self.cards), 2)
        else:
            avg_rating = 0

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": self.platform_status
        }
