import aiohttp
import json
import random
import asyncio
from discord.ext import commands
import discord
class Gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,10,commands.BucketType.user)
    async def hug(self,ctx,member:discord.Member):
     if ctx.author == member:
        await ctx.send('Oh Nuuu!! <a:crying:716427099300429854>\nI will hug you instead >~<')
     else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/hug") as r:
                data = await r.json()
                embed = discord.Embed(title=f'{ctx.author.name} **hugs** {member.name}',
                colour=0xdb7bff)
                embed.set_image(url=data['link'])
                await ctx.send(embed=embed)
    @hug.error
    async def hug_error(self,ctx,error):
        if isinstance(error,commands.CommandOnCooldown):
            msg=await ctx.send(f"*`You're on cooldown,please wait {round(error.retry_after)} seconds to use this command again`*")
            await asyncio.sleep(5)
            await message.delete()
        else:
            raise(error)

    @commands.command(alaises=['pet'])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def pat(self,ctx,member:discord.Member):
        if ctx.author == member:
           await ctx.send('Oh Nuuu!! <:sed:713324893609132044> \nI will pat you instead >~<')
        else:
           async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/pat") as r:
                data = await r.json()
                embed = discord.Embed(title=f'{ctx.author.name} **pats** {member.name} gently',
                colour=0xdb7bff)
                embed.set_image(url=data['link'])
                await ctx.send(embed=embed)
    @pat.error
    async def pat_error(self,ctx,error):
        if isinstance(error,commands.CommandOnCooldown):
            msg=await ctx.send(f"*`You're on cooldown,please wait {round(error.retry_after)} seconds to use to use this command again`*")
            await asyncio.sleep(5)
            await message.delete()
        else:
            raise(error)
    @commands.command()
    @commands.cooldown(1,10,commands.BucketType.user)
    async def meme(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/meme") as r:
                data = await r.json()
                embed = discord.Embed(title=data['caption'],
                colour=0xdb7bff)
                embed.set_image(url=data['image'])
                await ctx.send(embed=embed)
    @meme.error
    async def meme_error(self,ctx,error):
        if isinstance(error,commands.CommandOnCooldown):
            msg=await ctx.send(f"*`You're on cooldown,please wait {round(error.retry_after)} seconds to use to use this command again`*")
            await asyncio.sleep(5)
            await message.delete()
        else:
            raise(error)

    @commands.command(alaises=['pfp','picture','display picture'])
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            e = discord.Embed(title=f"{ctx.author.name}'s avatar" , color = 0xdb7bff)
            e.set_image(url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=e)

        else:
            e = discord.Embed(title=f"{member.name}'s avatar" , color = 0xdb7bff)
            e.set_image(url=f'{member.avatar_url}')
            await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1,10,commands.BucketType.user)
    async def cuddle(self,ctx,member:discord.Member):
        """Cuddles the mentioned user
        Even you could use userID or username instead of mentioning them"""
        if ctx.author == member:
            await ctx.send('How do you plan to cuddle yourself? :thinking:')
        else:
            e = discord.Embed(title=f'{ctx.author.name} cuddles {member.name} , so cute >~< ' , color = 0xdb7bff)
            content = ['https://media1.tenor.com/images/8f8ba3baeecdf28f3e0fa7d4ce1a8586/tenor.gif?itemid=12668750', 'https://i.imgur.com/VNhuTUT.gif',
            'https://media1.tenor.com/images/e07473d3cf372dbc24c760527740b85e/tenor.gif?itemid=12668884', 'https://media1.tenor.com/images/08de7ad3dcac4e10d27b2c203841a99f/tenor.gif?itemid=4885268'
            'https://i.pinimg.com/originals/d8/7c/5c/d87c5cdd0a68caf2b6feeec0f7da7315.gif']
            link = random.choice(content)
            e.set_image(url=f'{link}')
            await ctx.send(embed=e)
        await asyncio.sleep(3)





def setup(bot):
    bot.add_cog(Gif(bot))
