# system_info.py
import platform
import psutil
import telegram

# Bot token and chat ID
bot = telegram.Bot(token="YOUR_BOT_TOKEN")
chat_id = "YOUR_CHAT_ID"

def gather_system_info():
    sys_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "CPU": psutil.cpu_count(logical=False),
        "RAM": psutil.virtual_memory().total / (1024 ** 3)  # in GB
    }
    
    sys_info_str = "\n".join([f"{key}: {value}" for key, value in sys_info.items()])
    return sys_info_str

def send_system_info():
    sys_info = gather_system_info()
    bot.send_message(chat_id=chat_id, text=sys_info)

if __name__ == "__main__":
    send_system_info()
