import sys

def main():
    """
    Main entry point that parses command-line arguments. It calculates 
    the total number of parameters and displays each one with its index.
    """
    print("=== Command Quest ===")
    argc = len(sys.argv)

    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {argc}")
        return

    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {argc - 1}")

    idx = 1
    while idx < argc:
        print(f"Argument {idx}: {sys.argv[idx]}")
        idx += 1

    print(f"Total arguments: {argc}")

if __name__ == "__main__":
    main()
