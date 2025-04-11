# phishing_toolkit.py
import os

def setup_phishing_website(target_url):
    # Simple phishing setup (copy website HTML, add fake login)
    os.system(f"git clone {target_url}")
    print("Phishing website setup complete.")

target_url = input("Enter target URL for phishing: ")
setup_phishing_website(target_url)
