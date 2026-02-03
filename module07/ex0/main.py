from ex0 import CreatureCard

game_state = {}
fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
print("=== DataDeck Card Foundation ===")
print()

print("CreatureCard Info:")
print(fire_dragon.get_card_info())
print()

print("Playing Fire Dragon with 6 mana available:")
print(f"Playable: {fire_dragon.is_playable(6)}")
print(f"Play result: {fire_dragon.play(game_state)}")
print()

print("Fire Dragon attacks Goblin Warrior:")
print(f"Attack result: {fire_dragon.attack_target("Goblin Warrior")}")
print()

print("Testing insufficient mana (3 available):")
print(f"Playable: {fire_dragon.is_playable(3)}")

print()

print("Abstract pattern successfully demonstrated!")
