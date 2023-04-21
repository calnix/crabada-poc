import os, requests
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("PUSHOVER_USER_ID")
API = os.getenv('PUSHOVER_API_TOKEN')

BASE_URL = "https://api.pushover.net/1/"
MESSAGE_URL = BASE_URL + "messages.json"

# POST an HTTPS request to https://api.pushover.net/1/messages.json with the following parameters:

def send_message(text):
    #Send a message
    payload = {"token": "aekmnzsv34vvtn36brg1g8uwtpnatw", "user": "uvf6cqpc8e8rb1nvh6vx3d4jtf9p3i", "message": text}
    r = requests.post('https://api.pushover.net/1/messages.json', data = payload)
    return r

def main():
    """Main function for this script."""
    r = send_message('testing')
    if not r.status_code == 200:
        print(r.text)
    
if __name__ == '__main__':
    send_message('testing')
