import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

dicas = [
    "Evite usar plástico descartável no dia a dia.",
    "Separe o lixo reciclável do orgânico.",
    "Economize água ao escovar os dentes.",
    "Prefira transporte público ou bicicleta.",
    "Reduza o consumo de energia desligando aparelhos."
]

@bot.event
async def on_ready():
    print(f'Bot online como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "oi":
        await message.channel.send("o que voce gostaria pra hoje")
    if "dica" in message.content.lower():
        await message.channel.send(random.choice(dicas))
    await bot.process_commands(message)

@bot.command()
async def dica(ctx):
    await ctx.send(random.choice(dicas))

@bot.command()
async def poluicao(ctx):
    await ctx.send(
        "A poluição pode ser reduzida com pequenas atitudes diárias, como reciclar, reduzir consumo e evitar desperdícios."
    )

bot.run("")
