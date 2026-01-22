def ft_crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    files = ["lost_archive.txt", "classified_vault.txt", "standard_archive.txt"]
    for name in files:
        if name == "standard_archive.txt":
            print(f"\nROUTINE ACCESS: Attempting access to '{name}'...")
        else:
            print(f"\nCRISIS ALERT: Attempting access to '{name}'...")
        try:
            with open(name, "r") as file:
                content = file.read().replace("\n", "")
                print(f"SUCCESS: Archive recovered - ``{content}''")
                print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except Exception:
            print("RESPONSE: Unexpected system anomaly")
            print("STATUS: Emergency protocols active")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()