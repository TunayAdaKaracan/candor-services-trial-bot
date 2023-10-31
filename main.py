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
async def say(ctx: discord.ApplicationContext, message: discord.Option(str, required=True, name="Message", description="Your message to repeat")):
    await ctx.respond(message)



if __name__ == "__main__":
    with open("./settings.json", "r", encoding="utf-8") as f:
        client.run(json.loads(f.read()))
