## Name: Corey Everett
## Date: March 12th, 2019
## Program: E.T.O.R.Y.
## Purpose: It's just a simple chat program, do you have more deliverables?

## Import Discord Tools
import discord, discord.ext.commands, time, asyncio
from discord.ext.commands import Bot
from discord.ext import commands

## Import NLTK tools
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


Client = discord.Client()

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():  ## When program executes and "is ready".
    print("E.T.O.R.Y. is active.")


@client.event
async def on_message(message):  ## When E.T.O.R.Y. receives a message.

    ##Initial data changing used to increase computation speed.
    userMessage = message.content.lower()

    ## Will not count any words said by the bot, to avoid recursive spamming (COOKIE ATTACK)
    if message.author == client.user:
        return

    stop_words = set(stopwords.words("english"))

    words = word_tokenize(userMessage)

    filtered_sentence = {w for w in words if not w in stop_words}

  ##  await client.send_message(message.channel, words)
   ## await client.send_message(message.channel, filtered_sentence)

    ## E.T.O.R.Y. testing "Twilight Zone"
    if "cookie" in userMessage:
         await client.send_message(message.channel, ":cookie:")

    if "help me with" in userMessage:
         await client.send_message(message.channel, "*Oooooh, no.* I am **not** getting involved in this presentation. This is all on you.")

    if "serious" or "seriously" in userMessage:
        await client.send_message(message.channel, "Uh, *yeah.* I have too much to do, like being fictional. Have fun angering everyone with your terrible presentation skills!")







## Login info of the bot
client.run("NTU0NDQzNDQzMzEzNTczODk4.D2c9rg.Is1W8oYKAUm-ohp6vHxl4XRSE1A")