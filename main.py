import discord
import os
import requests
import json
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
client = discord.Client()
Token_Key = os.getenv("DISCORD_TOKEN")


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('$hello'):
        await message.channel.send("Hello! I'm Encourage Bot")
    if message.content.startswith('$quote'):
        await message.channel.send(f'Here is your quote: {get_quote()}')
    if message.content.startswith('$salute'):
        await message.channel.send("Klk menol, somo un bo' pa hace senti mejol :v")

keep_alive()
client.run(Token_Key)