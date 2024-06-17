import discord
import os
from dotenv import load_dotenv
from listeners import *

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

myToken = os.getenv("TOKEN")

client = discord.Client(intents=intents)

client.run(myToken)
