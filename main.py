import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

client = commands.Bot(command_prefix = '!')

token = "OTM5NzkxMDE0NzQxMjk5MjEx.Yf9-lg.adrhrX9RpuvMUc7Z1VYL3pdB4yo"

@client.command(pass_context=True)
async def clear(ctx, amont=100):
    channel = ctx.message.channel
    message = []
    async for message in client.log_from(channel, limit-int(amont)):
        message.append(message)
    await client.delete_messages(message)

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!help':
            await message.channel.send('!Agnaktor  !Glacial !Agnaktor  !Akantor  !Arzuros  1Barioth')
            await message.channel.send('!Sand Barioth  !Barroth  !Jade Barroth  !Bulldrome  !Deviljho')
            await message.channel.send('!Diablos  !Black Diablos  !Duramboros  !Gigginox  !Baleful Giggino')
            await message.channel.send('!Great Baggi  !Great Jaggi  !Great Wroggi  !Lagombi  !Nargacuga')
            await message.channel.send('!Green Nargacuga  !Nibelsnarf  !Qurupeco  !Crimson Qurupeco !Rathalos')
            await message.channel.send('!Silver Rathalos !Rathian  !Gold Rathian  !Royal Ludroth  !Purple Ludroth')
            await message.channel.send('!Tigrex  !Brute Tigrex  !Ukanlos  !Uragaan  !Steel Uragaan')
            await message.channel.send('!Volvidon  !Zinogre  !Alatreon  !Amatsu  !Jhen Mohran')
           

        if message.content == '!Agnaktor':
              await message.channel.send('https://static.wikia.nocookie.net/monsterhunter/images/4/4a/MHGen-Agnaktor_Render_001.png/revision/latest/scale-to-width-down/350?cb=20160216154811')
              await message.channel.send('https://static.wikia.nocookie.net/monsterhunter/images/1/1a/DMG-Agnaktor.png/revision/latest/scale-to-width-down/760?cb=20100712064900')
              await message.channel.send('https://cdn.discordapp.com/attachments/700558744211423245/958353494354567279/unknown.png')


        if message.content.startswith('!Agnaktor'):
        #title
           embedVar = discord.Embed(title="Agnaktor", color=0xE67E22)

       #object
           embedVar.set_thumbnail(url='https://static.wikia.nocookie.net/monsterhunter/images/6/64/MHXR-Purgatory_Agnaktor_Icon.png/revision/latest/scale-to-width-down/128?cb=20190328020518')
           embedVar.set_footer(text='จุดสำคัญ')
           embedVar.set_image(url='https://static.wikia.nocookie.net/monsterhunter/images/9/9e/Agnaktor-Wounded.png/revision/latest/scale-to-width-down/972?cb=20100615075005')
           await message.channel.send(embed=embedVar)


        if message.content == ('!Arzuros'):
            await message.channel.send('https://static.wikia.nocookie.net/monsterhunter/images/e/ed/MHRise-Arzuros_Render_001.png/revision/latest/scale-to-width-down/350?cb=20210323140920')
            
        if message.content == ('!Arzuros'):
            await message.channel.send('______________________________________*******************Hitzone Damage Data*******************______________________________')

        if message.content.startswith('!Arzuros'):
        #title
           embedVar = discord.Embed(title="Arzuros", color=0x2879EC)

       #object
           embedVar.set_footer(text='จุดสำคัญ')
           embedVar.set_thumbnail(url='https://static.wikia.nocookie.net/monsterhunter/images/5/52/MHP3-Arzuros_Icon.png/revision/latest/scale-to-width-down/62?cb=20160623223638')
           embedVar.set_image(url='https://cdn.discordapp.com/attachments/700558744211423245/957297503630405773/unknown.png')
           await message.channel.send(embed=embedVar)
        


        if message.content == ('!Rathian'):
            await message.channel.send('https://static.wikia.nocookie.net/monsterhunter/images/b/be/MHRise-Rathian_Render_001.png/revision/latest/scale-to-width-down/350?cb=20210217224035')
            await message.channel.send('https://static.wikia.nocookie.net/monsterhunter/images/f/f2/DMG-Rathian.png/revision/latest/scale-to-width-down/700?cb=20100809023513')

        if message.content == ('!Rathian'):
            await message.channel.send('Hitzone	Fire	Water	Thunder	Ice	Dragon')
            await message.channel.send('Head	      0	       15	         20	       15	       35')
            await message.channel.send('Neck	      0           10	         15	       10	        20')
            await message.channel.send('Stomach   0	         5	         20	       5	         10')
            await message.channel.send('Tail	        0	          5	         10	       5	         25')
            await message.channel.send('Wing	     0	        10	         15	       10	       20')
            await message.channel.send('Foot	       0	          5	         10	        5	        10')

        if message.content.startswith('!Rathian'):
        #title
           embedVar = discord.Embed(title="Rathian", color=0x2879EC)

       #object
           embedVar.set_footer(text='จุดสำคัญ')
           embedVar.set_thumbnail(url='https://static.wikia.nocookie.net/monsterhunter/images/1/14/MHP3-Rathian_Icon.png/revision/latest/scale-to-width-down/62?cb=20160623224803')
           embedVar.set_image(url='https://cdn.discordapp.com/attachments/700558744211423245/957997797838315570/unknown.png')
           await message.channel.send(embed=embedVar)
        
        if message.content.startswith('!Tigrex'):
        #title
           embedVar = discord.Embed(title="Tigrex", color=0x2879EC)

       #object
           embedVar.set_footer(text='จุดสำคัญ')
           embedVar.set_thumbnail(url='https://static.wikia.nocookie.net/monsterhunter/images/5/5a/MHP3-Tigrex_Icon.png/revision/latest/scale-to-width-down/62?cb=20160623225006')
           embedVar.set_image(url='https://media.discordapp.net/attachments/849108734768316456/957272204800851988/unknown.png?width=488&height=676')
           await message.channel.send(embed=embedVar)

        if message.content == ('!Barioth'):
            await message.channel.send('https://static.wikia.nocookie.net/monsterhunter/images/2/2f/MHRise-Barioth_Render_001.png/revision/latest/scale-to-width-down/350?cb=20210107151601')
            await message.channel.send('https://static.wikia.nocookie.net/monsterhunter/images/8/8a/DMG-Barioth.png/revision/latest/scale-to-width-down/700?cb=20100709122209')
            await message.channel.send('______________________________________*******************Hitzone Damage Data*******************______________________________')

        if message.content.startswith('!Barioth'):
        #title
           embedVar = discord.Embed(title="Barioth", color=0x2879EC)

       #object
           embedVar.set_footer(text='จุดสำคัญ')
           embedVar.set_thumbnail(url='https://static.wikia.nocookie.net/monsterhunter/images/0/08/MHP3-Barioth_Icon.png/revision/latest/scale-to-width-down/62?cb=20160623223639')
           embedVar.set_image(url='https://cdn.discordapp.com/attachments/700558744211423245/958356136283738142/unknown.png')
           await message.channel.send(embed=embedVar)

    
       








client = MyClient()
client.run(token)