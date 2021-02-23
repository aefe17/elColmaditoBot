import discord
import os
from discord import channel
from dotenv import load_dotenv
from Server.keep_alive import keep_alive
from Functionalities.quotes import get_quote
from Functionalities.challenge import get_challenge, new_challenge, get_challengeList
from discord.ext import commands

#Loads token to be read by discord library
load_dotenv()
Token_Key = os.getenv("DISCORD_TOKEN")

client = discord.Client()

#Bot Commands 
bot = commands.Bot(command_prefix = '$')

@bot.command(name='Hola', help= 'Sends help and greets user')
async def Hola(message):
    await message.author.send('¡Hola soy el bot del colmadito! Estos son mis comandos: \n$Hola: Te saludo y te doy mi lista de comandos disponibles \n$Quote: Te doy una cita inspiracional\n$Reto: Te envio un coding challenge')

@bot.command(name='Quote', help='Sends a inspirational Quote')
async def Quote(message):
    await message.send(f'Here is your quote: {get_quote()}')

@bot.command(name='challenge', help='Sends a coding challenge to the discord')
async def Reto(message):
    await message.send(f'Aqui esta el reto: {get_challenge()}')

@bot.command(name='challengeList', help='Returns Challenges list')
async def challengeList(message):
    # await message.channel.send(f'Esta es nuestra lista de retos acutal: {get_challengeList()}')
    await message.send(f'Aqui nuestra lista de retos: {get_challengeList()}')

@bot.command(name='addChallenge', help='Adds a new challenge into the challenges_list')
async def addChallenge(message):
    url = message.content.split(' ')[1]
    new_challenge(url)
    await message.channel.send('Added ' + url + ' to list!')

async def on_ready():
    print(f'We have logged in as {client.user}')

#runs server to keep alive the bot.
keep_alive()
on_ready()
#runs the bot and its commands with the provided token key.
bot.run(Token_Key)
client.run(Token_Key)