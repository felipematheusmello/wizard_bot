import discord
from config import load_token
from app.model.report_bot import client
from app.views.dropdrown_view import DropdownView
from discord import app_commands


def run():
    TOKEN = load_token()

    client.run(TOKEN)

