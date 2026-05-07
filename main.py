import discord
from discord.ext import commands
from dotenv import load_dotenv
import os



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


load_dotenv()
token = os.getenv("DISCORD_TOKEN")



@bot.event
async def on_ready():
    guild = discord.Object(id=1292276502867607642)
    await bot.tree.sync(guild=guild)
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


@bot.tree.command(name="echo", description="Echoes what you say")
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)


@bot.tree.command(name="echo", description="Echoes what you say", guild=discord.Object(id=GUILD_ID))
async def echo(interaction: discord.Interaction, message: str):
    embed = discord.Embed(
        title="Echo",
        description=message,
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)


bot.run(token)