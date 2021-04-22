import discord
import os
from discord.ext import commands






client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(
        type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"
    ))
    print("ready")



@client.event
async def on_message(message):
 if message.content.startswith ("c!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제됨", description="메시지 {}개가\n관리자 {}님에 의해 삭제되었습니다.".format(amount, message.author), color=0xE74C3C)
            embed.set_footer(text="개발자 ㄹㅇㅋㅋ#4359", icon_url="https://cdn.discordapp.com/attachments/763628372713930765/831523720114733066/ab778a5905f2c6cab34b61751340fcf0.png")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

 if message.content.startswith ("c!help"):
     embed = discord.Embed(title="명령어 도움", description="명령어 사용법 안내", color=0xE67E22)
     embed.add_field(name="c!청소 : 특정 메시지를 삭제합니다", value="`c!청소 [지우고 싶은 메시지 겟수]`",inline=False)
     embed.add_field(name="c!help : 이 메시지를 보넵니다", value="`명령어 사용법 안내`",inline=False)
     embed.add_field(name="기타", value="[봇 초대하기](https://discord.com/api/oauth2/authorize?client_id=831516504968265778&permissions=8&scope=bot)",inline=False)
     embed.set_footer(text="개발자 ㄹㅇㅋㅋ#4359")
     await message.channel.send(embed=embed)
 if message.content.startswith ("c! 청소"):
     embed = discord.Embed(title="알림", description="  ", color=0xE67E22)
     embed.add_field(name="올바른 사용법", value="`c!청소 [지우고 싶은 메시지 겟수]`",inline=False)
     embed.set_footer(text="개발자 ㄹㅇㅋㅋ#4359")
     await message.channel.send(embed=embed)








access_token = os.environ['BOT_TOKEN']
client.run(access_token)
