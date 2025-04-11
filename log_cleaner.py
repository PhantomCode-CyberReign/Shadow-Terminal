# log_cleaner.py
import os

# Function to delete specific log files
def delete_logs(log_file_path):
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
        print(f"Deleted log file: {log_file_path}")
    else:
        print(f"No log file found at {log_file_path}")

# Specify the log file path to delete
log_file_path = "/path/to/logfile.log"  # Customize this with your log file path
delete_logs(log_file_path)
