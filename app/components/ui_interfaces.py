import discord
from app.components.button import Button

class Dropdown(discord.ui.Select):
    def __init__(self):
        dropdown_options = [
            discord.SelectOption(value='service', label='Atendimento', emoji='🎫'),
            discord.SelectOption(value='help', label='Ajuda', emoji='👋'),
        ]

        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=dropdown_options,
            custom_id="persistent_view:dropdown_help"
        )

    async def callback(self, interaction: discord.Integration):
        print(self.values[0])
        if self.values[0] == "help":
            await interaction.response.send_message("Se você precisa de ajuda escreva algum comentário abaixo", ephemeral=True)

        elif self.values[0] == "service":
            await interaction.response.send_message("Clique abaixo para criar um ticket",ephemeral=True, view=Button())
