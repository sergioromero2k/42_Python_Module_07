#!/usr/bin/env python3

from ex0.Card import Card

"""Module for the concrete implementation of Artifact cards."""


class ArtifactCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str,
            durability: int, effect: str) -> None:
        # Initialize parent attributes and artifact-specific properties
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        # Return play results for the artifact
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        # Handle ability usage and durability depletion
        if self.durability > 0:
            self.durability -= 1
            return {
                "artifact": self.name,
                "effect": self.effect,
                "durability_left": self.durability
            }
        else:
            # Case when durability is already exhausted
            return {
                "artifact": self.name,
                "effect": self.effect,
                "durability_left": 0
            }
