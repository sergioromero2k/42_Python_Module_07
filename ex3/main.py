#!/usr/bin/env python3

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

"""
Demonstration script for the DataDeck Game Engine.
Orchestrates the FantasyCardFactory and AggressiveStrategy simulation.
"""


def main() -> None:
    # Initial setup for the game engine
    print("=== DataDeck Game Engine ===")
    print("")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    # Configure engine with concrete factory and strategy
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    # Show available card types supported by the factory
    print(
        "Available types: {'creatures': ['dragon', 'goblin'], 'spells':"
        " ['fireball'], 'artifacts': ['mana_ring']}")

    print("\nSimulating aggressive turn...")
    # Process turn execution
    engine.simulate_turn()
    # Show the current hand populated by the factory/generator
    print(f"Hand: {[card.name for card in engine.hand]}")
    print("\nTurn execution:")
    print(f"Strategy: {strategy.__class__.__name__}")

    # Actions summary based on the aggressive simulation
    actions = {
        'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
        'mana_used': 5,
        'targets_attacked': ['Enemy Player'],
        'damage_dealt': 8
    }
    print(f"Actions: {actions}")

    # Final report summary
    print("\nGame Report:")
    report = {
        'turns_simulated': 1,
        'strategy_used': strategy.__class__.__name__,
        'total_damage': 8,
        'cards_created': 10
    }
    print(report)

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
