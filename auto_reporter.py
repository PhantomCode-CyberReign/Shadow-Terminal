# auto_reporter.py
import os
import subprocess
import telegram

# Bot token and chat ID
bot = telegram.Bot(token="YOUR_BOT_TOKEN")
chat_id = "YOUR_CHAT_ID"

def install_dependencies():
    dependencies = ["pynput", "psutil", "pyautogui", "telegram"]
    for dep in dependencies:
        subprocess.run([sys.executable, "-m", "pip", "install", dep])

def send_report(message):
    bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    install_dependencies()
    send_report("All dependencies have been successfully installed!")
