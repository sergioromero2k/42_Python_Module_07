#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict, List

"""
Abstract interface for cards with magical capabilities.
Defines methods for spell casting and mana management.
"""


class Magical(ABC):
    """
    Interface that defines the magical behavior of a card.
    Any card with magical agilities must implement these methods.
    """
    @abstractmethod
    def cast_spell(
            self, spell_name: str, targets: List[str]) -> Dict[str, Any]:
        # Execute a spell with a given name on a list of targets.
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        # Increase the mana pool of the card.
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        # Retrieve current magic-related stats (mana, power, etc).
        pass
