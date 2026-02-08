#!/usr/bin/env python3

"""
Module defining the abstract foundation for all game cards.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        # Initialize basic card atrributes
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        # To be implemented by concrete subclasses
        pass

    def get_card_info(self) -> Dict[str, Any]:
        # Return base card data as a dictionary
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, avaliable_mana: int) -> bool:
        # Compare cost against available mana pool
        if avaliable_mana >= self.cost:
            return True
        return False
