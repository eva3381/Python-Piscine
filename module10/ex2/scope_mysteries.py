def mage_counter() -> callable:
    count = 0

    def m_counter():
        nonlocal count
        count += 1
        return count
    return m_counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def power(add_power: int):
        nonlocal total_power
        total_power += add_power
        return total_power
    return power


def enchantment_factory(enchantment_type: str) -> callable:
    def enchantment(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(**kwargs):
        nonlocal memory
        memory.update(kwargs)
        return "Stored successfully"

    def recall(key: str):
        nonlocal memory
        return memory.get(key, "Memory not found")
    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    print("--- Testing Exercise 2: Memory Depths ---")

    print("\n1. Mage Counter:")
    c1 = mage_counter()
    print(f"Mage ID: {c1()}")
    print(f"Mage ID: {c1()}")

    print("\n2. Spell Accumulator:")
    acc = spell_accumulator(100)
    print(f"Total Power: {acc(50)}")
    print(f"Total Power: {acc(25)}")

    print("\n3. Enchantment Factory:")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))

    print("\n4. Memory Vault:")
    vault = memory_vault()
    vault['store'](fireball="A ball of fire", shield="Magic protection")
    print(f"Recall fireball: {vault['recall']('fireball')}")
    print(f"Recall fly: {vault['recall']('fly')}")
