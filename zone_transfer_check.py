import subprocess
import sys
import os

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

def banner():
    os.system("clear")
    print(f"""{CYAN}
╔══════════════════════════════════════════════╗
║              AXFR ZONE SCANNER              ║
╚══════════════════════════════════════════════╝
{RESET}""")

def get_nameservers(domain):
    try:
        result = subprocess.check_output(["dig", "ns", domain, "+short"], stderr=subprocess.STDOUT)
        nameservers = result.decode().strip().split("\n")
        return [ns.strip('.') for ns in nameservers if ns]
    except subprocess.CalledProcessError:
        print(f"{RED}[!] Error retrieving NS records.{RESET}")
        return []

def try_zone_transfer(domain, nameserver):
    print(f"\n{YELLOW}↳ Attempting AXFR on {WHITE}{domain}{YELLOW} via {CYAN}{nameserver}{RESET}")
    try:
        result = subprocess.check_output(["dig", "axfr", f"@{nameserver}", domain], stderr=subprocess.STDOUT)
        output = result.decode()
        if "Transfer failed." in output or "XFR size" not in output:
            print(f"{RED}✘ AXFR failed on {nameserver}{RESET}")
        else:
            print(f"{GREEN}✔ AXFR successful on {nameserver}!{RESET}")
            print(f"{CYAN}{'-'*50}\n{output}\n{'-'*50}{RESET}")
    except subprocess.CalledProcessError:
        print(f"{RED}✘ Error during AXFR attempt on {nameserver}{RESET}")

def main():
    banner()
    if len(sys.argv) != 2:
        print(f"{YELLOW}Usage: {WHITE}python3 {sys.argv[0]} <domain>{RESET}")
        sys.exit(1)

    domain = sys.argv[1]
    print(f"{CYAN}🔍 Looking up NS records for: {WHITE}{domain}{RESET}")

    nameservers = get_nameservers(domain)
    if not nameservers:
        print(f"{RED}[!] No nameservers found.{RESET}")
        sys.exit(1)

    print(f"{CYAN}🧠 Found {len(nameservers)} NS server(s): {', '.join(nameservers)}{RESET}")

    for ns in nameservers:
        try_zone_transfer(domain, ns)

    print(f"\n{GREEN}✅ Scan complete.{RESET}")

if __name__ == "__main__":
    main()
