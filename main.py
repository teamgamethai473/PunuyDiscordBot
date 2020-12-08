import discord
import os
import sys
import random
import requests
import json
import re
import string
import asyncio
import psutil
import platform
import datetime
import uptime
import shutil
import time
import timedelta
import subprocess
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from re import findall
from discord.utils import get
from json import loads, dumps
from base64 import b64decode
from datetime import datetime
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from itertools import cycle
from bs4 import BeautifulSoup
from requests.utils import requote_uri

start_time = time.time()
prefix = 'p!'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
status = cycle(['> Evolution coming soon... <'])

@bot.event
async def on_ready():
	with open("text\\punuybot.txt") as f:
		print(f.read())
	print("PunuyBot", end ="")
	print(f' v 1.0.5 Evolution (For Linux)')
	print(bot.user.name)
	print(bot.user.id)
	print(f'--> Start Now <--')

	change_status.start()

	#bot.load_extension('cogs.music')

@tasks.loop(seconds=10)
async def change_status():
	sv ="on > {} Server <".format(str(len(bot.guilds)))

	result = next(status)

	if result == 'sv' :
		await bot.change_presence(activity=discord.Game(sv))
	else :
		await bot.change_presence(activity=discord.Game(result))

#@tasks.loop(seconds=5)
#async def server_count():
#	member = guild.member_count
#	role = 
#	bot = 
#	user = 
#	channel = 

@bot.event
async def on_message(message):
	await bot.process_commands(message)
	user = message.author
	msg = message.content
	chn = message.channel
	sv = message.guild
	channel = bot.get_channel(741676672209911910)

	if str(message.author) != 'This is Punuy#9684' :

		embed=discord.Embed(
		title="{} => {}\n{} IN {}".format(user,msg,chn,sv)[:2048],        
		color=0x78e40c
		)

		await channel.send(embed=embed)
		return

@bot.command()
async def setup_counter(ctx):
    try:
        guild = bot.get_guild(629604166641254410) # <-- insert yor guild id here
        await ctx.send("Setting up management!")
        category = await guild.create_category("Management", overwrites=None, reason=None)
        await guild.create_voice_channel(f"Member Count: {guild.member_count}", overwrites=None, category=category, reason=None)
        await ctx.send("Setup finished!")
    except Exception as errors:
        print(f"Bot Error: {errors}")

@bot.command()
async def ping(ctx):
	embed=discord.Embed(
		title=':signal_strength: Loading...',
		color=0x78e40c
	)

	msg = await ctx.send(embed=embed)
	
	embed2=discord.Embed(
		title=f':signal_strength:   **PONG!** {round(bot.latency * 1000)}ms',
		color=0x78e40c
	)

	embed2.set_author(name="Requested by " + str(ctx.message.author),
	icon_url=ctx.message.author.avatar_url)

	await msg.edit(embed=embed2)

@bot.command()
async def ปิง(ctx):
	embed=discord.Embed(
		title=':signal_strength: โหลด...',
		color=0x78e40c
	)

	msg = await ctx.send(embed=embed)

	asyncio.sleep(2)

	get = (f'  :signal_strength:   **ปอง!** {round(bot.latency * 1000)}ms')
	embed2=discord.Embed(
		title=get,
		color=0x78e40c
	)

	embed2.set_author(name="Requested by " + str(ctx.message.author),
	icon_url=ctx.message.author.avatar_url)

	await msg.edit(embed=embed2)

@bot.command()
async def clear(ctx, amount=5):
	try :
		await ctx.channel.purge(limit=amount)
	finally :
		msg = await ctx.send("Clear!")
		await asyncio.sleep(1)
		await msg.delete()

@bot.command(pass_context=True)
async def cls(ctx):
	try :
		os.system("clear")
	finally :
		msg = await ctx.send("Clear !")
		time.sleep(0.5)
		await ctx.message.delete()
		await msg.delete()

@bot.command()
async def randomsnekos(ctx, types) :
	get = requests.get('https://nekos.life/api/v2/img/{}'.format(types))
	data = json.loads(get.text)

	embed=discord.Embed(
		title="Categories : --> __{}__ <--".format(types),
		description="--> [Link Here]({}) <--".format(data["url"]),
		color=0x78e40c
		)

	embed.set_image(url=data["url"])

	await ctx.send(embed=embed)

