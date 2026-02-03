import sys
import site
import os


def verify_venv():
    """
    Analiza el entorno de ejecución para determinar si estamos dentro
    del entorno virtual o todavía conectados a la 'Matrix' (entorno global).
    """
    try:
        en_venv = sys.prefix != sys.base_prefix

        path_packages = site.getsitepackages([sys.prefix])

        if en_venv:
            print("MATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}\n")

            print("SUCCESS: You're in an isolated environment!")
            print(
                "Safe to install packages without affecting "
                "the global system.\n")

            print("Package installation path (Isolated):")
            print(f"-> {path_packages[0]}")
        else:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")

            print("WARNING: You're in the global environment!")
            print(
                "The machines can see everything you install. "
                "This risks corrupting")
            print("the core architecture of your system.\n")

            print("To enter the construct and isolate your data, run:")
            print("-" * 40)
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate  # On Unix/macOS")
            print("matrix_env\\Scripts\\activate     # On Windows")
            print("-" * 40)
            print("\nThen run this program again to verify your connection.")

    except Exception as e:
        print(f"ERROR: A glitch in the Matrix occurred: {e}")


if __name__ == "__main__":
    verify_venv()
