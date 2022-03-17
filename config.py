from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("1BVtsOJUBu1IhE7EzRQevoGIPLNViDXhZpGR0L6p1FfWQGXU4FGRt8v6FW3sYk-ZdQbwok_jJv34_wrPT_O8k-ln3w6o1mvTfS4XcsLM6ZlcyXSVVTFpu_Q7kJu2vqqnG4bdEm65V3t7v2z-RT4-gmuTkMtWo0Ge-cw0SRBSIu1sDk8_PtxLnyoeb3I4ELDX4DU2yrDG05Z_I0JmxOUmJT6RhQm7emA2m7jkDJ3jrjWyo3X3X6Cvfca4VyxLjdiLvgpQds2Re-4DdxrQ0C4wxrWiJB6HAczgkt-QibBaA11rJIMXkcnJM7YCmZ2aplowQ8mqp7-axR0nnjqji0P53d_5mtoIjN-g=", "session")
BOT_TOKEN = ("5106142420:AAHcjFV5DGAQn6-6qdKmZnGvAfH14HOjsRI")
API_ID = int(getenv("7246721", ""))
API_HASH = getenv("bc7dc8ccc13aa4b650c2e5c35b7191b3")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
