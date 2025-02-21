# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "6534707"))
    API_HASH = os.environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5225692027:AAFwugDiuhZjwQKUDjWbXhLZlhzzFMXAHJo")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1430593323))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://nhere118:jSsmgEs1uEqnlbrZ@cluster0.rdkih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001729892476"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
