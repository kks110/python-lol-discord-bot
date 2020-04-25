

class Register:
    def get_summoners(self):
        with open("summoners.txt") as f:
            summoners = f.read().splitlines()
        return summoners


    def register(self, summoner_name):
        if not self.__player_already_registered(summoner_name):
            f = open("summoners.txt", "a")
            f.write(summoner_name + "\n")


    def __player_already_registered(self, summoner_name):
        f = open("summoners.txt", "r")
        registered_summoners = f.readlines()
        for summoner in registered_summoners:
            if summoner.rstrip() == summoner_name:
                return True
        return False