def garden_operations(mode):
    try:
        if mode == "value":
            int("abc")

        if mode == "zero":
            10 / 0

        if mode == "file":
            open("missing.txt")

        if mode == "key":
            data = {}
            data["missing_plant"]

    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    garden_operations("value")

    print("Testing ZeroDivisionError...")
    garden_operations("zero")

    print("Testing FileNotFoundError...")
    garden_operations("file")

    print("Testing KeyError...")
    garden_operations("key")

    print("Testing multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!\n")


test_error_types()
