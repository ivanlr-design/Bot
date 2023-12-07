
import discord
from discord.ext import commands
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    print(message.content)

bot.run('MTE4MjI4MDE1NDIxOTgyNzI0MA.GqOl1G.C5B0_hh6w93JF8whvl2mWXTeXGXtF4PhNso61E')
