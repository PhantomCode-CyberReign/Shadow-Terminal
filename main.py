# main.py (Updated)
from payload_generator import generate_payload
from port_scanner import start_port_scanner
from brute_forcer import start_brute_force
from phishing_toolkit import start_phishing_attack
from telegram_bot import start_telegram_bot
from log_cleaner import clean_logs
from auto_wordlist_downloader import start_auto_wordlist_download

# main.py (Updated with cool banner)
def banner():
    print("""
╔══════════════════════════════════════════════╗
║                                              ║
║  🕷️  SHADOW TERMINAL | ULTIMATE HACKER'S  🕷️ ║
║           FRAMEWORK v1.0                     ║
║                                              ║
║     ⚔️  Phantom Code | Cyber Reign ⚔️        ║
║                                              ║
╚══════════════════════════════════════════════╝
    """)
    print("=" * 50)

def menu():
    banner()
    print("Select an option:")
    print("1. Payload Generator")
    print("2. SSH Brute Force Attack")
    print("3. Port Scanner")
    print("4. Phishing Toolkit")
    print("5. Telegram Bot Controller")
    print("6. Log Cleaner")
    print("7. Auto Wordlist Downloader")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        generate_payload()
    elif choice == '2':
        start_brute_force()
    elif choice == '3':
        start_port_scanner()
    elif choice == '4':
        start_phishing_attack()
    elif choice == '5':
        start_telegram_bot()
    elif choice == '6':
        clean_logs()
    elif choice == '7':
        start_auto_wordlist_download()
    elif choice == '8':
        print("Exiting Shadow Terminal. See you soon!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
