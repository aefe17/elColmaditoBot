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
@bot.command(name='Comandos', help= 'Sends help and greets user')
async def Comandos(message):
    await message.author.send('¡Hola soy el bot del colmadito! Estos son mis comandos: \n$Comandos: Te doy mi lista de comandos disponibles \n$Cita: Te doy una cita inspiracional\n$Challenge: Te envio un coding challenge \n$challengeList: Te muestro nuestra lista actual de retos \n$addChallenge: Añado tu reto a tu lista de retos')
@bot.command(name='Cita', help='Sends a inspirational Quote')
async def Cita(message):
    await message.send(f'Here is your quote: {get_quote()}')
@bot.command(name='Challenge', help='Sends a coding challenge to the discord')
async def Challenge(message):
    await message.send(f'Aqui esta el reto: {get_challenge()}')
@bot.command(name='challengeList', help='Returns Challenges list')
async def challengeList(message):
    await message.send(f'Aqui nuestra lista de retos: {get_challengeList()}')
@bot.command(name='addChallenge', help='Adds a new challenge into the challenges_list')
async def addChallenge(message):
    url = message.message.content.split(' ')[1]
    await message.channel.send(new_challenge(url))

#runs server to keep alive the bot.
keep_alive()
#runs the bot and its commands with the provided token key.
bot.run(Token_Key)
client.run(Token_Key)