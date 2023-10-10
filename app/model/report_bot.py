import discord
from app.views.dropdrown_view import DropdownView
from discord import app_commands
from discord.ext import commands
from app.components.message import embed

server_id = 691533643914412051

class ReportBotClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.syncronized = False # When the bot is not syncronized the command more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.syncronized:
            await tree.sync(guild=discord.Object(id=server_id))
            self.syncronized = True
        print(f"Entramos como {self.user}.")


    async def setup_hook(self) -> None:
        self.add_view(DropdownView())

client = ReportBotClient()
tree = app_commands.CommandTree(client)
# Adicione seus comandos da árvore aqui

@tree.command(guild=discord.Object(id=server_id), name='setup', description='Setup')
@commands.has_permissions(manage_guild=True)
async def setup(interaction: discord.Interaction):
    await interaction.response.send_message(f"Painel criado!", ephemeral=True)

    await interaction.channel.send(f"Mensagem do painel!", embed=embed, view=DropdownView())

@tree.command(guild=discord.Object(id=server_id), name='fecharticket', description='FecharTicket')
async def _fecharticket(interaction: discord.Interaction):
    mod = interaction.guild.get_role(960015181054885928)
    if str(interaction.user.id) in interaction.channel.name or mod in interaction.author.role:
        await interaction.response.send_message(f"O ticket foi arquivado por {interaction.user.name}")
        await interaction.channel.archive(locked=True)
    else:
        await interaction.response.send_message("Isso não pode ser executado")