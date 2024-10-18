from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        help = "replies with a friendly \'hello\'!"
    )
    async def hello(self, message):
        print(f"hello received from {message.author}")
        await message.channel.send(f"Hello {message.author.mention}")
        return

async def setup(bot):
    await bot.add_cog(Hello(bot))

async def teardown(bot):
    await bot.remove_cog(Hello(bot))