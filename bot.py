import discord
from discord.ext import commands
import database
from commands import TaskCommands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    database.init_db()

bot.add_cog(TaskCommands(bot))

bot.run("YOUR_DISCORD_BOT_TOKEN")
