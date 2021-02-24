import json
import requests 
import random
import discord

client = discord.Client()

challenges = []
with open('Functionalities\challenges.json') as json_file:
    data = json.load(json_file)
    for c in data['challenges']:
        challenges.append(c)
    temp = data['challenges']

#adds new challenge to the challenge list
def write_json(data, filename='Functionalities\challenges.json'):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)

#this function gets you a challenge from the list of challenges and returns it as a string to be sent through chat.
def get_challenge():
    response = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{random.choice(challenges)}")
    json_data = json.loads(response.text)
    challenge = json_data['name']+ '\n' + 'Languages: ' +str(json_data['languages']) + '\n' + json_data['url']
    return challenge

#this function adds a new challenge to the challenges list
def new_challenge(challenge_url):
    challenge_id = challenge_url.split('/')[-3]
    if challenge_id not in challenges:
        temp.append(challenge_id)
        write_json(data)
        return f'Se añadio https://www.codewars.com/kata/{challenge_id} a la lista!'
    else:
        return 'El reto ya existe en nuestra base de datos!'        

#this function return our current challenge list
def get_challengeList():
    x = []
    for i in range(len(challenges)):
        response = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{challenges[i]}")
        json_data = json.loads(response.text)
        challenge = json_data['url']
        x.append(challenge)
    return x


