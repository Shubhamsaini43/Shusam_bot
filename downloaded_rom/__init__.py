from telethon import TelegramClient
import logging
import time  


openai_key = "sk -MxJrVidnaA6aC4abDHSmT3BlbkFJA1fdLXUeKL89qUgi4OQ8"

api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6090313957:AAEdphvNfs-saRS54B3XyH3Bho3Y3GfKT3A"

bot = TelegramClient("shusam",api_id,api_hash).start(bot_token = bot_token) 