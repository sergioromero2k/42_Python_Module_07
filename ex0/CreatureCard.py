#!/usr/bin/env python3

"""
Module for the concrete implementation of Creature cards.
"""
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        # Initialize parent attributes and validate creature-specific stats
        super().__init__(name, cost, rarity)

        # Attack must be a positive integer
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        self.attack = attack

        # health must be a positive integer
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")
        self.health = health

    def play(self, game_state: dict) -> dict:
        # Implementation of the abstract play method from Card
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> dict:
        # Specific behavior for creature combat
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    # def get_card_info(self) -> dict:
    #     # Returns dictionary including base info and creature stats
    #     return {
    #         "name": self.name,
    #         "cost": self.cost,
    #         "rarity": self.rarity,
    #         "type": "Creature",
    #         "attack": self.attack,
    #         "health": self.health
    #     }
