import os
from dotenv import load_dotenv
from discord.ext import commands
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
RIOT_API_KEY = os.getenv('RIOT_API_KEY')

bot = commands.Bot(command_prefix='!lol-test ')

def player_already_registered(summoner_name):
    f = open("summoners.txt", "r")
    registered_summoners = f.readlines()
    for summoner in registered_summoners:
        if summoner.rstrip() == summoner_name:
            print("Player already exists")
            return True
    print("Player doesnt exist")
    return False

def get_summoner_id(summoner):
    summoner_account_api = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "/?api_key=" + RIOT_API_KEY
    summoner_account_json = requests.get(summoner_account_api).json()
    return summoner_account_json['id']

def get_summoner_stats(summoner_id):
    summoner_data_api = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summoner_id + "/?api_key=" + RIOT_API_KEY
    summoner_data_json = requests.get(summoner_data_api).json()
    for queue in summoner_data_json:
        if queue['queueType'] == 'RANKED_SOLO_5x5':
            summoner_name = queue['summonerName']
            summoner_tier = queue['tier']
            summoner_rank = queue['rank']
            summoner_wins = queue['wins']
            summoner_losses = queue['losses']
    return {
        "summoner_name": summoner_name,
        "summoner_tier": summoner_tier,
        "summoner_rank": summoner_rank,
        "summoner_win_rate": str(round((summoner_wins/(summoner_wins+summoner_losses))*100)) + "%"
    }

def get_summoners():
    with open("summoners.txt") as f:
        summoners = f.read().splitlines()
    return summoners

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='register', help='Register your league name.')
async def register(ctx, summoner_name):
    if not player_already_registered(summoner_name):
        f = open("summoners.txt", "a")
        f.write(summoner_name + "\n")

    await ctx.send("Registered " + summoner_name)

@bot.command(name='ranks', help='Returns registered users ranks.')
async def ranks(ctx):
    all_summoner_details = []
    summoners = get_summoners()
    for summoner in summoners:
        summoner_id = get_summoner_id(summoner)
        summoner_stats = get_summoner_stats(summoner_id)
        all_summoner_details.append(summoner_stats)

    await ctx.send(all_summoner_details)

bot.run(TOKEN)