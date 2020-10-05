import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!') #bot commands prefix
TOKEN = os.getenv("DISCORD_TOKEN")

path = os.path.dirname(__file__)

@bot.event
async def on_ready(): #activates when bot is ready to work
    print(f'--------------------------------')
    print(f'wndrx is ready') 
    print(f'user name: {bot.user.name}')
    print(f'user id: {bot.user.id}')
    print(f'--------------------------------')

    game = discord.Game("kill mankind")
    await bot.change_presence(status = discord.Status.idle, activity = game)


@bot.command() #loads cogs
async def load_ext(ctx, ext):
    bot.load_extension(f'cogs.{ext}')


@bot.command() #unload cogs
async def unload_ext(ctx, ext):
    bot.unload_extension(f'cogs.{ext}')


for filename in os.listdir(path + '/cogs'): #auto activate all cogs from /cogs directory
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)
