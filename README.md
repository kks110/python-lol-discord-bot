# League of Legends Discord Bot

Requires `requests` and `dotevn` to be installed:
```bash
pip install -U requests
pip install -U python-dotenv
pip install -U discord.py
```

You need to make a copy of the `.env.exampe` file, and call it `.env`.
Update with your appropriate Token, Guild and Riot API key.
The Discord token can be generated in the discord developer portal when you create the bot.

You can start it by running the `bot.py` file:
```bash
py .\bot.py
```

Once connect it should say:
```bash
botname has connected to Discord!
```

Once it's running users on your server can register with the command:
```bash
!lol-bot register summoner_name
```

You can then see the stats of the registered player buy running:
```bash
!lol-bot ranks
```