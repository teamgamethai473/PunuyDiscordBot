import math
import re
import discord
import lavalink
from discord.ext import commands
from discord.ext.commands import has_permissions

url_rx = re.compile('https?:\\/\\/(?:www\\.)?.+') 

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        if not hasattr(bot, 'lavalink'): 
            bot.lavalink = lavalink.Client(bot.user.id)
            bot.lavalink.add_node('127.0.0.1', 2333, '05022548', 'eu', 'default-node') 
            bot.add_listener(bot.lavalink.voice_update_handler, 'on_socket_response')

        lavalink.add_event_hook(self.track_hook)

    def cog_unload(self):
        self.bot.lavalink._event_hooks.clear()

    async def cog_before_invoke(self, ctx):
        guild_check = ctx.guild is not None

        if guild_check:
            await self.ensure_voice(ctx)

        return guild_check

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(error.original)

    async def ensure_voice(self, ctx):
        player = self.bot.lavalink.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))
        should_connect = ctx.command.name in ('play',)

        if not ctx.author.voice or not ctx.author.voice.channel:
            embed=discord.Embed(title='Join a voicechannel first =.=',
                color=0x78e40c)
            raise commands.CommandInvokeError(embed)

        if not player.is_connected:
            if not should_connect:
                raise commands.CommandInvokeError('Not connected.')

            permissions = ctx.author.voice.channel.permissions_for(ctx.me)

            if not permissions.connect or not permissions.speak:  # Check user limit too?
                raise commands.CommandInvokeError('I need the `CONNECT` and `SPEAK` permissions.')

            player.store('channel', ctx.channel.id)
            await self.connect_to(ctx.guild.id, str(ctx.author.voice.channel.id))
        else:
            if int(player.channel_id) != ctx.author.voice.channel.id:
                raise commands.CommandInvokeError('You need to be in my voicechannel.')

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)

    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, query: str):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        query = query.strip('<>')

        if not url_rx.match(query):
            query = f'ytsearch:{query}'

        results = await player.node.get_tracks(query)

        if not results or not results['tracks']:
            embed=discord.Embed(
                title='404 Not Found :neutral_face:',
                color=0x78e40c
                )
            return await ctx.send(embed=embed)

        embed = discord.Embed(color=0x78e40c)

        if results['loadType'] == 'PLAYLIST_LOADED':
            tracks = results['tracks']

            for track in tracks:
                player.add(requester=ctx.author.id, track=track)

            embed.title = 'เพิ่มเพลลิสแล้ว'
            embed.description = f'{results["playlistInfo"]["name"]} - {len(tracks)} tracks'
        else:
            track = results['tracks'][0]
            embed.title = 'เพิ่มเพลงแล้ว'
            embed.description = f'[{track["info"]["title"]}]({track["info"]["uri"]})'
            embed.set_author(name="Requested by " + str(ctx.message.author),
            icon_url=ctx.message.author.avatar_url)
            player.add(requester=ctx.author.id, track=track)

        await ctx.send(embed=embed)

        if not player.is_playing:
            await player.play()

    @commands.command()
    async def seek(self, ctx, *, seconds: int):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        track_time = player.position + (seconds * 1000)
        await player.seek(track_time)

        await ctx.send(f'Moved track to **{lavalink.utils.format_time(track_time)}**')

    @commands.command(aliases=['forceskip'])
    async def skip(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            return await ctx.send('Not playing.')

        await player.skip()
        await ctx.send('⏭ | Skipped.')

    @commands.command()
    async def stop(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            return await ctx.send('เพลงยังไม่ได้ถูกเล่น')

        player.queue.clear()
        await player.stop()
        await ctx.send('⏹ | หยุดเล่นเพลงชั่วคราว')

    @commands.command(aliases=['np', 'n', 'playing'])
    async def now(self, ctx):
        """ Shows some stats about the currently playing song. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.current:
            return await ctx.send('เพลงยังไม่ได้ถูกเล่น')

        position = lavalink.utils.format_time(player.position)
        if player.current.stream:
            duration = '🔴 ไลฟ์'
        else:
            duration = lavalink.utils.format_time(player.current.duration)
        song = f'**[{player.current.title}]({player.current.uri})**\n({position}/{duration})'

        embed = discord.Embed(color=0x78e40c,
                              title='กำลังเล่นเพลง', description=song)
        await ctx.send(embed=embed)

    @commands.command(aliases=['q'])
    async def queue(self, ctx, page: int = 1):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.queue:
            return await ctx.send('ไม่มีคิวเพลง')

        items_per_page = 10
        pages = math.ceil(len(player.queue) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue_list = ''
        for index, track in enumerate(player.queue[start:end], start=start):
            queue_list += f'`{index + 1}.` [**{track.title}**]({track.uri})\n'

        embed = discord.Embed(colour=0x78e40c,
                              description=f'**{len(player.queue)} คิว**\n\n{queue_list}')
        embed.set_footer(text=f'หน้าที่ {page} / {pages}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['resume'])
    async def pause(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            return await ctx.send('เพลงยังไม่ได้ถูกเล่น')

        if player.paused:
            await player.set_pause(False)
            await ctx.send('⏯ | กลับมาเล่นเพลงต่อ')
        else:
            await player.set_pause(True)
            await ctx.send('⏯ | หยุดแล่นเพลง')

    @commands.command(aliases=['vol'])
    async def volume(self, ctx, volume: int = None):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not volume:
            return await ctx.send(f'🔈 | {player.volume}%')

        await player.set_volume(volume) 
        await ctx.send(f'🔈 | ปรับเสียงในระดับที่ {player.volume}%')

    @commands.command()
    async def shuffle(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        if not player.is_playing:
            return await ctx.send('เพลงยังไม่ได้ถูกเล่น')

        player.shuffle = not player.shuffle
        await ctx.send('🔀 | Shuffle ' + ('enabled' if player.shuffle else 'disabled'))

    @commands.command(aliases=['loop'])
    async def repeat(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            return await ctx.send('เพลงยังไม่ได้ถูกเล่น')

        player.repeat = not player.repeat
        await ctx.send('🔁 | ลูป ' + ('เปิดใช้งาน' if player.repeat else 'ปิดใช้งาน'))

    @commands.command()
    async def remove(self, ctx, index: int):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.queue:
            return await ctx.send('ไม่มีเพลงอยู่ในคิว =.=')

        if index > len(player.queue) or index < 1:
            return await ctx.send(f'Index has to be **between** 1 and {len(player.queue)}')

        removed = player.queue.pop(index - 1)
        embed=discord.Embed(
            title=f'ลบเพลง **{removed.title}** เรียบร้อย =.=',
            color=0x78e40c
            )

        await ctx.send(embed=embed)

    @commands.command()
    async def find(self, ctx, *, query):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not query.startswith('ytsearch:') and not query.startswith('scsearch:'):
            query = 'ytsearch:' + query

        results = await player.node.get_tracks(query)

        if not results or not results['tracks']:
            embed=discord.Embed(
                title='ไม่เจอ =.=\nNot found',
                color=0x78e40c
                )
            return await ctx.send(embed=embed)

        tracks = results['tracks'][:10]

        o = ''
        for index, track in enumerate(tracks, start=1):
            track_title = track['info']['title']
            track_uri = track['info']['uri']
            o += f'`{index}.` [{track_title}]({track_uri})\n'

        embed = discord.Embed(color=0x78e40c, description=o)
        await ctx.send(embed=embed)

    @commands.command(aliases=['dc'])
    async def disconnect(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_connected:
            embed=discord.Embed(
                title='ยังไม่ได้อยู่ในห้องเสียงนะ =.=\nStill not in the sound room =.=',
                color=0x78e40c
                )
            return await ctx.send(embed=embed)

        if not ctx.author.voice or (player.is_connected and ctx.author.voice.channel.id != int(player.channel_id)):
            embed=discord.Embed(
                title='อยู่คนละห้อง =.=\nIn different rooms',
                color=0x78e40c
                )
            return await ctx.send(embed=embed)

        embed=discord.Embed(
        title=':musical_note: | Disconnects ^-^',
        color=0x78e40c
        )

        emoji = '\N{THUMBS UP SIGN}'

        msg = await ctx.send(embed=embed)

        player.queue.clear()
        await player.stop()
        await self.connect_to(ctx.guild.id, None)
        await msg.add_reaction(emoji)

def setup(bot):
    bot.add_cog(Music(bot))