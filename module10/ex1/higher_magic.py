

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Combines two distinct spells into a single simultaneous cast.

    Returns:
        A function that executes both spells and returns their results
        as a tuple.
    """
    def combined_spell(*args, **kwargs):
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        result = (res1, res2)
        return (result)
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Creates an amplified version of a numerical spell.

    Args:
        base_spell: The original spell function.
        multiplier: Factor to increase the spell's output.
    """
    def amplify(*args, **kwargs):
        result = base_spell(*args, **kwargs) * multiplier
        return (result)
    return amplify


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Wraps a spell with a logical requirement check before execution.

    Returns:
        The spell result if condition is met, otherwise 'Spell fizzled'.
    """
    def condition_cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return ("Spell fizzled")
    return condition_cast


def spell_sequence(spells: list[callable]) -> callable:
    def cast_spell(*args, **kwargs):
        results = [spell(*args, **kwargs) for spell in spells]
        return results
    return cast_spell


if __name__ == "__main__":
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def double_damage(n: int) -> int:
        return n * 2

    def is_powerful(n: int) -> bool:
        return n > 50

    print("--- Testing Exercise 1: Higher Realm ---")

    print("\n1. Testing Spell Combiner:")
    combo = spell_combiner(fireball, heal)
    print(f"Result: {combo('Dragon')}")

    print("\n2. Testing Power Amplifier:")
    mega_damage = power_amplifier(double_damage, 5)
    print(f"Result: {mega_damage(10)}")

    print("\n3. Testing Conditional Caster:")
    secure_spell = conditional_caster(is_powerful, double_damage)
    print(f"Condition True (60): {secure_spell(60)}")
    print(f"Condition False (30): {secure_spell(30)}")

    print("\n4. Testing Spell Sequence:")
    sequence = spell_sequence([fireball, heal, lambda t: f"Buffs {t}"])

    print(f"Result: {sequence('Hero')}")
