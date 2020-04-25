import os
from dotenv import load_dotenv
import requests


class RiotApi:
    def __init__(self):
        load_dotenv()
        self.RIOT_API_KEY = os.getenv('RIOT_API_KEY')


    def get_summoner_stats(self, summoner):
        summoner_id = self.__get_summoner_id(summoner)
        summoner_data_api = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summoner_id + "/?api_key=" + self.RIOT_API_KEY
        return requests.get(summoner_data_api).json()


    def __get_summoner_id(self, summoner):
        summoner_account_api = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "/?api_key=" + self.RIOT_API_KEY
        summoner_account_json = requests.get(summoner_account_api).json()
        return summoner_account_json['id']
