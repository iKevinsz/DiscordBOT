import json
import asyncio
import discord 
from discord.ext.commands import AutoShardedBot, when_mentioned_or


modulos = ["cogs.comando"]

client = AutoShardedBot(command_prefix="!", case_insensitive=True)

@client.event
async def on_ready():
    print(f"{client.user.name} - Online.")
    await client.change_presence(activity=discord.Streaming(name="Kevin_x", url="https://www.twit.tv/kevin_X"))

if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)

    client.run("TOKEN")