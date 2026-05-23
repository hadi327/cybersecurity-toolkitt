import socket
import hashlib
import requests
import re
import os
import threading
import subprocess
import time
import json
from datetime import datetime

from colorama import Fore, Style, init
try:
    import whois
except:
    whois = None
init(autoreset=True)
scan_results = []
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def pause():
    input("\nPress Enter to continue...")
def hacker_intro():
    clear()
    intro = [
        "Initializing toolkit...",
        "Loading modules...",
        "Bypassing firewalls...",
        "Accessing secure protocols...",
        "Toolkit ready..."
    ]
    for line in intro:
        print(Fore.GREEN + line)
        time.sleep(0.5)

    time.sleep(1)
    clear()
def save_logs():
    filename = f"scan_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        for item in scan_results:
            file.write(item + "\n")
    print(Fore.CYAN + f"\nLogs saved to {filename}")
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            output = f"[OPEN] Port {port}"
            print(Fore.GREEN + output)
            scan_results.append(output)

        s.close()

    except:
        pass


def port_scanner():
    clear()

    target = input("Enter target IP/domain: ")

    start = int(input("Start Port: "))
    end = int(input("End Port: "))

    print(Fore.YELLOW + f"\nScanning {target}...\n")

    threads = []

    for port in range(start, end + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Fore.CYAN + "\nScan completed.")

    pause()
def password_checker():
    clear()

    password = input("Enter password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*()]", password):
        score += 1

    print()

    if score == 5:
        print(Fore.GREEN + "Very Strong Password")

    elif score >= 3:
        print(Fore.YELLOW + "Moderate Password")

    else:
        print(Fore.RED + "Weak Password")

    pause()
def hash_generator():
    clear()

    text = input("Enter text: ")

    print("\n1. MD5")
    print("2. SHA1")
    print("3. SHA256")

    choice = input("\nSelect: ")

    if choice == "1":
        result = hashlib.md5(text.encode()).hexdigest()

    elif choice == "2":
        result = hashlib.sha1(text.encode()).hexdigest()

    elif choice == "3":
        result = hashlib.sha256(text.encode()).hexdigest()

    else:
        print("Invalid choice")
        pause()
        return

    print(Fore.CYAN + f"\nHash:\n{result}")

    pause()
def network_info():
    clear()

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(Fore.GREEN + "=== NETWORK INFO ===\n")

    print(f"Hostname : {hostname}")
    print(f"Local IP : {local_ip}")

    try:
        public_ip = requests.get("https://api.ipify.org").text
        print(f"Public IP: {public_ip}")

    except:
        print("Could not fetch public IP")

    pause()
def whois_lookup():
    clear()

    if whois is None:
        print("python-whois not installed.")
        pause()
        return

    domain = input("Enter domain: ")

    try:
        info = whois.whois(domain)

        print(Fore.CYAN + "\nWHOIS INFO:\n")
        print(info)

    except:
        print("Failed WHOIS lookup.")

    pause()
def subdomain_scanner():
    clear()

    domain = input("Enter domain: ")

    subdomains = ["www", "mail", "ftp", "admin", "blog", "api"]

    print()

    for sub in subdomains:
        url = f"{sub}.{domain}"

        try:
            socket.gethostbyname(url)
            print(Fore.GREEN + f"[FOUND] {url}")

        except:
            pass

    pause()
def ping_sweeper():
    clear()

    base_ip = input("Enter base IP (example 192.168.1): ")

    print()

    for i in range(1, 10):

        ip = f"{base_ip}.{i}"

        response = os.system(f"ping -n 1 {ip} > nul" if os.name == "nt"
                             else f"ping -c 1 {ip} > /dev/null")

        if response == 0:
            print(Fore.GREEN + f"{ip} is ONLINE")

    pause()
def url_checker():
    clear()

    url = input("Enter URL: ")

    try:
        response = requests.get(url)

        print(Fore.CYAN + f"\nStatus Code: {response.status_code}")

    except:
        print(Fore.RED + "Could not connect.")

    pause()
def file_hash_checker():
    clear()

    path = input("Enter file path: ")

    try:
        with open(path, "rb") as file:
            data = file.read()

            sha256 = hashlib.sha256(data).hexdigest()

            print(Fore.GREEN + f"\nSHA256:\n{sha256}")

    except:
        print("File not found.")

    pause()
def export_json():
    clear()

    filename = "results.json"

    with open(filename, "w") as file:
        json.dump(scan_results, file, indent=4)

    print(Fore.CYAN + f"\nExported to {filename}")

    pause()
def main():

    hacker_intro()

    while True:

        clear()

        print(Fore.GREEN + """
========================================
      ADVANCED CYBER TOOLKIT
========================================
1. Port Scanner
2. Password Strength Checker
3. Hash Generator
4. Network Info Viewer
5. WHOIS Lookup
6. Subdomain Scanner
7. Ping Sweeper
8. URL Status Checker
9. File Hash Checker
10. Save Logs
11. Export JSON
12. Exit
========================================
""")

        choice = input("Select option: ")

        if choice == "1":
            port_scanner()

        elif choice == "2":
            password_checker()

        elif choice == "3":
            hash_generator()

        elif choice == "4":
            network_info()

        elif choice == "5":
            whois_lookup()

        elif choice == "6":
            subdomain_scanner()

        elif choice == "7":
            ping_sweeper()

        elif choice == "8":
            url_checker()

        elif choice == "9":
            file_hash_checker()

        elif choice == "10":
            save_logs()
            pause()

        elif choice == "11":
            export_json()

        elif choice == "12":
            print(Fore.RED + "\nExiting Toolkit...")
            break

        else:
            print(Fore.RED + "\nInvalid option.")
            pause()

if __name__ == "__main__":
    main()