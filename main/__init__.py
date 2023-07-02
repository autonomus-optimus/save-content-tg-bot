#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 26957450
API_HASH = "c82248cee35b0c9a9de4a5caf0c2ac9f"
BOT_TOKEN = "5465761249:AAFYGRwBvPMTlH-OVlGPbH1RpSzpLnKhR4I"
SESSION = "AgAjAXdJu9EJDSdbvwqfztbBfhOb54z0j_uSU_eI3g9kUKLeRoRVz89bVV10dFIxSQLTSGIzb9tpSlY99xNEqyJ6LeyM9t46fuqiMydlqe8hMnnIa7Kl484E565Hpx9IVUqbWwNOSGPO_PfOY77Jyw27j8mnjKLDuVgHf-k1gLGW8BioQPEDvIlAn0GX6VAvSqt_FljK-QqrYcbq9d0InPzhNnPVTRh9uGnMlltFQnp6siVZcmDNO5Xu52COyZFkE-iR-_LBx9OjzAXNbGDG3TSw4u8ZIRdDgdhoVFYC5u8NgWRCTBCPMphLn31_GKHYRDgceLAqU7k3LfhJoVAcI_UWAAAAATvYpM4A"
FORCESUB = "savecontenttempbot"
AUTH = 5299021006

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
