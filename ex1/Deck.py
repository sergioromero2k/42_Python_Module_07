#!/usr/bin/env python3

import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard

"""Module for managing a collection of game cards as a Deck."""


class Deck:
    def __init__(self) -> None:
        # Initialize an empty list to store card objects
        self.cards = []

    def add_card(self, card: Card) -> None:
        # Append a new card to the deck collection
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        # Find and remove a card by name, returning success status
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        # Randomize the order of cards in the deck
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        # Remove and return the top card if available
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        # Calculate totals and average costs for the current deck
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1

        total_cards = len(self.cards)
        # Avoid division by zero and calculate cost average
        if total_cards > 0:
            avg_cost = total_cost / total_cards
        else:
            avg_cost = 0.0

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
