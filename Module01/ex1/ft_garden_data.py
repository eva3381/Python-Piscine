
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


plant1 = Plant("Rosa", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===")
print(f"{plant1.name.capitalize()}: {plant1.height}cm, {plant1.age} days old")
print(f"{plant2.name.capitalize()}: {plant2.height}cm, {plant2.age} days old")
print(f"{plant3.name.capitalize()}: {plant3.height}cm, {plant3.age} days old")
