import discord
import asyncio

client = discord.Client()
token = "" # Put your token here
prefix = "#"
leaveMessage = "Bye!"

@client.event
async def on_message(message):
    if message.author == client.user:
        cmd = str(message.content).split(' ')
        if cmd[0] == prefix + "gl":
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
