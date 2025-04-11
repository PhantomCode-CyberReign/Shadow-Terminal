# screenshot_capture.py
import pyautogui
import telegram
import time

# Bot token and chat ID
bot = telegram.Bot(token="YOUR_BOT_TOKEN")
chat_id = "YOUR_CHAT_ID"

def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")  # Save the screenshot as a PNG file
    bot.send_photo(chat_id=chat_id, photo=open("screenshot.png", 'rb'))  # Send screenshot to Telegram bot

if __name__ == "__main__":
    while True:
        capture_screenshot()
        time.sleep(60)  # Capture screenshot every minute
