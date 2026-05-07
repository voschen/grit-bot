import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

with open("dictionary.json", "r") as f:
    concepts = json.load(f)

@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


@bot.tree.command(name="cracked_glass", description="Information about the cracked glass effect", guild=discord.Object(id=GUILD_ID))
async def echo(interaction: discord.Interaction):
    data = concepts["cracked_glass"]
    embed = discord.Embed(
        title=data["title"],
        description= data["description"],
        color=discord.Color.blue()
    )
    for field in data["fields"]:
        embed.add_field(name = field["name"], value=field["value"], inline=False)
    await interaction.response.send_message(embed=embed)


bot.run(token)