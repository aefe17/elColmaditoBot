import os
import discord
import youtube_dl


def play_music(url: str):
    song_there = os.path.isfile('Music/song.mp3')
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        return "Wait for the current playing music to end or use the '$stop' command"

    voiceChannel = discord.utils.get(discord.guild.voice_channels, name='NA')
    voice = discord.utils.get(discord.voice_clients, guild=discord.guild)
    voiceChannel.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192'}]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio('song.mp3'))

# @bot.command(name='play', help='plays music')
# async def play(ctx, url: str):
#
#     voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='NA')
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     await voiceChannel.connect()

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{'key': 'FFmpegExtractAudio',
#                             'preferredcodec': 'mp3',
#                             'preferredquality': '192'}]
#     }
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#         shutil.move('elColmaditoBot','Music')
#     for file in os.listdir('Music'):
#         if file.endswith(".mp3"):
#             os.rename(file, "song.mp3")
#     voice.play(discord.FFmpegPCMAudio('song.mp3'))


# @bot.command(name='leave', help='leaves voice channel')
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_connected():
#         await voice.disconnect()
#     else:
#         await ctx.send("The bot is not connected to any voice channel")


# @bot.command(name='pause', help='pause music')
# async def pause(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send('Currently no audio is being played')


# @bot.command(name='resume', help='pause music')
# async def resume(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_pause():
#         voice.resume()
#     else:
#         await ctx.send('Currently no audio is paused')


# @bot.command(name='stop', help='stops music from playing')
# async def stop(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     voice.stop
