
def get_summoners():
    with open("summoners.txt") as f:
        summoners = f.read().splitlines()
    return summoners


def player_already_registered(summoner_name):
    f = open("summoners.txt", "r")
    registered_summoners = f.readlines()
    for summoner in registered_summoners:
        if summoner.rstrip() == summoner_name:
            print("Player already exists")
            return True
    print("Player doesnt exist")
    return False


def register(summoner_name):
    if not player_already_registered(summoner_name):
        f = open("summoners.txt", "a")
        f.write(summoner_name + "\n")