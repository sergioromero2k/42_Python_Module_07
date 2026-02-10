#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from tools.card_generator import CardGenerator

"""Execution script to demonstrate deck building using CardGenerator."""


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    # Initialize card generator
    generator = CardGenerator()

    # Retrieve card data from generator
    creature_data = generator.get_creature("Fire Dragon")
    spell_data = generator.get_spell("Lightning Bolt")
    artifact_data = generator.get_artifact("Mana Crystal")

    # Instantiate concrete card objects
    creature_card = CreatureCard(
        creature_data["name"],
        creature_data["cost"],
        creature_data["rarity"],
        creature_data["attack"],
        creature_data["health"]
    )

    spell_card = SpellCard(
        spell_data["name"],
        spell_data["cost"],
        spell_data["rarity"],
        spell_data["effect_type"]
    )

    artifact_card = ArtifactCard(
        artifact_data["name"],
        artifact_data["cost"],
        artifact_data["rarity"],
        artifact_data["durability"],
        artifact_data["effect"]
    )

    # Build deck and add cards
    deck = Deck()
    for card in [spell_card, artifact_card, creature_card]:
        deck.add_card(card)

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")
    while deck.get_deck_stats()["total_cards"] > 0:
        card = deck.draw_card()
        if card is None:
            break

        # Determine card type dynamically
        type_name = "Creature"
        if isinstance(card, SpellCard):
            type_name = "Spell"
        elif isinstance(card, ArtifactCard):
            type_name = "Artifact"

        # Print drawn card and play result
        print(f"Drew: {card.name} ({type_name})")
        print(f"Play result: {card.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
