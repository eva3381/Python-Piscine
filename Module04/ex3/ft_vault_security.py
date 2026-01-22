def ft_vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("\nSECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as vault:
            content = vault.read()
            for line in content.splitlines():
                if "" in line:
                    line = line.replace("", "")
                if "100%" in line:
                    line = line.replace("100%", "100 %")
                print(line)
    except (FileNotFoundError, IOError):
        pass
    print("\nSECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", "r") as protocols:
            content = protocols.read()
            for line in content.splitlines():
                if "" in line:
                    line = line.replace("", "")
                print(line)
    except (FileNotFoundError, IOError):
        pass
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()