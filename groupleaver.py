import discord
import asyncio

#
# Any issues feel free to message my discord Otter7070
#

client = discord.Client()
token = "" # Put your token here
prefix = "#"
command = "gl"
leaveMessage = "Bye!"

@client.event
async def on_ready():
    print("Token Verification Successful! Type " + prefix + "" + command + " in to any chat and the script will execute!") # Tell the user the script is actually running.

@client.event
async def on_message(message):
    if message.author == client.user:
        cmd = str(message.content).split(' ')
        if cmd[0] == prefix + command:
            await message.delete()
            count = 0
            for channel in client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if channel.id != message.channel.id: # If the message was sent in a group chat, dont leave it.
                        count = count + 1
                        await channel.send(leaveMessage)
                        await channel.leave()
                        print("Left a group: " + str(channel.id)) # Print group ID in console.
            await message.channel.send("``You left a total of [" + str(count) + "] group chats!``")
            await client.close() # Updated because they changed it for some reason

# If you are getting an improper token error or 401 code, make sure you have no greater than version 1.7.3 of discord.py installed!

client.run(token, bot=False)
input("Press enter to exit") # Allow user to actually fucking read the data before the script closes.
