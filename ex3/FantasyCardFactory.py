#!/usr/bin/env python3
from abc import ABC, abstractmethod
from tools.card_generator import CardGenerator
from ex0 import CreatureCard, Card
from ex1 import SpellCard
from ex2 import EliteCard
from ex3 import CardFactory
from typing import Dict, List, Any


class FantasyCardFactory(CardFactory):
    
    def __init__(self):
        self.generator = CardGenerator()

    def create_creature(self, name_or_power) -> Card:
        data : Dict[str, Any] = self.generator.get_creature(name_or_power)

        if data:
            return CreatureCard(
                name = data.get("name", "Unkdown"),
                cost = data.get("cost", 1),
                rarity = data.get("rarity", "Common"),
                attack = data.get("attack", 1),
                health = data.get("health", 1)
            )
        if name_or_power == "dragon":
            CreatureCard("Fire Dragon",5, "Legendary",7 ,5)
        elif name_or_power == "goblin":
            CreatureCard("Goblin Warrior",2, "Common",2 ,1)
        return CreatureCard("Generic Minion", 1, "Common", 1, 1)
    
    def create_spell(self, name_or_power) -> Card:
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
                impact=f"Magic spell of type {spell_data['effect_type']}"
            )
        
        return SpellCard("Minor Magic", 1, "Common", "A simple magical spark")
        
    def create_artifact(self, name_or_power) -> Card:
        artifact_data = None
        self.mana_pool = 4

        
        for s in self.generator._artifacts:
            if s["name"].lower() == str(name_or_power).lower():
                artifact_data = s
                break

        if artifact_data:
            rarity_power ={
                    "Common": 5, 
                    "Uncommon": 10,
                    "Rare": 15,
                    "Legendary": 25
                }
            power = rarity_power.get(artifact_data["rarity"], 5)

            artifact= EliteCard(
                name=artifact_data["name"],
                cost=artifact_data["cost"],
                rarity=artifact_data["rarity"],
                attack=0,
                health=artifact_data.get("durability", 5),
                magic_power= power
            )
            artifact.mana_pool = 4
        generic_artifact = EliteCard("Ancient Relic", 1, "Common", 0, 5, 5)
        generic_artifact.mana_pool = 2
        return generic_artifact


    def create_themed_deck(self, size: int) -> dict
    def get_supported_types(self) -> dict
