
class Plant:
    count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.set_height = height
        self.set_age = age
        Plant.count += 1
        print(f"Plant Created: {self.name}")

    @property
    def get_height(self):
        return self._height

    @get_height.setter
    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_info(self):
        print(
            f"Current plant: {self.name} ({self._height}cm, {self._age} days)"
        )
