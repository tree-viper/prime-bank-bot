import discord
from discord.ext import commands
import config

client = commands.Bot(command_prefix = '^')

@client.event
async def on_ready():
    print('Bot is ready.')



async def isMessage(channelID): #checks whether there are any messages in the channel, if not returns false, if yes returns the id of the message
    channel = client.get_channel(channelID)
    messages = 0
    messageID = ''
    async for x in client.logs_from(channel):
        messages = messages + 1
        messageID = x.id
    if messages == 0:
        return False
    else:
        return messageID

client.run(config.TOKEN)