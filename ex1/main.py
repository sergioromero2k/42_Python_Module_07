#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck

"""Execution script to demonstrate deck building and polymorphism."""


def main() -> None:
    # Display header for the deck builder demonstration
    print("=== DataDeck Deck Builder ===")
    print("")

    # Initialize deck and add various card types to test stats
    # Costs (5, 4, 3) are chosen to result in an average of 4.0
    deck = Deck()
    deck.add_card(SpellCard("Lightning Bolt", 5, "Normal", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 4, "Normal", 1, "mana"))
    deck.add_card(CreatureCard("Fire Dragon", 3, "Legendary", 7, 5))

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("")

    print("Drawing and playing cards:")
    print("")

    # Demonstrate drawing and playing the first card (Spell)
    card1 = deck.draw_card()
    if card1:
        print(f"Drew: {card1.name} (Spell)")
        print(f"Play result: {card1.play({})}")
        print("")

    # Demonstrate drawing and playing the second card (Artifact)
    card2 = deck.draw_card()
    if card2:
        print(f"Drew: {card2.name} (Artifact)")
        print(f"Play result: {card2.play({})}")
        print("")

    # Demonstrate drawing and playing the third card (Creature)
    card3 = deck.draw_card()
    if card3:
        print(f"Drew: {card3.name} (Creature)")
        print(f"Play result: {card3.play({})}")
        print("")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
