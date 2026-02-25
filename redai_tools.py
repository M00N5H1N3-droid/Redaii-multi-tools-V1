#!/usr/bin/env python3
import os
import sys
import base64
import zlib
import time
import platform
import getpass

AUTHOR = "M00N5H1N3-droid"
PROFILE_LINK = "https://github.com/M00N5H1N3-droid"

def type_writer(text, speed=0.003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def fsociety_banner():
    os.system("clear" if os.name != "nt" else "cls")
    banner = f"""
██████╗ ███████╗██████╗  █████╗ ██╗██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██║
██████╔╝█████╗  ██║  ██║███████║██║██║
██╔══██╗██╔══╝  ██║  ██║██╔══██║██║██║
██║  ██║███████╗██████╔╝██║  ██║██║███████╗
╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝

          >>> Redai Tools <<<
          by {AUTHOR}

          Profile: {PROFILE_LINK}

          # fsociety
"""
    type_writer(banner, 0.001)

def whoami():
    print("\n=== WHOAMI ===\n")
    print("User      :", getpass.getuser())
    print("System    :", platform.system())
    print("Node      :", platform.node())
    print("Release   :", platform.release())
    print("Machine   :", platform.machine())
    print("Python    :", platform.python_version())
    print()

def obfuscate():
    print("\n=== PYTHON OBFUSCATOR ===\n")
    input_file = input("Input file (.py) : ").strip()
    output_file = input("Output file (.py): ").strip()

    if not os.path.exists(input_file):
        print("[-] File not found.")
        return

    with open(input_file, "rb") as f:
        original = f.read()

    compressed = zlib.compress(original)
    encoded = base64.b64encode(compressed)

    loader = f"""# Obfuscated with Redai Tools
# Author: {AUTHOR}

import base64,zlib
exec(zlib.decompress(base64.b64decode({encoded})))
"""

    with open(output_file, "w") as f:
        f.write(loader)

    print(f"[+] Obfuscated file created: {output_file}\n")

def main():
    while True:
        print("""
==========================
        Redai Tools
==========================

1) whoami
2) Python Obfuscator
3) fsociety banner
4) Exit
""")
        choice = input("Select option > ").strip()

        if choice == "1":
            whoami()
        elif choice == "2":
            obfuscate()
        elif choice == "3":
            fsociety_banner()
        elif choice == "4":
            print("Bye.")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
