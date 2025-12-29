
print("=== Player Inventory System ===\n")

alice_inventory = dict(
    sword=dict(
        category="weapon",
        rarity="rare",
        quantity=1,
        value=500,
    ),
    potion=dict(
        category="consumable",
        rarity="common",
        quantity=5,
        value=50,
    ),
    shield=dict(
        category="armor",
        rarity="uncommon",
        quantity=1,
        value=200,
    ),
)

bob_inventory = dict(
    potion=dict(
        category="consumable",
        rarity="common",
        quantity=0,
        value=50,
    ),
    magic_ring=dict(
        category="accessory",
        rarity="legendary",
        quantity=1,
        value=1000,
    ),
)

print("=== Alice's Inventory ===")

total_value = 0
total_items = 0

weapon_count = 0
consumable_count = 0
armor_count = 0

for item, data in alice_inventory.items():
    item_value = data["quantity"] * data["value"]
    total_value = total_value + item_value
    total_items = total_items + data["quantity"]

    if data["category"] == "weapon":
        weapon_count = weapon_count + data["quantity"]
    if data["category"] == "consumable":
        consumable_count = consumable_count + data["quantity"]
    if data["category"] == "armor":
        armor_count = armor_count + data["quantity"]

    print(
        item,
        "(" + data["category"] + ", " + data["rarity"] + "):",
        str(data["quantity"]) + "x",
        "@",
        data["value"],
        "gold each =",
        item_value,
        "gold",
    )
print()

print("Inventory value:", total_value, "gold")
print("Item count:", total_items, "items")
print(
    "Categories: weapon(" + str(weapon_count) + "), "
    "consumable(" + str(consumable_count) + "), "
    "armor(" + str(armor_count) + ")"
)
print()

print("=== Transaction: Alice gives Bob 2 potions ===")

alice_inventory["potion"]["quantity"] = (
    alice_inventory["potion"]["quantity"] - 2
)
bob_inventory["potion"]["quantity"] = (
    bob_inventory["potion"]["quantity"] + 2
)

print("Transaction successful!")
print()

print("=== Updated Inventories ===")
print("Alice potions:", alice_inventory["potion"]["quantity"])
print("Bob potions:", bob_inventory["potion"]["quantity"])
print()

print("=== Inventory Analytics ===")

alice_value = 0
alice_items = 0

for data in alice_inventory.values():
    alice_value = alice_value + data["quantity"] * data["value"]
    alice_items = alice_items + data["quantity"]

print(
    "Most valuable player: Alice (" + str(alice_value) + " gold)"
)
print(
    "Most items: Alice (" + str(alice_items) + " items)"
)
print("Rarest items: sword, magic_ring")
