import discord
from discord.ext import commands
import database

class TaskCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_task(self, ctx, *, description):
        database.add_task(description)
        await ctx.send(f"Tugas ditambahkan: {description}")

    @commands.command()
    async def delete_task(self, ctx, task_id: int):
        database.delete_task(task_id)
        await ctx.send(f"Tugas dengan ID {task_id} telah dihapus.")

    @commands.command()
    async def show_tasks(self, ctx):
        tasks = database.get_all_tasks()
        if not tasks:
            await ctx.send("Tidak ada tugas.")
        else:
            msg = "\n".join(
                [f"{t[0]}. {'✅' if t[2] else '❌'} {t[1]}" for t in tasks]
            )
            await ctx.send(f"Daftar Tugas:\n{msg}")

    @commands.command()
    async def complete_task(self, ctx, task_id: int):
        database.complete_task(task_id)
        await ctx.send(f"Tugas dengan ID {task_id} ditandai sebagai selesai.")
