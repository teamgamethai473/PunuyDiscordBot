import discord
import os
import sys
import random
import time
import requests
import json
import asyncio
#import lavalink
from discord.ext import commands

bot = commands.Bot(command_prefix='p!')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("________   _____  _____  ____   ___   ___   ___   ___    ___     ", end ="")
    print(" ______       _____      ________   ")
    print("|   _   \  |   |  |   |  |   \  | |  |   |  |  |  \  \  /  /     ", end ="")
    print("|  ___ \     /  __ \    |        |  ")
    print("|  |__| |  |   |  |   |  |    \ | |  |   |  |  |   \  \/  /      ", end ="")
    print("| |___| |   /  /  \ \   |__    __|  ")
    print("|   ____/  |   |  |   |  |  |\ \| |  |   |  |  |    \    /       ", end ="")
    print("|  ___  /   |  |  | |      |  |     ")
    print("|  |       \   \__/   /  |  | \   |  \   \__/  /    |   |        ", end ="")
    print("| |___| |   \  \__/ /      |  |     ")
    print("|__|        \________/   |__|  \__|   \_______/     |___|        ", end ="")
    print("|_______/    \_____/       |__|      ")
    print("PunuyBot", end ="")
    print(f' v 1.0.0')
    print(bot.user.name)
    print(bot.user.id)
    print(f'--> Start Now <--')
    #bot.load_extension('music')
    await bot.change_presence(activity=discord.Game('> Love MaidRuri <'))

    try :
        result = sys.argv[1]
    except :
        result = ""

    if result == '--reboot' :
        user_speical = await bot.fetch_user("301178730196238339")
        await user_speical.send("Reboot Success!")
    else :
        pass

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "⏩-ยินดีต้อนรับ":
            await channel.send("Welcome to the server")

