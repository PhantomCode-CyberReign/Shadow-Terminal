# telegram_bot.py
import telegram
from time import sleep

# Bot initialization (enter your bot's token here)
bot = telegram.Bot(token="YOUR_BOT_TOKEN")

# Send a message to your Telegram bot
def send_message(chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)

# Example of sending a message
chat_id = input("Enter your chat ID (obtain from @userinfobot): ")
message = "Shadow Terminal | Ultimate Hacker’s Framework v1.0 has started!"
send_message(chat_id, message)
print("Message sent to Telegram bot.")

# Example of receiving messages (real-time updates)
def check_updates():
    updates = bot.get_updates()
    for update in updates:
        print(f"New message from {update.message.from_user.first_name}: {update.message.text}")

# Check messages every 5 seconds
while True:
    check_updates()
    sleep(5)
