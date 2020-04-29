from lib import riot_api


class SummonerStatsBuilder:
    def __init__(self):
        self.riot_api = riot_api.RiotApi()


    def build_for(self, summoner):
        summoner_data_json = self.riot_api.get_summoner_stats(summoner)
        for queue in summoner_data_json:
            if queue["queueType"] == "RANKED_SOLO_5x5":
                return self.__string_builder(
                    summoner_name = queue["summonerName"],
                    summoner_tier = queue["tier"],
                    summoner_rank = queue["rank"],
                    summoner_winrate = str(round((queue["wins"]/(queue["wins"]+queue["losses"]))*100)) + "%",
                    games_played = str(queue["losses"] + queue["wins"])
                )


    def __string_builder(self, summoner_name, summoner_tier, summoner_rank, summoner_winrate, games_played):
        return ("Name: " + summoner_name +
                "  |  Rank " + summoner_tier +
                " " + summoner_rank +
                "  |  Win rate " + summoner_winrate +
                " (Games played: " + games_played + ")")