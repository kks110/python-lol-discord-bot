import os
from dotenv import load_dotenv
from discord.ext import commands
from lib import api_calls, builders, summoner_details

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!lol-test ')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='register', help='Register your league name.')
async def register(ctx, summoner_name):
    summoner_details.register(summoner_name)

    await ctx.send("Registered " + summoner_name)


@bot.command(name='ranks', help='Returns registered users ranks.')
async def ranks(ctx):
    all_summoner_details = []
    summoners = summoner_details.get_summoners()
    for summoner in summoners:
        summoner_stats = builders.summoner_stats_builder(summoner)
        all_summoner_details.append(summoner_stats)

    await ctx.send(builders.string_builder(all_summoner_details))

bot.run(TOKEN)