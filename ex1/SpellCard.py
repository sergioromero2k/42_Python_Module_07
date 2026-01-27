#!/usr/bin/env python3

from ex0.Card import Card


"""Module for the concrete implementation of Spell cards."""


class SpellCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        # Initialize parent attributes and define the specific spell effect
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        # Implementation of the abstract play method for spells
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Spell cast {self.effect_type}"
        }

    def resolve_effect(self, targets: list) -> dict:
        # Handle different spell behaviors based on effect_type
        output = {}

        if self.effect_type == "damage":
            output = {
                "targets": targets, "effect_type": "damage",
                "result": "damage applied"}
        elif self.effect_type == "heal":
            output = {
                "targets": targets, "effect_type": "heal",
                "result": "healing applied"}
        elif self.effect_type == "buff":
            output = {
                "targets": targets, "effect_type": "buff",
                "result": "buff applied"}
        else:
            # Default case for debuffs or other types
            output = {
                "targets": targets, "effect_type": "debuff",
                "result": "debuff applied"}

        return output
