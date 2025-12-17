
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.kind = "regular"

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True
        self.kind = "flowering"

    def info(self):
        state = "blooming" if self.blooming else "not blooming"
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers ({state})"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points
        self.kind = "prize"

    def info(self):
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.points}"
        )


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.plant_count = 0
        self.total_growth = 0

    def add(self, plant):
        self.plants.append(plant)
        self.plant_count += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if plant.kind == "regular":
                print(f"- {plant.name}: {plant.height}cm")
            else:
                print(f"- {plant.info()}")


class GardenManager:
    garden_total = 0

    class GardenStats:
        @staticmethod
        def count_types(plants):
            regular = 0
            flowering = 0
            prize = 0

            for plant in plants:
                if plant.kind == "regular":
                    regular += 1
                elif plant.kind == "flowering":
                    flowering += 1
                else:
                    prize += 1

            return regular, flowering, prize

        @staticmethod
        def validate_heights(plants):
            for plant in plants:
                if plant.height <= 0:
                    return False
            return True

        @staticmethod
        def score(plants):
            total = 0
            for plant in plants:
                total += plant.height
                if plant.kind == "prize":
                    total += plant.points
            return total

    def __init__(self):
        self.gardens = {}

    def add_garden(self, garden):
        self.gardens[garden.owner] = garden
        GardenManager.garden_total += 1

    @classmethod
    def create_garden_network(cls):
        return cls()

    def analytics(self, owner):
        garden = self.gardens[owner]
        r, f, p = self.GardenStats.count_types(garden.plants)

        print(
            f"Plants added: {garden.plant_count}, "
            f"Total growth: {garden.total_growth}cm"
        )
        print(
            f"Plant types: {r} regular, "
            f"{f} flowering, {p} prize flowers"
        )
        print(
            f"Height validation test: "
            f"{self.GardenStats.validate_heights(garden.plants)}"
        )

    def scores(self):
        alice = self.gardens["Alice"]
        bob = self.gardens["Bob"]

        print(
            "Garden scores - Alice:",
            self.GardenStats.score(alice.plants),
            ", Bob:",
            self.GardenStats.score(bob.plants),
        )
        print("Total gardens managed:", GardenManager.garden_total)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network()

    alice = Garden("Alice")
    bob = Garden("Bob")

    manager.add_garden(alice)
    manager.add_garden(bob)

    alice.add(Plant("Oak Tree", 100))
    alice.add(FloweringPlant("Rose", 25, "red"))
    alice.add(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice.grow_all()
    alice.report()
    manager.analytics("Alice")

    bob.add(Plant("Cactus", 92))

    manager.scores()
