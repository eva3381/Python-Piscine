
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    Seed_type = seed_type.capitalize()
    if unit == "packets":
        print(f"{Seed_type} seeds:{quantity} packets available")
    elif unit == "grams":
        print(f"{Seed_type} seeds:{quantity} grams total")
    elif unit == "area":
        print(f"{Seed_type} seeds: covers {quantity} square meters")
