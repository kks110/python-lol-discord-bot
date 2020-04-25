import os
from dotenv import load_dotenv
from discord.ext import commands
from lib import summonerstatsbuilder, register

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!lol-test ')

summoner_stats_builder = summonerstatsbuilder.SummonerStatsBuilder()
summoner_register = register.Register()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='register', help='Register your league name.')
async def register(ctx, summoner_name):
    summoner_register.register(summoner_name)

    await ctx.send("Registered " + summoner_name)


@bot.command(name='ranks', help='Returns registered users ranks.')
async def ranks(ctx):
    all_summoner_details = []
    summoners = summoner_register.get_summoners()
    for summoner in summoners:
        all_summoner_details.append(summoner_stats_builder.build_for(summoner))

    await ctx.send("\n".join(all_summoner_details))

bot.run(TOKEN)
