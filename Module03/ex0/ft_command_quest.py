
import sys


def main():
    print("=== Command Quest ===")
    argc = len(sys.argv)

    # Caso sin argumentos adicionales
    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {argc}")
        return

    # Caso con argumentos
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {argc - 1}")

    # Imprimir argumentos uno por uno
    idx = 1
    while idx < argc:
        print(f"Argument {idx}: {sys.argv[idx]}")
        idx += 1

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
