import discord # 개발자 캠트(camt4372)
import random # 팔면 뒤짐^^

intents = discord.Intents.all()

client = discord.Client(intents=intents)

# !재고추가 쓰게가능하게할 역할아이디 넣으세요.
allowed_role_id = 1128306617759309912

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == 1128306619000828008 and not message.author.bot: # 아이디는 아무말이나 입력해도 젠되는 채널아이디
        await message.channel.trigger_typing()  # ~입력중 표시되게하는건데 싫으면 이부분 지우삼

        with open('gen.txt', 'r') as f:
            lines = f.read().strip().split('\n')

        if not lines or (len(lines) == 1 and lines[0].strip() == ''):
            embed = discord.Embed(title="재고 부족!", description="재고가 부족합니다! 관리자에게 문의해주세요.", color=discord.Color.red())
            await message.reply(embed=embed)
            return

        chosen = random.choice(lines)
        lines.remove(chosen)

        with open('gen.txt', 'w') as f:
            f.write('\n'.join(lines))

        embed_success = discord.Embed(title="무료 젠 성공!", description=f"||{chosen}||", color=discord.Color.green())
        embed_success.set_footer(text="Made By.camt4372")
        await message.author.send(embed=embed_success)

        embed_reply = discord.Embed(title="DM을 확인해주세요", description=f"남은 재고 수: `{len(lines)}`개", color=discord.Color.blue())
        await message.reply(embed=embed_reply)

    elif message.content.startswith('!재고추가'):
        await message.channel.trigger_typing()
        # ~입력중 표시되게하는건데 싫으면 이부분 지우삼
        if allowed_role_id in [role.id for role in message.author.roles]:
            content = message.content[len('!재고추가 '):].strip()
            if content:
                with open('gen.txt', 'a') as f:
                    f.write(content + '\n')  # "!재고추가 [내용]" 하면 내용이 자동으로 gen.txt에 들어가짐

                embed = discord.Embed(title="재고추가 성공!", description="재고가 추가되었습니다.", color=discord.Color.green())
                await message.reply(embed=embed)
            else:
                embed = discord.Embed(title="재고추가 실패!", description="내용을 입력해주세요.", color=discord.Color.red())
                await message.reply(embed=embed)
        else:
            embed = discord.Embed(title="권한 없음!", description="이 명령어는 특정 역할만 사용 가능합니다.", color=discord.Color.red())
            await message.reply(embed=embed)

TOKEN = "" # 님 봇 토큰 넣어요
client.run(TOKEN)
