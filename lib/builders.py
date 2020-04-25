from lib import api_calls


def summoner_stats_builder(summoner):
    summoner_data_json = api_calls.get_summoner_stats(summoner)
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
        "summoner_win_rate": str(round((summoner_wins/(summoner_wins+summoner_losses))*100)) + "%",
        "games_played": str(summoner_losses + summoner_wins)
    }


def string_builder(summoner_details):
    formatted_details = []
    for summoner in summoner_details:
        formatted_details.append("Name: " + summoner["summoner_name"] +
                                 "  |  Rank " + summoner["summoner_tier"] +
                                 " " + summoner["summoner_rank"] +
                                 "  |  Win rate " + summoner["summoner_win_rate"] +
                                 " (Games played: " + summoner["games_played"] + ")")
    return "\n".join(formatted_details)