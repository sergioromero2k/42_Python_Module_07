#!/usr/bin/env python3

"""
Execution script to demonstrate the Foundation Layer architecture
"""
from ex0.CreatureCard import CreatureCard


def main() -> None:
    # Header display as required by the exercise
    print("=== DataDeck Card Foundation ===")
    print("")

    print("Testing Abstract Base Class Design:")
    print("")

    print("CreatureCard Info:")
    # Instantiate the concrete CreatureCard
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(creature.get_card_info())
    print("")

    # Test mana validatio nand play mechanics (Success case)
    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", creature.is_playable(6))
    print("Play result:", creature.play({"mana": 6}))
    print("")

    # Demonstrate specific CreatureCard behavior
    print("Fire Dragon attacks Goblin Warrior:")
    print("Attack result:", creature.attack_target("Goblin Warrior"))
    print("")

    # Test mana validation (Failure case)
    print("Testing insufficient mana (3 available):")
    print("Playable:", creature.is_playable(3))
    print("")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
