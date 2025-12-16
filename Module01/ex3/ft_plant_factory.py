
class Plant:
    count = 0

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


plant1 = Plant("Rose", 25, 30),
plant2 = Plant("Oak", 200, 365),
plant3 = Plant("Cactus", 5, 90),
plant4 = Plant("Sunflower", 80, 45),
plant5 = Plant("Fern", 15, 120)
print(f"Total plants created: {Plant.count}")
