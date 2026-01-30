"""
Achievement Tracker System Module.
This script manages player achievements using Python Sets. It demonstrates 
how to perform set operations like union, intersection, and difference 
to find commonalities and unique items across multiple players.
"""

print("=== Achievement Tracker System ===\n")

alice = set(
    [
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    ]
)

bob = set(
    [
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    ]
)

charlie = set(
    [
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    ]
)

print("Player alice achievements:", alice)
print("Player bob achievements:", bob)
print("Player charlie achievements:", charlie)
print()

print("=== Achievement Analytics ===")

all_achievements = alice.union(bob).union(charlie)
print("All unique achievements:", all_achievements)
print("Total unique achievements:", len(all_achievements))
print()

common_all = alice.intersection(bob).intersection(charlie)
print("Common to all players:", common_all)

rare = all_achievements.difference(
    alice.intersection(bob)
    .union(alice.intersection(charlie))
    .union(bob.intersection(charlie))
)
print("Rare achievements (1 player):", rare)
print()

alice_bob_common = alice.intersection(bob)
print("Alice vs Bob common:", alice_bob_common)

alice_unique = alice.difference(bob)
print("Alice unique:", alice_unique)

bob_unique = bob.difference(alice)
print("Bob unique:", bob_unique)
