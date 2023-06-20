from .. import bot,openai_key
from telethon import events
import asyncio
import openai

openai.my_api_key = openai_key





@bot.on(events.NewMessage(incoming= True,pattern="/start"))
async def start(event):
  await  event.reply("hey it's me shusam bot") 

@bot.on(events.NewMessage(incoming= True,pattern="/get"))
async def start(event):
  await  event.reply("Hello this is get command")
  
@bot.on(events.NewMessage(incoming= True,pattern="/eval"))
async def start(event):
  await  event.reply("Hello this is eval command")
  
@bot.on(events.NewMessage(incoming= True,pattern="/hello"))
async def start(event):
  await  event.reply("Hello this is hello command")
 
@bot.on(events.NewMessage(incoming= True,pattern="/youtube"))
async def start(event):
  a = await  event.reply("welcome to my channel")
  await asyncio.sleep(2)
  await a.edit("jiya aayo hai biya wapis chlo ja")