@randomsnekos.error
async def randomsnekos_error(ctx, error) :
	embed=discord.Embed(
	title="**ไม่เจออะ T_T** :slight_frown: ", 
	description="ไม่พบสิ่งที่คุณกำลังหา ลองใหม่ดูนะ =.=\nหรือลองใช้ **p!loli (สิ่งที่คุณจะหา)** ดูนะ ^-^", 
	color=0x78e40c
	)

	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652568046900215823/654737485607338033/639815524339154945.png")

	await ctx.send(embed=embed)

@bot.command()
async def loli(ctx, categories) :
	try:
		get = requests.get('https://api.lolis.life/{}'.format(categories))
		data = json.loads(get.text)

		embed=discord.Embed(title="Categories : --> __{}__ <--".format(data["categories"][0]), 
		description="--> [Link Here]({}) <--".format(data["url"]),
		color=0x78e40c
		)

		embed.set_image(url=data["url"])

		await ctx.send(embed=embed)

	except Exception as e:
		embed=discord.Embed(
			title="**ไม่เจออะ T_T** :slight_frown: ", 
			description="ไม่พบสิ่งที่คุณกำลังหา ลองใหม่ดูนะ =.=\nหรือลองใช้ **p!ramdoms (สิ่งที่คุณจะหา)** ดูนะ ^-^", 
			color=0x78e40c
		)

		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652568046900215823/654737485607338033/639815524339154945.png")

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

		embed=discord.Embed(title='พยากรณ์อากาศ',
		description=description_weather,
		color=0x78e40c
		)

		embed.set_thumbnail(url=str(url_status))
		
		embed.add_field(name='อุณหภูมิ °c',
		value=temp, inline=True)
		
		embed.add_field(name='อุณหภูมิตํ่าสุด °c',
		value=temp_min, inline=True)
		
		embed.add_field(name='อุณหภูมิสูงสุด °c ',
		value=temp_max, inline=True)
		
		embed.set_footer(text='Powered By openweathermap.org \nCoded By : M - 307')
		
		await ctx.channel.send(embed=embed)

	except Exception as e:

		embed=discord.Embed(
			title="**Bruh** :slight_frown: ", 
			description="ไม่พบจังหวัด ลองใหม่ดูนะ ^-^", 
			color=0x78e40c
		)

		await ctx.channel.send(embed=embed)

@bot.command()
async def say(ctx, channel, message) :
	if int(ctx.author.id) == 355426872718524416:
		data = re.sub('[^0-9]+', '', channel)
		channel_server = bot.get_channel(int(data))
		await channel_server.send(message)
	else :
		await ctx.send("**No No No !!!**")

@bot.command()
async def sayembed(ctx, channel, message) :
	if int(ctx.author.id) == 355426872718524416 :
		data = re.sub('[^0-9]+', '', channel)
		channel_server = bot.get_channel(int(data))
		await channel_server.send(

			embed=discord.Embed(
			title=message,
			color=0x78e40c
			)
		)
	else :
		await ctx.send("**No No No !!!**")

@bot.command(pass_context=True)
async def avatar(ctx, members=None) :
	if not members :
		embed=discord.Embed(
			title=str(ctx.author), 
			description="--> [Avatar URL Link]({}) <--".format(ctx.author.avatar_url), 
			color=0x78e40c
		)

		embed.set_image(url=ctx.author.avatar_url)

		await ctx.send(embed=embed)
	else :
		for xmembers in ctx.message.guild.members:
			user = re.findall(str(members).lower(),str(xmembers).lower())

			if user :
				embed=discord.Embed(
					title="{}".format(str(xmembers)), 
					description="--> [Avatar URL Link]({}) <--".format(xmembers.avatar_url), 
					color=0x78e40c
				)

				embed.set_image(url=xmembers.avatar_url)
				await ctx.send(embed=embed)
				break
			else :
				sub_string =  re.compile('@!')

				query = str(members).strip('<>')

				if sub_string.match(query):
					find = re.sub('[^0-9]+', '', (str(members).lower()))
					members = await bot.fetch_user(int(find))
					embed=discord.Embed(
						title="{}".format(str(members)), 
						description="--> [Avatar URL Link]({}) <--".format(members.avatar_url), 
						color=0x78e40c
					)

					embed.set_image(url=members.avatar_url)
					await ctx.send(embed=embed)
					break
				else :
					pass

