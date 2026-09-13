import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "20366712"))
API_HASH = getenv("API_HASH", "a05398c005f6381009a9bb5d55118842")
BOT_TOKEN = getenv("BOT_TOKEN", "8617005297:AAFBgsgHX-ABFhNmT-FungWh-T1k6pXj8QE")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mehermusic369_db_user:mehermusic@cluster0.t7miuqv.mongodb.net/?appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000))

LOGGER_ID = int(getenv("LOGGER_ID", "-100381157409"))
OWNER_ID = int(getenv("OWNER_ID", 5719281608))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TEAMPURVI/ALPHA_MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/pittu_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+k-Mk-vprk7swNDA9")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

STRING1 = getenv("STRING_SESSION", "BQE2xXgASfgU7AmhxXfyH7UMlXEiI3jVQAREyoWYeuQ9B2FDjGonu60MU0d-SdNcFYn4IflyMjCcqQCUNvJS2mOMnIEWwcaQFVjfHrm9YGcE65aI_moWhbKWECxfVqGhkPfIpbhalz_iTzcOYf1US2H3uaIKUspzd_laD2ttboA4LDCXqYcz_EJ00aMLbpeHE6YbSyIlkxiF9JTXviTvNdPh21ky2WpXy53OVc4PmiJtb3j1DOAqnpWj66WG83cF3Ib41MxNioJSjLvTukYZxAcFFXTJ2ug4PERtURYz9AxSHaPhOIr9uxZA-VSG884W9LN3VGu1TtXO-afZ2J34Li9nFos3HAAAAAH76MrBAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/fu6jk3.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/26nzoq.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/f2s4ws.jpg"
STATS_IMG_URL = "https://files.catbox.moe/z0gh23.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://")
