import discord
import asyncio
from discord.ext import commands


#
# Any issues feel free to message my discord Otter#7070
#

bot = commands.Bot(command_prefix='!', self_bot=True)
token = "" #<<--- put your token here
prefix = "#"
command = "gl"
leaveMessage = "Bye!"

@bot.event
async def on_ready():
    print("Token Verification Successful! Type " + prefix + "" + command + " in to any chat and the script will execute!") # Tell the user the script is actually running.

@bot.event
async def on_message(message):
    if message.author == bot.user:
        cmd = str(message.content).split(' ')
        if cmd[0] == prefix + command:
            await message.delete()
            count = 0
            for channel in bot.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if channel.id != message.channel.id: # If the message was sent in a group chat, dont leave it.
                        count = count + 1
                        await channel.send(leaveMessage)
                        await channel.leave()
                        print("Left a group: " + str(channel.id)) # Print group ID in console.
            await message.channel.send("``You left a total of [" + str(count) + "] group chats!``")
            await bot.close() # Updated because they changed it for some reason
bot.run(token, bot=False)
input("Press enter to exit") # Allow user to actually fucking read the data before the script closes.
