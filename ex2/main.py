#!/usr/bin/env python3
from typing import List, Any, Dict
from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from tools.card_generator import CardGenerator


def get_methods(cls: Any) -> List[str]:
    # Retrieve public methods from a class for architecturel demonstration.
    return [m for m in dir(cls) if not m.startswith('_')]


def main() -> None:
    # Execute the demonstration of the EliteCard ability systen,

    # Initalize the generator provided in the project attachments
    generator: CardGenerator = CardGenerator()

    # Get base data from a sample creature to build our EliteCard
    # Using 'Ice Wizard' as a template for a magical-combat card
    sample_data: Dict[str, Any] = generator.get_creature("Ice Wizard")

    # Instantiate EliteCard using data from the tools/directory
    warrior: EliteCard = EliteCard(
            name="Arcane Warrior",
            cost=sample_data.get("cost", 5),
            rarity=sample_data.get("rarity", "Rare"),
            attack=sample_data.get("attack", 5),
            health=sample_data.get("health", 50),
            magic_power=15
        )

    # Initialize mana pool to match expected output baseline
    warrior.mana_pool = 4

    # Header and Architecture Inspecition using introspection
    print("=== DataDeck Ability System ===")
    print("")
    print("EliteCard capabilities: ")
    print(f"- Card: {get_methods(Card)}")
    print(f"- Combatable: {get_methods(Combatable)}")
    print(f"- Magical: {get_methods(Magical)}")

    print(f"\nPlaying {warrior.name} (Elite Card):")
    print("")

    # Combat phase demonstration (Contable interface)
    print("Combat phase: ")
    print(f"Attack result: {warrior.attack('Enemy')}")
    # Defense logic: damage taken vs damage blocked
    print(f"Defense result: {warrior.defend(5)}")
    print("")

    # Magic phase demonstration (Magical interface)
    print("Magic phase:")
    print(
        f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
