
class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days


class Flower(Plant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        print(
            f"{self.name.capitalize()}(Flower): {self.height}cm, {self.days}"
            f" days, {self.color} color"
        )

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        print(
            f"{self.name.capitalize()}(Tree): {self.height}cm, {self.days}"
            f" days, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        radius = self.trunk_diameter // 10
        shadow = 31416 * radius ** 2
        print(
            f"{self.name.capitalize()} provides {shadow}"
            f" square meters of shade"
        )


class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season, nutritional_value):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(
            f"{self.name.capitalize()}(Vegetable): {self.height}cm,"
            f" {self.days} days, {self.harvest_season}cm harvest"
        )
        print(f"{self.name.capitalize()} is rich in {self.nutritional_value}")


print("=== Garden Plant Types ===")
print()
rose = Flower("Rose", 25, 30, "red")
rose.bloom()
print()
oak = Tree("Oak", 500, 1825, 50)
oak.produce_shade()
print()
tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
