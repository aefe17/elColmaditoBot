import discord
import os
from discord import channel
from dotenv import load_dotenv
from Server.keep_alive import keep_alive
from Functionalities.quotes import get_quote
from Functionalities.challenge import get_challenge, new_challenge

#Loads token to be read by discord library
load_dotenv()
Token_Key = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('$hola'): 
        await message.author.send('¡Hola soy el bot del colmadito! Estos son mis comandos: \n$hola: Te saludo y te doy mi lista de comandos disponibles \n$quote: Te doy un quote \n$reto: Te envio un coding challenge')
    if message.content.startswith('$quote'):
        await message.channel.send(f'Here is your quote: {get_quote()}')
    if message.content.startswith('$reto'):
        print('Reto xD')
        await message.channel.send(f'Aqui esta el reto: {get_challenge()}')
    if message.content.startswith('$add_challenge'):
        url = message.content.split(' ')[1]
        new_challenge(url)
        await message.channel.send('Added ' + url + ' to list!')

keep_alive()
client.run(Token_Key)
