# =========================================
# FICHIER : ia/kai.py
# =========================================

import discord
from discord.ext import commands

from ia.emotions import get_current_mood
from ia.responses import (
    get_response,
    get_welcome_message
)
from ia.memory import (
    remember_user
)
from ia.triggers import detect_kai

# =========================================
# CONFIG
# =========================================

TOKEN = "TON_TOKEN_ICI"

GENERAL_CHANNEL_NAME = "general"

# =========================================
# INTENTS
# =========================================

intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# =========================================
# READY
# =========================================

@bot.event
async def on_ready():

    print("=" * 50)
    print(f"{bot.user} est connecté.")
    print("Kai est maintenant actif.")
    print("=" * 50)

# =========================================
# WELCOME SYSTEM
# =========================================

@bot.event
async def on_member_join(member):

    remember_user(
        member.id,
        member.name
    )

    channel = discord.utils.get(
        member.guild.text_channels,
        name=GENERAL_CHANNEL_NAME
    )

    if channel:

        await channel.send(
            get_welcome_message(
                member.mention
            )
        )

# =========================================
# IA MESSAGE SYSTEM
# =========================================

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    if detect_kai(message.content):

        mood = get_current_mood()

        response = get_response(
            mood,
            message.author.mention
        )

        await message.reply(response)

    await bot.process_commands(message)

# =========================================
# COMMANDES
# =========================================

@bot.command()
async def humeur(ctx):

    mood = get_current_mood()

    await ctx.send(
        f"Humeur actuelle de Kai : {mood}"
    )

@bot.command()
async def ping(ctx):

    latency = round(bot.latency * 1000)

    await ctx.send(
        f"🏓 Pong : {latency}ms"
    )

# =========================================
# START BOT
# =========================================

bot.run(TOKEN)