@bot.command()
async def roll(ctx):
	embed=discord.Embed(
		title=':game_die: Rolling...',
		color=0x78e40c
	)

	msg = await ctx.send(embed=embed)

	rdroll = ['1','2','3','4','5','6','7','8','9','10']
	res = random.choice(rdroll)

	asyncio.sleep(2)

	get = ':game_die: Gocha!\n       You have roll is : {}'.format(res)
	embed2=discord.Embed(
		title=get,
		color=0x78e40c
	)

	await msg.edit(embed=embed2)

@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member=None):
	if not user:
		embed = discord.Embed(title="Your Info.",color=0x78e40c)

		embed.add_field(name="Username",value=ctx.message.author.name + "#" + ctx.message.author.discriminator, inline=True)
		embed.add_field(name="ID",value=ctx.message.author.id, inline=True)
		embed.add_field(name="Status",value=ctx.message.author.status, inline=True)
		embed.add_field(name="Highest role",value=ctx.message.author.top_role)
		embed.add_field(name="Roles",value=len(ctx.message.author.roles))
		embed.add_field(name="Joined",value=ctx.message.author.joined_at.strftime("%d %B %Y \n%H:%M:%S %p"))
		embed.add_field(name="Created",value=ctx.message.author.created_at.strftime("%d %B %Y \n%H:%M:%S %p"))
		embed.add_field(name="Bot?",value=ctx.message.author.bot)

		embed.set_thumbnail(url=ctx.message.author.avatar_url)

		embed.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)

		embed.set_footer(text="Code By : Punuy#9999",icon_url='https://cdn.discordapp.com/attachments/652568046900215823/654737485607338033/639815524339154945.png')

		await ctx.send(embed=embed)

	else:

		embed = discord.Embed(title="{}'s info".format(user),color=0x78e40c)

		embed.add_field(name="Username",value=user, inline=True)
		embed.add_field(name="ID",value=user.id, inline=True)
		embed.add_field(name="Status",value=user.status, inline=True)
		embed.add_field(name="Highest role",value=user.top_role)
		embed.add_field(name="Roles",value=len(user.roles))
		embed.add_field(name="Joined",value=user.joined_at)
		embed.add_field(name="Created",value=user.created_at)
		embed.add_field(name="Bot?",value=user.bot)

		embed.set_thumbnail(url=user.avatar_url)

		embed.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)

		embed.set_footer(text="Code By : Punuy#9999",icon_url='https://avatars3.githubusercontent.com/u/16878148?s=400&v=4')
		
		await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx, guild: discord.Guild = None):
	guild = ctx.guild
	embed = discord.Embed(title=f'{guild}',timestamp=ctx.message.created_at, color=0x78e40c)
	embed.set_thumbnail(url=guild.icon_url)
	embed.add_field(name="Channels:", value=len(guild.channels))
	embed.add_field(name="Roles:", value=len(guild.roles))
	embed.add_field(name="Booster Server:", value=guild.premium_subscription_count)
	embed.add_field(name="Member:", value=guild.member_count)
	embed.add_field(name="Creater at:", value=guild.created_at)
	embed.add_field(name="OwOner:", value=guild.owner)
	embed.set_footer(text=f"Request By {ctx.author}", icon_url=ctx.author.avatar_url)

	await ctx.send(embed=embed)

#--------------------------------------------------------------------------------------------------------------------#

@bot.command()
async def help(ctx):	
	embed=discord.Embed(title="PunuyBot =.=", color=0x78e40c)
	
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652568046900215823/654737485607338033/639815524339154945.png")

	embed.add_field(name='**UPDATE!!! ^~^**' ,
	value="Evolution coming soon..." , inline=False)

	embed.set_footer(text=f"Request By : {ctx.author}", icon_url=ctx.author.avatar_url)

	await ctx.send(embed=embed)
        
#--------------------------------------------------------------------------------------------------------------------#

with open("json\\token.json", encoding='utf8') as f:
	data = json.load(f)
bot.run(data["TOKEN"])	