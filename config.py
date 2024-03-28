import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5675942836:AAHnwqYsqPtZjoX0eMDUOwx5IpAQhmeFC6o")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7375040"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4166e18db5a7880136d41ceb0aa20971")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001863544070"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1880970848"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Vidraplay")

# CHANNEL & GROUP
CHANNEL1 = os.environ.get("CHANNEL1", "jjnswf")
CHANNEL2 = os.environ.get("CHANNEL2", "demonicxyz")
CHANNEL3 = os.environ.get("CHANNEL3", "Demigodxyz")
CHANNEL4 = os.environ.get("CHANNEL4", "fwbhunters")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://ssygtqme:qzBUfpOHRLuvjXToezgp8l4xI-lA5HOt@satao.db.elephantsql.com/ssygtqme")

# force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001168297108"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001698540394"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001768600339"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1001815424816"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))

# start message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}\n\nSaya dapat menyimpan file pribadi di Saluran Tertentu dan pengguna lain dapat mengaksesnya dari tautan khusus.</b>",
)
try:
    ADMINS = []
    for x in os.environ.get("ADMINS", "5841494828").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Daftar Admin anda tidak berisi User ID yang valid.")
try:
    ADMINS = []
    for x in os.environ.get("ADMINS", "").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Daftar Admin anda tidak berisi User ID yang valid.")

# Force sub message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Terlebih Dahulu</b>",
)

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True":
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1880970848)
ADMINS.append(5841494828)
ADMINS.append(2108493355)
ADMINS.append(1735782610)

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
