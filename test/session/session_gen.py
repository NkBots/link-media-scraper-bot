from pyrogram import Client
from decouple import config

api_id = config("API_ID", "8755370")
api_hash = config("API_HASH", "54261233493bbc5bbf489146dd2909dc")
bot_token = config("BOT_TOKEN", "6108521425:AAH-viqVb0Xa8bWjQglaZ2HIVhCImQ_TuBM")

def gen_session():
    app = Client("my_bot",api_id,api_hash,bot_token=bot_token)
    with app:
        session_string = app.export_session_string()
        app = Client("my_bot", api_id,api_hash,bot_token=bot_token)
        return app
