import functools
import time


def spell_timer(func: callable) -> callable:
    """Instruments a spell with high-precision execution timing."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """Enforces power level security protocols on decorated spells."""
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) > 2:
                power = args[2]
            else:
                power = args[0]

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """
    Añade una capa de resiliencia, reintentando el hechizo si la magia falla.
    """
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validates if a mage's name meets the guild's linguistic standards.
        """
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        Executes a spell cast after passing all security and power validations.
        """
        return f"Successfully cast {spell_name} with power {power}"


@spell_timer
def fireball():
    """Un hechizo básico que toma un poco de tiempo."""
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_portal(should_fail=True):
    """Un hechizo que falla intencionalmente para probar la resiliencia."""
    if should_fail:
        raise Exception("Mana leak detected!")
    return "Portal opened successfully!"


def main():
    print("--- 1. Probando spell_timer ---")
    result = fireball()
    print(f"Result: {result}\n")

    print("--- 2. Probando retry_spell ---")
    # Probamos la capacidad de recuperación ante fallos del gremio.
    print("Intentando abrir un portal inestable...")
    failed_portal = unstable_portal(should_fail=True)
    print(f"Final Outcome: {failed_portal}\n")

    print("--- 3. Probando MageGuild (staticmethod y power_validator) ---")
    guild = MageGuild()

    names = ["Al", "Gandalf the Grey", "M4g3"]
    for name in names:
        is_valid = MageGuild.validate_mage_name(name)
        print(f"Is '{name}' a valid mage name? {is_valid}")

    print("\nLanzando hechizos desde el gremio:")
    print(guild.cast_spell("Lightning Bolt", 15))
    print(guild.cast_spell("Small Spark", 5))


if __name__ == "__main__":
    main()
