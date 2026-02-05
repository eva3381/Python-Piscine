def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]

    for ing in ingredients.split():
        if ing in valid_ingredients:
            return f"{ing} - VALID"
    return f"{ingredients} - INVALID"
