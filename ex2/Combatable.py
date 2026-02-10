#!/usr/bin/env python3
from abc import ABC, abstractmethod
# Authorized: abc, typing, enum, random, print()

"""
Abstract interface for combat-capable cards.
Defines the mandatory contract for attacking, defending,
and stat retrieval.
"""


class Combatable(ABC):
    """
    Interface that defines combat behaviors for DataDeck cards.
    Any class inheriting from this must implement attack and defense logic.
    """
    @abstractmethod
    def attack(self, target: str) -> dict:
        # Execute an attack against a target.
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        # Process incoming damage to the card.
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        # Retrieve the current combat attributes (attack and health).
        pass
