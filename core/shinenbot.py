from datetime import datetime
from functools import cached_property
from typing import Any
from disnake.ext import commands
from loguru import logger


class ShinenBot(commands.InteractionBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._start_time = datetime.now()
        self._members = self.get_all_members()
        self._voice_clients = []

    async def on_ready(self):
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')

    @property
    def start_time(self):
        return self.start_time

    @property
    @cached_property
    def members(self):
        return len(set(self.get_all_members()))

    @cached_property
    def guilds_count(self) -> int:
        return len(self.guilds)

    @property
    def voice_clients(self) -> list[Any]:
        return self._voice_clients
