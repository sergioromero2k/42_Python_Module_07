#!/usr/bin/env python3
import random
from tools.card_generator import CardGenerator
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex2.EliteCard import EliteCard
from ex3.CardFactory import CardFactory
from typing import Dict, Any


"""
FantasyCardFactory implementation.
Creates fantasy-themed cards using CardGenerator data.
"""


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.generator = CardGenerator()

    def create_creature(self, name_or_power) -> Card:
        data: Dict[str, Any] = self.generator.get_creature(name_or_power)
        if data:
            return CreatureCard(
                name=data.get("name", "Unkdown"),
                cost=data.get("cost", 1),
                rarity=data.get("rarity", "Common"),
                attack=data.get("attack", 1),
                health=data.get("health", 1),
            )
        # Fallback logic for specific fantasy types
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        elif name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        return CreatureCard("Generic Minion", 1, "Common", 1, 1)

    def create_spell(self, name_or_power) -> Card:
        # Find spell data in generator list
        spell_data = None
        for s in self.generator._spells:
            if s["name"].lower() == str(name_or_power).lower():
                spell_data = s
                break

        if spell_data:
            return SpellCard(
                name=spell_data["name"],
                cost=spell_data["cost"],
                rarity=spell_data["rarity"],
                effect_type=spell_data["effect_type"]
            )

        return SpellCard("Minor Magic", 1, "Common", "General")

    def create_artifact(self, name_or_power) -> Card:
        # Create artifact or elite cards based on generator data
        artifact_data = None
        self.mana_pool = 4

        for s in self.generator._artifacts:
            if s["name"].lower() == str(name_or_power).lower():
                artifact_data = s
                break

        if artifact_data:
            rarity_power = {
                "Common": 5, "Uncommon": 10, "Rare": 15, "Legendary": 25}
            power = rarity_power.get(artifact_data["rarity"], 5)

            artifact = EliteCard(
                name=artifact_data["name"],
                cost=artifact_data["cost"],
                rarity=artifact_data["rarity"],
                attack=0,
                health=artifact_data.get("durability", 5),
                magic_power=power,
            )
            artifact.mana_pool = 4
            return artifact

        generic_artifact = EliteCard("Ancient Relic", 1, "Common", 0, 5, 5)
        generic_artifact.mana_pool = 2
        return generic_artifact

    def get_supported_types(self) -> dict:
        # Return all available names from the generator catalog
        return {
            "creatures": [c["name"] for c in self.generator._creatures],
            "spells": [s["name"] for s in self.generator._spells],
            "artifacts": [a["name"] for a in self.generator._artifacts],
        }

    def create_themed_deck(self, size: int) -> dict:
        # Generate a randomized deck dictionary
        catalog = self.get_supported_types()

        deck_cards = []
        tipos = ["creature", "spell", "artifact"]

        for _ in range(size):
            election = random.choice(tipos)
            if election == "creature":
                name_selected = random.choice(catalog["creatures"])
                card = self.create_creature(name_selected)
                deck_cards.append(card)
            elif election == "spell":
                name_selected = random.choice(catalog["spells"])
                card = self.create_spell(name_selected)
                deck_cards.append(card)
            elif election == "artifact":
                name_selected = random.choice(catalog["artifacts"])
                card = self.create_artifact(name_selected)
                deck_cards.append(card)

        return {
            "deck_name": "Fantasy Deck",
            "cards": deck_cards
        }
