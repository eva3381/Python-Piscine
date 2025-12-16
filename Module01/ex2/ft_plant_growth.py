
class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1


plant1 = Plant("Rosa", 25, 30)
initheight = plant1.height
print("=== Day 1 ===")
print(f"{plant1.name.capitalize()}: {plant1.height}cm, {plant1.days} days old")
i = 1
while i < 7:
    plant1.grow()
    plant1.age()
    i += 1
print(f"=== Day {i} ===")
print(f"{plant1.name.capitalize()}: {plant1.height}cm, {plant1.days} days old")
growth = plant1.height - initheight
print(f"Growth this week: +{growth}cm")
