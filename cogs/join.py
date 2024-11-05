import logging

import disnake
from disnake.ext import commands
from disnake.ext.commands import BucketType
from disnake.utils import get

from Shinen.core.log import log_colored


class JoinAndExit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="join",
        description="Join a voice channel",
    )
    @commands.has_permissions(administrator=True)
    @commands.max_concurrency(1, BucketType.user)
    async def join(self, interaction):
        try:
            channel = interaction.user.voice.channel
            voice = get(self.bot.voice_clients, guild=interaction.guild)

            if voice and voice.is_connected():
                await voice.move_to(channel)
                log_colored(logging.INFO, msg=f"Moving to voice channel {channel}")
            else:
                await channel.connect()
                log_colored(logging.INFO, msg="Joining voice channel")

            await interaction.response.send_message("Trying joining voice channel", ephemeral=True)

        except Exception as e:
            log_colored(logging.ERROR, msg=f"Failed to join voice channel, code = {e}")

    @commands.slash_command(
        name="exit",
        description="Exit a voice channel",
    )
    @commands.has_permissions(administrator=True)
    @commands.max_concurrency(1, BucketType.user)
    async def leave(self, interaction):
        try:
            voice_client = interaction.guild.voice_client

            if voice_client and voice_client.is_connected():
                await voice_client.disconnect()
                log_colored(logging.INFO, msg="Leaving voice channel")
                await interaction.response.send_message("Leaving voice channel", ephemeral=True)
            else:
                await interaction.response.send_message("Not connected to any voice channel", ephemeral=True)

        except Exception as e:
            log_colored(logging.ERROR, msg=f"Failed to leave voice channel, code = {e}")


def setup(bot):
    bot.add_cog(JoinAndExit(bot))
