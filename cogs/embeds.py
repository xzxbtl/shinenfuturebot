import logging
import disnake
from disnake.ext import commands
from disnake.ext.commands import BucketType
from Shinen.core.log import log_colored


class TestCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="test",
        description="Testing command",
    )
    @commands.max_concurrency(1, BucketType.user)
    async def test_command(self, interaction):
        try:
            embed = disnake.Embed(
                title="Testing Command",
                description="Testing command",
                color=disnake.Color.green(),
                timestamp=disnake.utils.utcnow(),
            )
            embed.set_image(url="https://i.pinimg.com/564x/e0/96/cf/e096cf5b9acd2b45a5c5d13a79b9bbbf.jpg")
            await interaction.response.send_message(embed=embed)
            log_colored(logging.INFO, msg="Successful Command")

        except Exception as e:
            log_colored(logging.ERROR, msg=f"Error in embeds.py code = {e}")


def setup(bot):
    bot.add_cog(TestCommand(bot))
