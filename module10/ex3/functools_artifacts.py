from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    signals = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }
    result = reduce(signals[operation], spells)
    return (result)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, 50, "fire"),
        'ice_enchant': partial(base_enchantment, 50, "ice"),
        'lightning_enchant': partial(base_enchantment, 50, "lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatcher(value: int):
        return "Unknow spell type"

    @dispatcher.register(int)
    def _(spell: int):
        return f"Damage spell: {spell} HP"

    @dispatcher.register(str)
    def _(spell: str):
        return f"Enchantment : {spell}"

    @dispatcher.register(list)
    def _(spell: list):
        return f"Multi-cast: {len(spell)} spells"
    return dispatcher


if __name__ == "__main__":
    print("--- Testing Exercise 3: Ancient Library ---")

    powers = [10, 5, 20, 8]
    print(f"Reducer Max: {spell_reducer(powers, 'max')}")
    print(f"Reducer Add: {spell_reducer(powers, 'add')}")

    def base_spell(power, element, target):
        return f"Casting {element} ({power} power) on {target}"

    factory = partial_enchanter(base_spell)
    print(factory['ice_enchant']("Frost Giant"))

    print(f"Fibonacci(50): {memoized_fibonacci(50)}")

    cast = spell_dispatcher()
    print(cast(150))
    print(cast("Invisibility"))
    print(cast([1, 2, 3, 4]))
