import discord

def create_notification(title, description):
    embed = discord.Embed(
        colour=discord.Color.blurple(),
        title=title,
        description=description,
    )
    embed.set_image(url='https://media.discordapp.net/attachments/1151336983889723392/1161077667248996402/WizardCrafft_Survival_-_1.9_a_1.20.1.gif?ex=6536fcd7&is=652487d7&hm=ac56b02123f5e53ceedfeef7574e0b97a9627dba79f25cd9f5ad7aeedc2e6c2f&=')

    return embed