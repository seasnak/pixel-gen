#discord bot implementation of pixelgen
import discord


class Pixel(commands.command):


    @commands.command
    async def pixel(self, message):

        if message.author.id == self.bot.user.id: #check to make sure it's not a bot
            return
