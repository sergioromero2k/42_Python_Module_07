from ex0 import Card
from abc import ABC, abstractmethod


class GameStrategy(ABC):

    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
