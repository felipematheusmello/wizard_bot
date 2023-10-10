import discord


class BotClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), command_prefix='/')
        self.syncronized = False # When the bot is not syncronized the command more than once
        self.server_id = 691533643914412051


