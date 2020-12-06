import asyncio
import pickle

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswitch('!ปุย'):
        await client.send_message(message.channel, 'ปุ๊ยยยยย')
    elif message.content.startswitch('!flip'):
        filp = random.choice(['Heads','Tails'])
        await client.send_message(message.channel, flip)
    elif message.content.startswitch('p!addquote'):
        if not os.path.lsfile("quote_file.pkl"):
            quote_list = []
        else:
            with open("quote_file.pkl", "rd") as quote_file:
                quote.list = pickle.load(quote_file)
        quote_list.append(message.content[9:])
        with open("quote_file.pkl", "wb") as quote_file:
            pickle.dump(quote_list, quote_file)
    elif message.content.startswitch("quote"):
        with open("quote_file.pkl", "rb") as quote_file:
            quote_list = pickle.load(quote_file)
        await client.send_message(message.channel, random.choice(quote_list))




@bot.event
async def on_message(message):
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')





@bot.event
async def on_message(message):
    if bot.user.id != message.author.id:
        if 'foo' in message.content:
            await bot.send_message(message.channel, 'bar')

    await bot.process_commands(message)





@bot.event
async def on_message(message):
    id = bot.get_guild(ID)
    channels = ["commands"]
    valid_users = ["Ti#9298"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi") 
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")