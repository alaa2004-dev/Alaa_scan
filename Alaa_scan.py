import socket
from colorama import Fore, Style, init

init(autoreset=True)

def get_localhost():
    print(Fore.YELLOW + "Localhost:", socket.gethostname())

def get_service_name(port):
    try:
        print(Fore.GREEN + f"Service for port {port}: {socket.getservbyport(port)}")
    except:
        print(Fore.RED + f"No service found for port {port}")

def port_scan(target):
    print(Fore.CYAN + f"Scanning ports on {target}...")
    for port in range(20, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(Fore.MAGENTA + f"Port {port} is open")
            s.close()
        except:
            pass

def main():
    # شعار البداية
    print(Fore.CYAN + """
====================================
          ♠ Alaa Scan ♠
   Created by Alaa Odeh Barak
====================================
""")

    while True:
        print(Fore.BLUE + "\n♠ Alaa_scan Tool ♠")
        print(Fore.YELLOW + "1. Get Localhost")
        print(Fore.GREEN + "2. Get Service Name for a Port")
        print(Fore.MAGENTA + "3. Port Scanning")
        print(Fore.RED + "4. Exit")

        choice = input(Fore.CYAN + "Enter choice: ")

        if choice == "1":
            get_localhost()
        elif choice == "2":
            port = int(input("Enter port number: "))
            get_service_name(port)
        elif choice == "3":
            target = input("Enter target IP: ")
            port_scan(target)
        elif choice == "4":
            print(Fore.RED + "Exiting Alaa_scan...")
            break
        else:
            print(Fore.RED + "Invalid choice!")

if __name__ == "__main__":
    main()
