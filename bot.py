import discord
from discord import app_commands
from discord.ext import commands
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="hug", description="Give someone a hug!")
@app_commands.describe(user="The person to hug")
async def hug(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f"{interaction.user.mention} hugs {user.mention} 🤗")

@bot.tree.command(name="wave", description="Wave at someone!")
@app_commands.describe(user="The person to wave at")
async def wave(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f"{interaction.user.mention} waves at {user.mention} 👋")

@bot.tree.command(name="8ball", description="Ask the magic 8-ball a question")
@app_commands.describe(question="Your question")
async def eight_ball(interaction: discord.Interaction, question: str):
    responses = [
        "Yes", "No", "Maybe", "Ask again later", "Definitely"
    ]
    answer = random.choice(responses)
    await interaction.response.send_message(f"🎱 {answer}")

@bot.tree.command(name="userinfo", description="Get info about a user")
@app_commands.describe(user="User to get info on")
async def userinfo(interaction: discord.Interaction, user: discord.Member = None):
    user = user or interaction.user
    embed = discord.Embed(title="User Info", color=discord.Color.blue())
    embed.set_thumbnail(url=user.avatar.url if user.avatar else user.default_avatar.url)
    embed.add_field(name="Username", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    await interaction.response.send_message(embed=embed)

bot.run(1184777708341829705)
