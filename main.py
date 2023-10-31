import datetime

import discord
import json


class AdvancedClient(discord.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())

    async def on_member_join(self, member: discord.Member):
        channel = self.get_channel(988515947499356230)
        await channel.send(f"Welcome to our server, *amnd some epic stuff here maybe* {member.mention}")


client = AdvancedClient()


@client.command(name="ping", description="Bot replies with a pong message")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("Pong!")


@client.command(name="say", description="Bot repeats your message")
async def say(ctx: discord.ApplicationContext, message: discord.Option(str, required=True, name="message", description="Your message to repeat")):
    await ctx.respond(message)


@client.command(name="ban", description="Bans a guild member")
@discord.default_permissions(ban_members=True)
async def ban(ctx: discord.ApplicationContext, user: discord.Option(discord.Member, required=True, description="Member to ban")):
    await user.ban()
    await ctx.respond(f"@{user.name} got banned.")


@client.command(name="kick", description="Kicks a guild member")
@discord.default_permissions(kick_members=True)
async def kick(ctx: discord.ApplicationContext, user: discord.Option(discord.Member, required=True, description="User to kick")):
    await user.kick()
    await ctx.respond(f"@{user.name} got kicked.")


@client.command(name="purge", description="Delete messages")
@discord.default_permissions(manage_messages=True)
async def purge(ctx: discord.ApplicationContext, amount: discord.Option(int, required=True, description="Amount of messages to delete")):
    messages = await ctx.channel.purge(limit=amount)
    await ctx.respond(content=f"{len(messages)} deleted.", ephemeral=True)


@client.command(name="mute", description="Mute someone")
@discord.default_permissions(manage_messages=True)
async def mute(ctx: discord.ApplicationContext, user: discord.Option(discord.Member, required=True, description="User to mute")):
    user: discord.Member = user
    await user.timeout(until=datetime.datetime.now()+datetime.timedelta(days=24))
    await ctx.respond(f"@{user.name} got muted.")


@client.command(name="unmute", description="Unmute someone")
@discord.default_permissions(manage_messages=True)
async def unmute(ctx: discord.ApplicationContext, user: discord.Option(discord.Member, required=True, description="User to unmute")):
    await user.timeout(until=None)
    await ctx.respond(f"@{user.name} got unmuted.")

if __name__ == "__main__":
    with open("./settings.json", "r", encoding="utf-8") as f:
        client.run(json.loads(f.read())["token"])
