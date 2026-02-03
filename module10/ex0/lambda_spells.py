

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sort_lambda = sorted(
        artifacts, key=lambda item: item['power'], reverse=True)
    return (sort_lambda)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filter_lambda = list(filter(
        lambda minimus: minimus['power'] >= min_power, mages))
    return (filter_lambda)


def spell_transformer(spells: list[str]) -> list[str]:
    map_lambda = list(map(lambda name: "* " + name + " *", spells))
    return (map_lambda)


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    max_lambda = max(powers)
    min_lambda = min(powers)
    avg_lambda = round(sum(powers) / len(powers), 2)
    result = {
        'max_power': max_lambda,
        'min_power': min_lambda,
        'avg_power': avg_lambda
    }
    return (result)


artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'}
    ]

mages = [
    {'name': 'Ember', 'power': 92, 'element': 'fire'},
    {'name': 'Storm', 'power': 55, 'element': 'lightning'},
    {'name': 'Nova', 'power': 78, 'element': 'light'},
    {'name': 'Sage', 'power': 95, 'element': 'wind'},
    {'name': 'Kai', 'power': 61, 'element': 'water'}
]

spells = ['fireball', 'heal', 'shield']

if __name__ == "__main__":
    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    if len(sorted_arts) >= 2:
        print(
            f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
            f"comes before {sorted_arts[1]['name']} "
            f"({sorted_arts[1]['power']} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\n---Power Filter (min=80) ---")
    print(power_filter(mages, 80))

    print("\n---Mage Stats ---")
    print(mage_stats(mages))
