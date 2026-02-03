import alchemy.elements
from alchemy import create_fire, create_water, __version__
from alchemy import __author__

print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")
fire = alchemy.elements.create_fire()
water = alchemy.elements.create_water()
air = alchemy.elements.create_air()
earth = alchemy.elements.create_earth()

print(f"alchemy.elements.create_fire(): {fire}")
print(f"alchemy.elements.create_water(): {water}")
print(f"alchemy.elements.create_earth(): {earth}")
print(f"alchemy.elements.create_air(): {air}")

print()

print("Testing package-level access (controlled by __init__.py):")

init_fire = create_fire()
init_water = create_water()
print(f"alchemy.create_fire(): {init_fire}")
print(f"alchemy.create_water(): {init_water}")
try:
    init_earth = alchemy.create_earth()
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")
try:
    init_air = alchemy.create_air()
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")

print()

print("Package metadata:")
print(f"Version: {__version__} ")
print(f"Author: {__author__}")
