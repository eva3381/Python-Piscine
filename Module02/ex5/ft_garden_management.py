
class GardenError(Exception):
    pass


class InvalidPlantError(Exception):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name, water_level=5, sunlight_hours=8):
        try:
            if not plant_name:
                raise InvalidPlantError("Plant name cannot be empty!")
            self.plants.append({
                "name": plant_name,
                "water": water_level,
                "sun": sunlight_hours
            })
            print(f"Added {plant_name} successfully")
        except InvalidPlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant["water"] < 1:
                    raise GardenError("Not enough water in tank")
                print(f"Watering {plant['name']} - success")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        for plant in self.plants:
            try:
                if plant["water"] < 1:
                    raise ValueError(f"Water level "
                                     f"{plant['water']} is too low (min 1)")
                if plant["water"] > 10:
                    raise ValueError(f"Water level "
                                     f"{plant['water']} is too high (max 10)")
                if plant["sun"] < 2:
                    raise ValueError(f"Sunlight hours "
                                     f"{plant['sun']} is too low (min 2)")
                if plant["sun"] > 12:
                    raise ValueError(f"Sunlight hours "
                                     f"{plant['sun']} is too high (max 12)")
                print(f"{plant['name']}: healthy (water: "
                      f"{plant['water']}, sun: {plant['sun']})")
            except ValueError as e:
                print(f"Error checking {plant['name']}: {e}")


def test_garden_management():
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    garden = GardenManager()
    garden.add_plant("tomato", 5, 8)
    garden.add_plant("lettuce", 15, 8)
    garden.add_plant("", 5, 8)
    print()

    print("Watering plants...")
    garden.water_plants()
    print()

    print("Checking plant health...")
    garden.check_health()
    print()

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
