import logging
from disnake import Member, AuditLogAction, Role
from disnake.ext import commands
from Shinen.core.log import log_colored


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        log_colored(logging.INFO, msg=f"Member : {message.author.name} send : {message.content}")
        ...

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_colored(logging.INFO, msg=f"Member : {member.name} Join in : {member.guild}")
        ...

    @commands.Cog.listener()
    async def on_member_update(self, member: Member, before: Member, after: Member):
        log_colored(logging.INFO, msg=f"Member {member} : {before.top_role} Update : {after.top_role}")

        if before.top_role != after.top_role:
            log_colored(logging.INFO, msg=f"Member {member} changed top role: {before.top_role} -> {after.top_role}")

    @commands.Cog.listener()
    async def on_guild_role_update(self, before: Role, after: Role):
        async for entry in before.guild.audit_logs(limit=1, action=AuditLogAction.role_update):
            if entry.target == before and entry.user != self.bot.user:
                log_colored(logging.INFO, msg=f"Role {after} was updated by {entry.user}")


def setup(bot):
    bot.add_cog(Messages(bot))
