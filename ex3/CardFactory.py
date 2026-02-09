#!/usr/bin/env python3
from abc import ABC, abstractmethod
from ex0.Card import Card

"""
Abstract Factory interface for DataDeck card creation.
"""


class CardFactory(ABC):
    """Abstract interface for the card factory."""

    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        # Creates a creature card based on name or power
        pass

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        # Creates a spell card based on name or power
        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        # Creates an artifact card based on name or power
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        # Creates a deck dictionary with the specified size
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        # Returns a dictionary of supported card types
        pass
