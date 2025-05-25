
import socket

def scan_ports(target):
    print(f"Scanning {target}...\n")
    for port in range(20, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[+] Port {port} is open")
            s.close()
        except:
            pass

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    scan_ports(target_ip)
