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

        for therad in interaction.channel.threads:
            if f'{interaction.user.id}' in therad.name:
                if therad.archived:
                    ticket = therad

                else:
                    await interaction.response.send_message(ephemeral=True, content=f"Você já tem um ticket em andamento!" )
                    return

        if ticket != None:
            await  ticket.unarchive()
            await ticket.edit(name=f"{self.emoji} {interaction.user.name} {interaction.user.id}", auto_archive_duration=10080, invitable=False)

        else:
            ticket = await interaction.channel.create_thread(name=f'{interaction} {interaction.user.name} {interaction.user.id}', auto_archive_duration=10080, type=discord.ChannelType.public_thread)
            await ticket.edit(invitable=False)

        await interaction.response.send_message(ephemeral=True, content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(
            f"📖 **| ** {interaction.user.mention} ticket criado! Envie todas as informações para que seu caso seja avaliado por um atendente. 📖 \n\n"
            f"Após a sua questão ser sanada, você pode usar `/fecharticket` para encherrar o atendimento!\n\n<@&691673359896805418>, <@&960015181054885928>"
            )
