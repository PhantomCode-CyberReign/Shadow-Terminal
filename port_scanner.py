# port_scanner.py
import socket

def port_scan(target_ip, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)
            sock.close()
        except socket.error:
            continue
    return open_ports

target_ip = input("Enter target IP for scanning: ")
ports_to_scan = [22, 80, 443, 8080]
open_ports = port_scan(target_ip, ports_to_scan)
print(f"Open Ports: {open_ports}")
