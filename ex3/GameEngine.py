#!/usr/bin/env python3

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

"""
GameEngine implementation.
Orchestrates the interaction between the CardFactory and GameStrategy.
"""


class GameEngine:
    """Main controller for game simulation and state management."""

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:
        # Set up the engine with the provided factory and strategy
        self.factory = factory
        self.strategy = strategy
        self.mana = 1
        self.player_health = 20
        self.opponent_health = 20

        # Create the initial deck using the factory
        deck_data = self.factory.create_themed_deck(10)
        self.deck = deck_data.get("cards", [])
        self.hand = []
        self.battlefield = []

    def simulate_turn(self) -> dict:
        # Draw a card if available
        if self.deck:
            self.hand.append(self.deck.pop(0))

        # Increase mana each turn
        self.mana += 1

        # Execute strategy logic and get the summary of actions
        turn_results = self.strategy.execute_turn(self.hand, self.battlefield)

        return turn_results

    def get_engine_status(self) -> dict:
        # Return the current state of the game engine
        return {
            "player_health": self.player_health,
            "opponent_health": self.opponent_health,
            "mana": self.mana,
            "cards_in_hand": len(self.hand),
            "creatures_on_board": len(self.battlefield)
        }
