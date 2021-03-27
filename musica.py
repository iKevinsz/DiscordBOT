import discord
import asyncio
import main

client = discord.Client()

players = {}
COR = 0xF7FE2E

@client.event
async def on_ready():
    print(client.user.name)
    

@client.event
async def on_message(message):
    if message.content.startswith('!join'):
        try:
            channel = message.author.voice.voice_channel
            await channel.connect(channel)
        except discord.errors.InvalidArgument:
            await client.user.name.send_message(message.channel, "O bot ja esta em um canal de voz")
        except Exception as error:
            await client.user.name.send_message(message.channel, "Error: ```{error}```".format(error=error))

    if message.content.startswith('!sair'):
        try:
            mscleave = discord.Embed(
                title="\n",
                color=COR,
                description="Sai do canal de voz, a musica parou!"
            )
            voice_client = client.voice_client_in(message.server)
            await client.send_message(message.channel, embed=mscleave)
            await voice_client.disconnect()
        except AttributeError:
            await client.user.name.send_message(message.channel, "O Bot não esta em nenhum canal de voz.")
        except Exception as Hugo:
            await client.user.name.send_message(message.channel, "Error: ```{haus}```".format(haus=Hugo))

    if message.content.startswith('!play'):
        try:
            yt_url = message.content[6:]
            if client.user.name.is_voice_connected(message.server):
                try:
                    voice = client.user.name.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb.add_field(name="Enviado em:", value="`{}`".format(player.uploaded_date))
                    mscemb.add_field(name="Enviado por:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Duraçao:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.user.name.send_message(message.channel, embed=mscemb)
                except Exception as e:
                    await client.user.name.send_message(message.server, "Error: [{error}]".format(error=e))

            if not client.user.name.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.user.name.join_voice_channel(channel)
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb2 = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb2.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb2.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb2.add_field(name="Enviado em:", value="`{}`".format(player.upload_date))
                    mscemb2.add_field(name="Enviado por:", value="`{}`".format(player.uploader))
                    mscemb2.add_field(name="Duraçao:", value="`{}`".format(player.duration))
                    mscemb2.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb2.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.user.name.send_message(message.channel, embed=mscemb2)
                except Exception as error:
                    await client.user.name.send_message(message.channel, "Error: [{error}]".format(error=error))
        except Exception as e:
            await client.user.name.send_message(message.channel, "Error: [{error}]".format(error=e))




    if message.content.startswith('!pause'):
        try:
            mscpause = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.user.name.send_message(message.channel, embed=mscpause)
            players[message.server.id].pause()
        except Exception as error:
            await client.user.name.send_message(message.channel, "Error: [{error}]".format(error=error))
    if message.content.startswith('!resume'):
        try:
            mscresume = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.user.name.send_message(message.channel, embed=mscresume)
            players[message.server.id].resume()
        except Exception as error:
            await client.user.name.send_message(message.channel, "Error: [{error}]".format(error=error))


client.run('TOKEN')