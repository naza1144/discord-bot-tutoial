import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

token = "OTM5NzkxMDE0NzQxMjk5MjEx.Yf9-lg.adrhrX9RpuvMUc7Z1VYL3pdB4yo"




@client.event
async def on_ready():
    print('Bot is ready')


@client.command(pass_context=True)
async def clear(ctx, amont=100):
    channel = ctx.message.channel
    message = []
    async for message in client.log_from(channel, limit-int(amont)):
        message.append(message)
    await client.delete_messages(message)


@client.event
async def on_message(message):
    if message.content.startswith('!Agnaktor'):
        #title
        embedVar = discord.Embed(title="Agnaktor", color=0xE67E22)

       #object
        embedVar.set_thumbnail(url='https://static.wikia.nocookie.net/monsterhunter/images/6/64/MHXR-Purgatory_Agnaktor_Icon.png/revision/latest/scale-to-width-down/128?cb=20190328020518')
        embedVar.set_footer(text='จุดสำคัญ')
        embedVar.set_image(url='https://static.wikia.nocookie.net/monsterhunter/images/1/1a/DMG-Agnaktor.png/revision/latest/scale-to-width-down/760?cb=20100712064900')
        await message.channel.send(embed=embedVar)

    elif message.content.startswith('+Agnaktor'):
        #title
        embedVar = discord.Embed(title="Agnaktor", color=0xE67E22)

       #object
        embedVar.set_footer(text='ความเสียหายธาตุของเเต่ละส่วน')
        embedVar.set_image(url='https://media.discordapp.net/attachments/700558744211423245/957293815620857926/unknown.png')
        await message.channel.send(embed=embedVar)

    elif message.content.startswith('!Tigrex'):
        #title
        embedVar = discord.Embed(title="Tigrex'", color=0x2879EC)

       #object
        embedVar.set_footer(text='จุดสำคัญ')
        embedVar.set_thumbnail(url='https://static.wikia.nocookie.net/monsterhunter/images/5/5a/MHP3-Tigrex_Icon.png/revision/latest/scale-to-width-down/62?cb=20160623225006')
        embedVar.set_image(url='https://media.discordapp.net/attachments/849108734768316456/957272204800851988/unknown.png?width=488&height=676')
        await message.channel.send(embed=embedVar)

    elif message.content.startswith('+Tigrex'):
        #title
        embedVar = discord.Embed(title="Tigrex'", color=0x2879EC)

       #object
        embedVar.set_footer(text='ความเสียหายธาตุของเเต่ละส่วน')
        embedVar.set_image(url='https://cdn.discordapp.com/attachments/700558744211423245/957295685487714425/unknown.png')
        await message.channel.send(embed=embedVar)
   
    elif message.content.startswith('!Arzuros'):
        #title
        embedVar = discord.Embed(title="Arzuros", color=0x2879EC)

       #object
        embedVar.set_footer(text='จุดสำคัญ')
        embedVar.set_thumbnail(url='https://static.wikia.nocookie.net/monsterhunter/images/5/52/MHP3-Arzuros_Icon.png/revision/latest/scale-to-width-down/62?cb=20160623223638')
        embedVar.set_image(url='https://cdn.discordapp.com/attachments/700558744211423245/957297503630405773/unknown.png')
        await message.channel.send(embed=embedVar)
    


















client.run(token)