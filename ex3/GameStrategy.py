#!/usr/bin/env python3
from abc import ABC, abstractmethod


"""
Abstract Strategy interface for DataDeck.
Defines the contract for turn execution and target prioritization.
"""


class GameStrategy(ABC):
    """Abstract base class for all game strategies."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        # Defines how a turn is executed and returns action results
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        # Returns the unique identifier name of the strategy
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        # Determines the order of targets to attack during a turn
        pass
