import discord
from app.components.ui_interfaces import Dropdown

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Dropdown())
