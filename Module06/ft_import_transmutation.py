import alchemy.elements
from alchemy.elements import create_fire
from alchemy.elements import create_water, create_earth
from alchemy.potions import healing_potion as heal, strength_potion


print("=== Import Transmutation Mastery ===\n")

print("Method 1 - Full module import:")
try:
    print(
        "alchemy.elements.create_fire(): "
        f"{alchemy.elements.create_fire()}"
    )
except AttributeError:
    print("alchemy.elements.create_fire(): AttributeError - not exposed")

print("\nMethod 2 - Specific function import:")
try:
    print(
        "create_water(): "
        f"{create_water()}"
    )
except AttributeError:
    print("alchemy.create_water(): AttributeError - not exposed")

print("\nMethod 3 - Aliased import:")
try:
    print(
        "heal(): "
        f"{heal()}"
    )
except AttributeError:
    print("Error")

print("\nMethod 4 - Multiple imports:")
try:
    print(
        "create_earth(): "
        f"{create_earth()}"
    )
    print(
        "create_fire(): "
        f"{create_fire()}"
    )
    print(
        "strength_potion(): "
        f"{strength_potion()}"
    )
except AttributeError:
    print("Error")

print("\nAll import transmutation methods mastered!")
