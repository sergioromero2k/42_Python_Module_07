#!/usr/bin/env python3

from typing import Any, Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical

"""
EliteCard implementation merging combat and magical abilities.
Demonstrates multiple inheritance from Card, Combatable, and Magical.
"""


class EliteCard(Card, Combatable, Magical):
    # Powerful card type with both combat and magical capabilities.
    def __init__(
            self, name: str, cost: int, rarity: str,
            attack: int, health: int, magic_power: int
            ) -> None:
        # Initialize the base class Card
        super().__init__(name, cost, rarity)
        # Atributos específicos de EliteCard
        self.attack_points = attack
        self.health = health
        self.magic_power = magic_power
        # Initial value o match PDF example
        self.mana_pool = 4

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        # Implementation of the abstract play method.
        return (
            {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Elite entity enters the battlefield"
            }
        )

    def attack(self, target: str) -> Dict[str, Any]:
        # Execute a melee attack as defined in Combatable interface.
        return (
            {
                "attacker": self.name,
                "target": target,
                "damage": self.attack_points,
                "combat_type": "melee",
                "combat_resolved": True,
            }
        )

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        # Process dfense and update survival status.
        self.health -= incoming_damage
        return (
            {
                "damage_taken": incoming_damage,
                "damage_blocked": 0,
                "still_alive": self.health > 0
            }
        )

    def get_combat_stats(self) -> Dict[str, Any]:
        # Return current combat attributes.
        return (
            {
                "attack_points": self.attack_points,
                "health": self.health,
            }
        )

    def cast_spell(
            # Cast a spell as defined in Magical inteface.
            self, spell_name: str, targets: List[str]) -> Dict[str, Any]:
        return (
            {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": self.cost
            }
        )

    def channel_mana(self, amount: int) -> dict:
        # Increase the mana pool and return status.
        self.mana_pool += amount
        return (
            {
                "channeled": amount,
                "total_mana": self.mana_pool

            }
        )

    def get_magic_stats(self) -> dict:
        # Return current magic attributes.
        return (
            {
                "magic_power": self.magic_power,
                "mana_pool": self.mana_pool
            }
        )
