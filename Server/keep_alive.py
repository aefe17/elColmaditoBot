from flask import Flask
from threading import Thread

#This file keeps the bot alive. 

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
    app.run(host='0.0.0.0', port=(5500))

def keep_alive():
    t = Thread(target=run)
    t.start()