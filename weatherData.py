import discord
from discord import message;

key_features = {'temp':'Temperature', 'feels_like':'Feels Like', 'temp_min':'Min. Temperature', 'temp_max':'Max. Temperature'}

def weather(data):
    data = data['main']
    del data['pressure']
    del data['humidity']
    return data

def command(data, location):
    location=location.title()
    message=discord.Embed(title=f'Weather of {location}', description=f'{location} Weather', color=0x0000FF)
    for key in data:
        message.add_field(name=key_features[key], value=str(data[key]), inline=False)
    return message

def error(location):
    location=location.title
    return discord.Embed(title='Error', description='Sorry, no location with that name', color=0x0000FF)