import discord

class Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value=None

    @discord.ui.button(label="Abrir Ticket", style=discord.ButtonStyle.primary, emoji="➕")
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()

        ticket = None
        if interaction.channel.name != 'ticket':
            await interaction.response.send_message(ephemeral=True, content=f"Você só pode mandar isso no canal de tickets" )
            return

        async for thread in interaction.channel.archived_threads():
            if f'{interaction.user.id}' in thread.name:
                if thread.archived:
                    ticket = thread

                else:
                    await interaction.response.send_message(ephemeral=True, content=f"Você já tem um ticket em andamento!" )
                    return

        if ticket != None:
            await ticket.edit(name=f"{button.emoji} {interaction.user.name} {interaction.user.id}", auto_archive_duration=10080, invitable=False, archived=False)

        else:
            ticket = await interaction.channel.create_thread(name=f'ticket {interaction.user.name} {interaction.user.id}', auto_archive_duration=10080, type=discord.ChannelType.private_thread)

        await interaction.response.send_message(ephemeral=True, content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(
            f"📖 **| ** {interaction.user.mention} ticket criado! Envie todas as informações para que seu caso seja avaliado por um atendente. 📖 \n\n"
            f"Após a sua questão ser sanada, você pode usar `/fecharticket` para encherrar o atendimento!\n\n<@&691673359896805418>, <@&960015181054885928>"
            )
