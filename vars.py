#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27263010"))
API_HASH = environ.get("API_HASH", "4c9da2b3fa15323237147eac02f1681c")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "27263010"))
CREDIT = environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '27263010').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '27263010').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
