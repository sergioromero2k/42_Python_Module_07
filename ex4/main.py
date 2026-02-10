#!/usr/bin/env python3

from tools.card_generator import CardGenerator
from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    """Display header for the tournament demonstration"""
    print("=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")

    # Retrieve predefined creature card data
    generator = CardGenerator()
    platform = TournamentPlatform()

    # Retrieve predefined creature card data
    fire_dragon_data = generator.get_creature("Fire Dragon")
    ice_wizard_data = generator.get_creature("Ice Wizard")

    # Create TournamentCard instances for each creature
    fire_dragon_card = TournamentCard(
        name=fire_dragon_data["name"],
        cost=fire_dragon_data["cost"],
        rarity=fire_dragon_data["rarity"],
        card_id="dragon_001",  # Assign a unique card ID
        attack_power=fire_dragon_data["attack"],
        health=fire_dragon_data["health"],
        wins=0,
        losses=0,
        rating=1000,  # Initial rating
    )

    ice_wizard_card = TournamentCard(
        name=ice_wizard_data["name"],
        cost=ice_wizard_data["cost"],
        rarity=ice_wizard_data["rarity"],
        card_id="wizard_001",  # Assign a unique card ID
        attack_power=ice_wizard_data["attack"],
        health=ice_wizard_data["health"],
        wins=0,
        losses=0,
        rating=1000,
    )

    # Register the cards in the tournament platform and display info
    for card in [fire_dragon_card, ice_wizard_card]:
        platform.register_card(card)
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.calculate_rating()}")
        print(f"- Record: {card.wins}-{card.losses}\n")

    # Create a match between the two registered cards
    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    # Display the leaderboard after the match
    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        print(
            f"{i}. {entry['name']} - Rating: {entry['rating']} "
            f"({entry['wins']}-{entry['losses']})"
        )

    # Generate and display an overall platform report
    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    # Final success message
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
