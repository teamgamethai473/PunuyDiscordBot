@bot.command(aliases=['h'])
async def help(ctx):
    author = ctx.author

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

    await ctx.send("Help ถูกส่งไปแล้ว ลองเช็คดู")
    await author.send(embed=embed)
    print(f'Help Command Has Sending...')
