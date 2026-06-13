import os
from banner import show_banner
from code import generate_hashes

hash_menu = {
    "1": "md5",
    "2": "sha1",
    "3": "sha224",
    "4": "sha256",
    "5": "sha384",
    "6": "sha512",
    "7": "sha3_224",
    "8": "sha3_256",
    "9": "sha3_384",
    "10": "sha3_512",
    "11": "blake2s",
    "12": "blake2b",
    "13": "bcrypt",
    "14": "argon2",
    "15": "argon2i",
    "16": "argon2d",
    "17": "argon2id",
    "18": "scrypt",
    "19": "pbkdf2",
    "20": "ntlm",
    "21": "lm"
}

while True:
    os.system("cls" if os.name == "nt" else "clear")

    show_banner()

    text = input("\n[+] Enter Text (or 'exit'): ")

    if text.lower() == "exit":
        print("\n[!] Exiting Hash Generator...")
        break

    hashes = generate_hashes(text)

    print("\n\033[96m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                    HASH ALGORITHMS MENU                      ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    print("\033[92m[ MD FAMILY ]\033[0m")
    print("  [01] MD5")

    print("\n\033[94m[ SHA FAMILY ]\033[0m")
    print("  [02] SHA1")
    print("  [03] SHA224")
    print("  [04] SHA256")
    print("  [05] SHA384")
    print("  [06] SHA512")

    print("\n\033[95m[ SHA3 FAMILY ]\033[0m")
    print("  [07] SHA3_224")
    print("  [08] SHA3_256")
    print("  [09] SHA3_384")
    print("  [10] SHA3_512")

    print("\n\033[93m[ BLAKE FAMILY ]\033[0m")
    print("  [11] BLAKE2S")
    print("  [12] BLAKE2B")

    print("\n\033[91m[ PASSWORD HASHING ]\033[0m")
    print("  [13] BCRYPT")
    print("  [14] ARGON2")
    print("  [15] ARGON2I")
    print("  [16] ARGON2D")
    print("  [17] ARGON2ID")
    print("  [18] SCRYPT")
    print("  [19] PBKDF2")

    print("\n\033[96m[ WINDOWS HASHES ]\033[0m")
    print("  [20] NTLM")
    print("  [21] LM")

    print("\n" + "═" * 62)

    choice = input("\n[+] Select Hash Number: ").strip()

    if choice in hash_menu:
        algo = hash_menu[choice]

        print("\n\033[92m" + "═" * 70)
        print(f"{algo.upper()} HASH GENERATED")
        print("═" * 70 + "\033[0m")

        print("\n" + hashes[algo])

        print("\n\033[92m" + "═" * 70 + "\033[0m")

    else:
        print("\n\033[91m[-] Invalid Selection!\033[0m")

    input("\nPress Enter to continue...")