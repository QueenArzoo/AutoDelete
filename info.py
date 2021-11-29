import os
from os import environ

API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
TOKEN = os.environ.get("TOKEN")
ADMINS = set(int(x) for x in os.environ.get("ADMINS", "1963952285").split())
Dev = int(os.environ.get("Dev", "1963952285"))
TIME = os.environ.get("TIME", None)
GROUPS = [int(admin) for admin in environ.get("GROUPS", "").split()]
