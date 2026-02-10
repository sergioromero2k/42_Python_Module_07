#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""
Abstract interface for rankable cards.
Defines the mandatory contract for rating calculations and tracking wins/losses
"""


class Rankable(ABC):
    """
    Interfaces that allows a card to be ranked in tournaments or leaderboards.
    """
    @abstractmethod
    def calculate_rating(self) -> int:
        # Calculate and return the current rating of the card.
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        # Update the card's win count
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        # Update the card's loss count.
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        # Retrieve ranking information as a dictionary.
        pass
