print("=== Player Inventory System ===")

game_inventory = {
    "players": {
        "alice": {
            "items": {
                "sword": 1,
                "potion": 5,
                "shield": 1,
                "magic_ring": 1,
            },
            "total_value": 1950,
            "item_count": 7,
        },
        "bob": {
            "items": { 
                "sword": 1,
                "potion": 0,
                "shield": 2,
                "magic_ring": 3,},
            "total_value": 3900,
            "item_count": 6,
        },
    },
    "catalog": {
        "sword": {"type": "weapon", "value": 500, "rarity": "rare"},
        "magic_ring": {"type": "accessory", "value": 1000, "rarity": "legendary"},
        "potion": {"type": "consumable", "value": 50, "rarity": "common"},
        "shield": {"type": "armor", "value": 200, "rarity": "uncommon"},
    },
}


def print_inventory(player_name):
    player_items = game_inventory["players"][player_name]["items"]
    catalog = game_inventory["catalog"]
    total_value = 0
    total_items = 0
    weapon_count = 0
    consumable_count = 0
    armor_count = 0
    print(f"=== {player_name.capitalize()}'s Inventory ===")
    for item, qty in player_items.items():
        value = catalog[item]["value"]
        category = catalog[item]["type"]
        rarity = catalog[item]["rarity"]
        total = value * qty
        total_value += total
        total_items += qty
        if category == "weapon":
            weapon_count += qty
        elif category == "consumable":
            consumable_count += qty
        elif category == "armor":
            armor_count += qty
        print(f"{item} ({category}, {rarity}): {qty}x @ {value} gold each = {total} gold")
    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print(f"Categories: weapon({weapon_count}), consumable({consumable_count}), armor({armor_count})")


def transfer_item(sender, receiver, item_name, amount):
    sender_items = game_inventory["players"][sender]["items"]
    receiver_items = game_inventory["players"][receiver]["items"]
    print(f"=== Transaction: {sender.capitalize()} gives {receiver.capitalize()} {amount} {item_name}s ===")
    if sender_items.get(item_name, 0) < amount:
        print("failure transaction!")
        return
    sender_items[item_name] -= amount
    receiver_items[item_name] = receiver_items.get(item_name, 0) + amount
    print("Transaction successful!")


def inventory_analytics():
    max_value = 0
    max_items = 0
    valuable_player = ""
    items_player = ""
    all_items = []
    catalog = game_inventory["catalog"]
    for player, data in game_inventory["players"].items():
        value = sum(catalog[item]["value"] * qty for item, qty in data["items"].items())
        if value > max_value:
            max_value = value
            valuable_player = player
        count = sum(data["items"].values())
        if count > max_items:
            max_items = count
            items_player = player
        all_items.extend(data["items"].keys())
    rare_items = []
    max_rarity = {"common": 1, "uncommon": 2, "rare": 3, "legendary": 4}
    highest = 0
    for item in set(all_items):
        rarity_score = max_rarity[catalog[item]["rarity"]]
        if rarity_score > highest:
            highest = rarity_score
            rare_items = [item]
        elif rarity_score == highest:
            rare_items.append(item)
    print("=== Inventory Analytics ===")
    print(f"Most valuable player: {valuable_player.capitalize()} ({max_value} gold)")
    print(f"Most items: {items_player.capitalize()} ({max_items} items)")
    print(f"Rarest items: {', '.join(rare_items)}")


print_inventory("alice")
transfer_item("alice", "bob", "potion", 2)
print("=== Updated Inventories ===")
print(f"Alice potions: {game_inventory['players']['alice']['items'].get('potion',0)}")
print(f"Bob potions: {game_inventory['players']['bob']['items'].get('potion',0)}")
inventory_analytics()
