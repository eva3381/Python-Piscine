
class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print("Caught PlantError:", error, "\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print("Caught WaterError:", error, "\n")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print("Caught a garden error:", error)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print("Caught a garden error:", error, "\n")

    print("All custom error types work correctly!\n")


test_custom_errors()
