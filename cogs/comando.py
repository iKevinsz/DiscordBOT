import discord
from discord.ext import commands



class comando(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Olá")


    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def info(self, ctx, *, usuario:discord.Member=None):
        if usuario is None:
          await ctx.send("!info + @usuario")
          return
        string = f"Nome: {usuario.name}\nId : {usuario.id}\nAvatar : {usuario.avatar_url}"
        await  ctx.send(string)
 
    @commands.command()
    async def admin(self, ctx):
        if ctx.author.guild_permissions.administrator:
            await ctx.send('Você é o administrador!')
        else:
            await ctx.sned('Você não é administrador!')


def setup(client):
    client.add_cog(comando(client))