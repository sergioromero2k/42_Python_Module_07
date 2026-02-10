#!/usr/bin/env python3
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

"""
Concrete implementation of a tournament card.
This class combines the base Card functionality with combat
and ranking capabilities.
"""


class TournamentCard(Card, Combatable, Rankable):
    """
    Initialize a TournamentCard with combat stats, ranking, and unique ID.
    """
    def __init__(
        self, name, cost,
        rarity, card_id, attack_power, health, wins, losses, rating
    ):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.attack_power = attack_power
        self.health = health
        self.wins = wins
        self.losses = losses
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        # Play the card if sufficient mana is available.
        mana = game_state.get("mana", 0)

        if self.is_playable(mana):
            game_state["mana"] = mana - self.cost
            return {
                "success": True,
                "action": "played",
                "card_name": self.name,
                "cost": self.cost,
                "mana_before": mana,
                "mana_after": mana - self.cost,
            }
        return {
            "success": False,
            "reason": "not enough mana",
            "card_name": self.name,
            "cost": self.cost,
            "mana_available": mana,
        }

    def attack(self, target: str) -> dict:
        # Execute a combat attack against a target.
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "action": "attack",
            "attacker_health": self.health,
        }

    def defend(self, incoming_damage: int) -> dict:
        # Receive incoming damage and update health accordingly.
        self.health -= incoming_damage
        if self.health < 0:
            self.health = 0

        if self.health == 0:
            defeated = True
        else:
            defeated = False

        return {
            "target": self.name,
            "damage_received": incoming_damage,
            "health_remaining": self.health,
            "defeated": defeated,
            "action": "defend",
        }

    def get_combat_stats(self) -> dict:
        # Retrieve the card's combat stats.
        return {
            "name": self.name,
            "attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        """ Calculate the card's rating
        based on combat stats and win/loss record."""
        rating = (
            1000
            + self.attack_power
            + self.health
            + (self.wins * 10)
            - (self.losses * 5)
        )
        return rating

    def update_wins(self, wins: int) -> None:
        # Add wins to the card's win count.
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        # Add losses to the card's loss count.
        self.losses += losses

    def get_rank_info(self) -> dict:
        # Retrieve ranking and status information.
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
            "attack": self.attack_power,
            "health": self.health,
            "status": "defeated" if self.health == 0 else "alive"
        }
