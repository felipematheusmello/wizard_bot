import os
import discord
from dotenv import load_dotenv
from discord import app_commands

def load_token():
    load_dotenv()
    return os.getenv("TOKEN_DISCORD")