@bot.event
async def on_member_leave(member):
    for channel in member.guild.channels:
        if str(channel) == "⏩-ยินดีต้อนรับ":
            await channel.send("Bye Bye T_T")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    author = message.author
    channel = message.channel
    server = message.guild
    print(f' ')
    print(message.author , end=" => ")
    print(message.content)
    print(message.channel , end=" IN ")
    print(message.guild)

    whatpunuy = ['ปุย','ปุ่ย','ปุ๊ย','ปุ้ย','ปุ๋ย']
    msg = ['ควย','ฆวย','kuy','kouy']
    msg1 = ['สัส','เฮี่ย']

    i = 0
    for x in whatpunuy :
        if whatpunuy[i] in message.content.lower():
            await message.channel.send('อะไรรึ ??')
            break
        else :
            i += 1
    
    i = 0
    for x in msg :
        if msg[i] in message.content.lower() : 
            msg_send = await message.channel.send('**__ค-ย พ่อง มึง อะ__**')
            time.sleep(0.5)
            await message.delete()
            time.sleep(0.5)
            await msg_send.delete()
            break
        else :
            i += 1

    i = 0
    for x in msg1 :
        if msg1[i] in message.content.lower() : 
            msg1_send = await message.channel.send('**__เป็น ค-ย ไร หล่ะ__**')
            time.sleep(0.5)
            await message.delete()
            time.sleep(0.5)
            await msg1_send.delete()
            break
        else :
            i += 1

    if 'yes' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('Yes Boi !!! :open_mouth: :point_left:')
        else :
          return

        if 'ที่รัก' in message.content.lower():
            if str(message.author) != 'This is Punuy#9684' :
                await message.channel.send('ค้าบ ที่ร๊ากก ^^ :heart: :heart:')
            else :
                return

    if 'เหงา' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('ผมไม่เหงาอะ')
          await message.channel.send('มีเมดสุดที่รักอยู่ข้างๆแล้ว ^-^ :heart: :heart:')
        else :
          return

    if 'แหม่' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('อิอิ ^-^')
        else :
          return

    if 'happy birthday' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('Happy Birthday! :balloon::tada:')
        else :
          return

    if 'padoru' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
            await message.channel.send('HASHIRE SORI YO')
            time.sleep(0.8)
            await message.channel.send('KAZE NO YOU NI')
            time.sleep(0.8)
            await message.channel.send('TSUKIMIHARA WO')
            time.sleep(0.8)
            await message.channel.send('**PADORU PADORU !!!**')
        else :
          return

    if '-p' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('เพลงถูกเพิ่มใน Groovy BOT แล้ว :ok_hand:')
        else :
          return

    if '-s' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('ใช้ -skip จร๊ะ :thinking: :thinking:')
        else :
          return

    if 'hm' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('**HMMMMMM !!!**')
        else :
          return

    if 'อั้ยยะ' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('ชั่ย ชั่ย :sunglasses: :sunglasses:')
        else :
          return

    if 'เอ้า' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('อารายย อารายย ')
        else :
          return

    if 'แช่ง' in message.content.lower():
        if str(message.author) != 'This is Punuy#9684' :
          await message.channel.send('จะไม่ขอแก้แค้น แต่ขอแช่งเธอเอาไว้ให้')
          time.sleep(0.5)
          await message.channel.send('ตกน้ำ')
          time.sleep(0.5)
          await message.channel.send('ตกรถ')
          time.sleep(0.5)
          await message.channel.send('ตกท่าน้ำ')
          time.sleep(0.7)
          await message.channel.send('ตกเครื่องบิน')
          time.sleep(0.3)
          await message.channel.send('ตกโต๊ะ')
          time.sleep(0.5)
          await message.channel.send('ตกเตียง')
          time.sleep(0.5)
          await message.channel.send('ตกตู้')
          time.sleep(0.5)
          await message.channel.send('ตกสอบ')
          time.sleep(0.5)
          await message.channel.send('สอบตก')
          time.sleep(0.5)
          await message.channel.send('ให้คางคกกัด')
          time.sleep(0.5)
          await message.channel.send('ให้งูรัด')
          time.sleep(0.5)
          await message.channel.send('ให้โดนพัดลมบาดมือ')
          time.sleep(0.5)
          await message.channel.send('บาดนิ้ว')
          time.sleep(0.5)
          await message.channel.send('และบาดแขน')
          time.sleep(0.7)
          await message.channel.send('บาดขา')
          time.sleep(0.5)
          await message.channel.send('สิวขึ้นหน้า')
          time.sleep(0.2)
          await message.channel.send('ฝ้าขึ้นหลัง')
          time.sleep(0.2)
          await message.channel.send('ลามขึ้นคอ')
          time.sleep(0.5)
          await message.channel.send('ยังไม่พอ')
          time.sleep(0.5)
          await message.channel.send('ขอให้อกหักไม่พบรัก')
          time.sleep(0.8)
          await message.channel.send('ทุกชาติ')
          time.sleep(0.5)
          await message.channel.send('ทุกชาติไป =_=')
        else :
          return

@bot.command()
async def ping(ctx):
    await ctx.send(f'**PONG!** {round(bot.latency * 1000)}ms')

@bot.command()
async def ปิง(ctx):
    await ctx.send(f'**พ่อง!** {round(bot.latency * 1000)}ms')

