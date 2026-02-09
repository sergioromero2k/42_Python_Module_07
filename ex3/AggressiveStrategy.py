#!/usr/bin/env python3

"""
AggressiveStrategy implementation for DataDeck.
Prioritizes low-cost cards and direct damage to the opponent.
"""

from typing import List, Any


class AggressiveStrategy:
    """Concrete strategy that focuses on offensive gameplay."""

    def execute_turn(self, hand: List[Any], battlefield: List[Any]) -> dict:
        # Plays the cheapest card available and returns turn actions.
        # This simulates the logic of playing a card and attacking
        played_cards = []
        damage_dealt = 0

        # In a real engine, mana would be passed or managed here
        # For the exercise, we return the turn summary as a dictionary
        return {
            "cards_played": played_cards,
            "mana_used": 0,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        # Returns the name of the strategy.
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        # Targets the enemy player directly as top priority.
        # Aggressive strategy always aims for the main objective
        return sorted(
            available_targets,
            key=lambda x: getattr(x, "is_player", False),
            reverse=True,
        )

    def play_card(self, hand: List[Any], mana: int):
        # Finds and returns the cheapest playable card.
        # Filter cards that the player can afford
        possible = [card for card in hand if card.cost <= mana]

        if not possible:
            return None

        # Return the card with the lowest mana cost
        return min(possible, key=lambda card: card.cost)

    def attack(self, creatures: List[Any], opponent: Any):
        # Commands all creatures on the battlefield to attack.
        for creature in creatures:
            creature.attack(opponent)
