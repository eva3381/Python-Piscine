from .elements import create_fire, create_water, create_earth, create_air


fire = create_fire()
water = create_water()
earth = create_earth()
air = create_air()


def healing_potion() -> str:
    return (f"Healing potion brewed with {fire} and {water}")


def strength_potion() -> str:
    return (f"Healing potion brewed with {fire} and {water}")


def invisibility_potion() -> str:
    return (f"nvisibility potion brewed with {air} and {water}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: {air}, {water}")