@bot.command()
async def clear (ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command(aliases=['h'])
async def help(ctx):
#    author = ctx.author

    embed=discord.Embed(
        title="PunuyBot | คำสั่งช่วยเหลือ", 
        color=0x78e40c
    )
    
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652568046900215823/654737485607338033/639815524339154945.png")

    embed.add_field(name='**__ตัวสั่งคอมแมน__** | **__Prefix__**' ,
    value=" p!" , inline=False)

    embed.add_field(name='**__คำสั่งทั่วไป__** | **__command__**' ,
    value=" help \n ping \n ปิง \n random \n support", inline=False)

    embed.add_field(name='**__สุ่มรูปโดย Punuy__** | **__Randoms Pic. By Punuy__**' ,
    value=" punuy \n fox \n cat", inline=False)

    embed.add_field(name='**__สุ่ม ความรู้สึก__**             | \n**__ใช้ random/rd__**           |' ,
    value=" smug \n tickle \n poke \n neko \n lizard \n hug \n feed \n cattext \n 8Ball" , inline=True)

    embed.add_field(name='**__Randoms Feeling__** \n **__Use random/rd__**' ,
    value=" baka \n slap \n pat \n meow \n kiss \n woof \n spoiler \n kemonomim" , inline=True)

    embed.add_field(name='** ** \n ** **' ,
    value=" foxGirl \n cuddle \n owoify \n fact \n nekogif \n holo \n why \n chat" , inline=True)

    embed.add_field(name='**__NSFW ZONE!!!__** | **__DAN__**' ,
    value=" ||randomHentaiGif|| \n ||pussy|| \n ||lesbian|| \n ||kuni|| \n ||cumsluts|| \n ||classic|| \n ||eroneko|| \n ||futanari||", inline=True)

    embed.add_field(name='**__GER!!!__**' ,
    value=" ||boobs|| \n ||bJ|| \n ||anal|| \n ||trap|| \n ||tits|| \n ||girlsologif|| \n ||yuri|| \n ||hentai||" , inline=True)

    embed.add_field(name='** **' ,
    value=" ||girlSolo|| \n ||smallboobs|| \n ||pussyWankgif|| \n ||pussyart|| \n  ||kemonomimi|| \n ||pussygif|| \n ||cumarts|| \n ||blowjob||" , inline=True)

    embed.add_field(name='**__เปิดเพลง__** | **__music control__**',
    value=" join \n play (url / name) \n pause \n skip \n stop \n loop \n queue \n nowplay \n leave \n volume (0-150) " , inline=False)

    embed.add_field(name='ข้อมูลผู้สร้างบอทและอื่นๆ | Infomation Bot Deverloper',
    value=' about \n ผู้สร้าง')

    embed.set_footer(text="ขอให้สนุกกับ ปุ๊ยยยยย! **^-^**")

    #await ctx.send("Help ถูกส่งไปแล้ว ลองเช็คดู")
    await ctx.send(embed=embed)
    #await author.send(embed=embed)
    print(f'Help Command Has Sending...')

@bot.command(pass_context=True)
async def reboot(ctx):
     try:
        await ctx.send("Rebooting....")
        await bot.logout()
     finally:
        print("Rebooting....")
        os.execv(sys.executable, ['python'] + sys.argv + ['--reboot'])

@bot.command(pass_context=True)
async def cls(ctx):
    try :
        os.system("clear")
    finally :
        await ctx.send("Clear Command Success!")

@bot.command(pass_context=True)
async def shutdown(ctx):
    try :
        await ctx.send("Shutting Down...")
        await bot.logout()
    finally :
        exit() 

@bot.command()
async def punuy(ctx):
    path = r"{}\image\random\punny".format(os.getcwd())
    files = os.listdir(path)
    rd = random.randrange(0, len(files))
    index = r"{}\image\random\punny\{}".format(os.getcwd(),files[rd])
    with open(index, 'rb') as picture :
        await ctx.send(file=discord.File(picture))

@bot.command()
async def random(ctx, types) :
    get = requests.get('https://nekos.life/api/v2/img/{}'.format(types))
    data = json.loads(get.text)
    await ctx.send(data["url"])

@bot.command()
async def rd(ctx, types) :
    get = requests.get('https://nekos.life/api/v2/img/{}'.format(types))
    data = json.loads(get.text)
    await ctx.send(data["url"])

@random.error
async def random_error(ctx, error) :
    await ctx.send("**Bruh!!** 404 Not Front")

@rd.error
async def rd_error(ctx, error) :
    await ctx.send("**Bruh!!** 404 Not Front")

@bot.command()
async def fox(ctx):
    url = "https://some-random-api.ml/img/fox"
    r = requests.get(url)
    data = json.loads(r.text)
    await ctx.send(data["link"])

@bot.command()
async def cat(ctx):
    url = "https://some-random-api.ml/img/cat"
    r = requests.get(url)
    data = json.loads(r.text)
    await ctx.send(data["link"])

@bot.command()
async def support(ctx):
    embed=discord.Embed(
        title='สามารถ Donate ได้ที่',
        color=0x78e40c
        )

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652568046900215823/654737485607338033/639815524339154945.png")

    embed.add_field(name='**__True Wallet__**',
    value="0658365756", inline=False)

    embed.add_field(name='**__BTC__**', 
    value="3P3865ETrVckon29XmfEAb3m5aJBFMupi9", inline=False)

    embed.set_footer(text='ขอบคุณที่ใช้บริการ ^-^')

    await ctx.send(embed=embed)

@bot.command(aliases=['พยากรณ์อากาศ','wt','พยากรณ์'])
async def weather(ctx, *, country) :
    try :
        apikey = '91374c97ff88bb708caae6c247dbd5d6'
        url = 'http://api.openweathermap.org/data/2.5/find?q='+ country +'&units=metric&APPID=' + apikey
        header = {'X-Requested-With':'XMLHttpRequest'}
        get =  requests.get(url,headers=header)
        x =  json.loads(get.text)
        
        description_weather = 'จังหวัด' + country
        
        temp = x['list'][0]['main']['temp']
        temp_min = x['list'][0]['main']['temp_min']
        temp_max =  x['list'][0]['main']['temp_max']

        url_status = "http://openweathermap.org/img/wn/{}@2x.png".format(x['list'][0]['weather'][0]['icon'])
        
        embed=discord.Embed(title='พยากรณ์อากาศ', description=description_weather, color=0x78e40c)
        embed.set_thumbnail(url=str(url_status))
        embed.add_field(name='อุณหภูมิ °c', value=temp, inline=True)
        embed.add_field(name='อุณหภูมิตํ่าสุด °c', value=temp_min, inline=True)
        embed.add_field(name='อุณหภูมิสูงสุด °c ', value=temp_max, inline=True)
        embed.set_footer(text='Powered By openweathermap.org & M - 307')
        
        await ctx.channel.send(embed=embed)

    except Exception as e:
        embed=discord.Embed(
            title="**Bruh** :slight_frown: ", 
            description="ไม่พบจังหวัด ลองใหม่ดูนะ ^-^", 
            color=0x78e40c
        )

        await ctx.channel.send(embed=embed)

@bot.command(aliases=['ผู้สร้าง'])
async def about(ctx):
    embed=discord.Embed(
        title='เกี่ยวกับผู้สร้าง',
        color=0x78e40c
        )

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652568046900215823/654737485607338033/639815524339154945.png")

    embed.add_field(name='ชื่อ',
    value="ปุย (ปุ๊ยยยยยย)", inline=True)

    embed.add_field(name='อายุ',
    value="14 ปี", inline=True)

    embed.add_field(name='นิสัย',
    value="งั้นๆ", inline=False)

    embed.add_field(name='สถานะ',
    value="มีเมียแล้วว ^^", inline=False)

    embed.add_field(name='สามารถติดต่อได้ที่',
    value="!!! UPDATE !!!", inline=False)

    embed.add_field(name='ผู้สร้างบอท',
    value="@Punuy_48_TGT#2938", inline=False)

    embed.set_footer(text='ปุ๊ยยยยยยยยย ^-^')

    await ctx.send(embed=embed)

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run('NjU0MzM4MzQwMjkxODcwNzMy.XfEQYQ.JXmFJqa-IQm0JCdqsPChxe1Xll8')