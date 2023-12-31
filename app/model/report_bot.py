import discord
from app.views.dropdrown_view import DropdownView
from app.views.notifications import NotificationView
from discord import app_commands
from discord.ext import commands
from app.components.message import embed
from app.components.notification import create_notification

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

def _check_roles(interaction: discord.Interaction, roles: [int]):
    for role in roles:
        if interaction.user.get_role(role):
            return True

    return False


@tree.command(guild=discord.Object(id=server_id), name='setup', description='Setup')
@commands.has_permissions(manage_guild=True)
async def setup(interaction: discord.Interaction):
    if not 'ticket' in interaction.channel.name:
        await interaction.response.send_message(f"Você só pode mandar isso no canal de tickets", ephemeral=True)
        return

    await interaction.response.send_message(f"Painel criado!", ephemeral=True)

    await interaction.channel.send(f"Mensagem do painel!", embed=embed, view=DropdownView())

@tree.command(guild=discord.Object(id=server_id), name='aviso', description='Aviso')
@commands.has_permissions(manage_guild=True)
async def aviso(interaction: discord.Interaction, titulo: str, mensagem: str):
    embed = create_notification(title=titulo.capitalize(), description=mensagem)
    if 'atualizações' not in str(interaction.channel.name):
        await interaction.response.send_message(f"Você só pode mandar isso no canal de Atualizações", ephemeral=True)
        return

    if not titulo and not mensagem:
        await interaction.response.send_message(f"Titulo e nome são necessários para essa ação", ephemeral=True)
        return

    await interaction.channel.send(None, embed=embed, view=NotificationView())


@tree.command(guild=discord.Object(id=server_id), name='fecharticket', description='FecharTicket')
async def _fecharticket(interaction: discord.Interaction):
    roles = [691673359896805418, 960015181054885928, 692076344351260732]
    if str(interaction.user) in str(interaction.channel.name) or _check_roles(interaction=interaction, roles=roles):
        await interaction.response.send_message(f"O ticket foi arquivado por {interaction.user.name}")
        await interaction.channel.edit(archived=True)
    else:
        print(interaction.channel)
        print(interaction.user)
        print(interaction.guild.get_role(960015181054885928))
        await interaction.response.send_message("Isso não pode ser executado aqui")