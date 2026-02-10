#!/usr/bin/env python3

"""
Module defining the abstract foundation for all game cards.
"""

from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        # Initialize basic card atrributes
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        # To be implemented by concrete subclasses
        pass

    def get_card_info(self) -> dict:
        # Return base card data as a dictionary
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        # Compare cost against available mana pool
        if available_mana >= self.cost:
            return True
        return False
