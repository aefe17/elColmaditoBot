import discord
import os
from discord import channel
from dotenv import load_dotenv
from Server.keep_alive import keep_alive
from Functionalities.quotes import get_quote
from Functionalities.challenge import get_challenge
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
@bot.command(name='Challenge', help='Sends a coding challenge to the discord')
async def Reto(message):
    await message.send(f'Aqui esta el reto: {get_challenge()}')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#runs server to keep alive the bot.
keep_alive()
#runs the bot and its commands with the provided token key.
bot.run(Token_Key)
client.run(Token_Key)