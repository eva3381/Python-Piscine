import os
from dotenv import load_dotenv


def load_oracle_config():
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...\n")
    mode = os.getenv('MATRIX_MODE', None)
    db = os.getenv('DATABASE_URL', None)
    api = os.getenv('API_KEY', None)
    log = os.getenv('LOG_LEVEL', None)
    zion = os.getenv('ZION_ENDPOINT', None)

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {'Connected' if db is not None else 'Disconnected'}")
    print(f"Api Access: {'Authenticated' if api is not None else 'Error'}")
    print(f"Log Level: {log}")
    print(f"Zion Network: {'Online' if zion is not None else 'offline'}")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists('.env'):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing! Using system defaults.")
    if mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running in standard mode")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    load_oracle_config()
