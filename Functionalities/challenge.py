import json
import requests 
import random

challenges = ['5865dd726b56998ec4000185', '555eded1ad94b00403000071', '517abf86da9663f1d2000003',
              '55bf01e5a717a0d57e0000ec', '55e2adece53b4cdcb900006c', '523a86aa4230ebb5420001e1',
              '55466989aeecab5aac00003e', '555615a77ebc7c2c8a0000b8', '521c2db8ddc89b9b7a0000c1',
              '550527b108b86f700000073f', '5324945e2ece5e1f32000370', '54a91a4883a7de5d7800009c']

#this function gets you a challenge from the list of challenges and returns it as a string to be sent through chat.

def get_challenge():
    response = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{random.choice(challenges)}")
    json_data = json.loads(response.text)
    challenge = json_data['name']+ '\n' + 'Languages: ' +str(json_data['languages']) + '\n' + json_data['url']
    return challenge

#this function adds a new challenge to the challenges list
def new_challenge(challenge_url):
    challenge_id = challenge_url.split('/')[-3]
    challenges.append(challenge_id)

def get_challengeList():
    x = []
    for i in range(len(challenges)):
        response = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{challenges[i]}")
        json_data = json.loads(response.text)
        challenge = json_data['url']
        x.append(challenge)
    return x