import os
from dotenv import load_dotenv
from discord.ext import commands
from lib import summonerstatsbuilder, register, riot_api

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!lol-bot ")

summoner_stats_builder = summonerstatsbuilder.SummonerStatsBuilder()
summoner_register = register.Register()
riot_api = riot_api.RiotApi()


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="register", help="Register your league name.")
async def register(ctx, summoner_name):
    summoner_register.register(summoner_name)

    await ctx.send("Registered " + summoner_name)


@bot.command(name="ranks", help="Returns registered users ranks.")
async def ranks(ctx):
    all_summoner_details = []
    summoners = summoner_register.get_summoners()
    for summoner in summoners:
        all_summoner_details.append(summoner_stats_builder.build_for(summoner))

    await ctx.send("\n".join(all_summoner_details))


@bot.command(name="patch", help="Returns the latest patch notes")
async def patch(ctx):
    league_version = riot_api.get_league_version()
    patch_notes_url = "https://euw.leagueoflegends.com/en-gb/news/game-updates/patch-" + league_version[0] + "-" + league_version[1] + "-notes/"

    await ctx.send(patch_notes_url)

bot.run(TOKEN)
