from weatherData import *
import discord
import requests
import json

#Client
id='ODYwODAyNzgwOTY0ODQ3NjM2.YOAjDw.dq2BBsFbn0vf23QsRCHCbYuiQv0'
com_prefix='w.'
api_key='adb375e170180136848707f760d75dd3'
client = discord.Client()  

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{com_prefix}[location]'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(com_prefix):
        location=message.content.replace(com_prefix,'')
        if len(location) >= 1:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            try:
                data = json.loads(requests.get(url).content)
                data=weather(data)
                await message.channel.send(embed=command(data,location))
            except KeyError:
                await message.channel.send(embed=error(location))

#Running the client on server
client.run(id)
