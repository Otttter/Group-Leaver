import discord
import asyncio

#
# Any issues feel free to message my discord Otter#7070
# or join my server https://discord.gg/G5ACnxn68z

client = discord.Client()
token = "" # Put your token here
prefix = "#"
command = "gl"
leaveMessage = "Bye!"

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
            await message.channel.send("``You left a total of [" + str(count) + "] group chats!``")
            await client.logout()
            exit(1)

client.run(token, bot=False)
