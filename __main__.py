import logging
import disnake
from disnake import Activity
from Shinen.core.shinenbot import ShinenBot
from utils import intents
from core.config_reader import config
from core.log import log_colored


def main():
    try:
        TOKEN_BOT, OWNER_ID = config.bot_token.get_secret_value(), config.owner_id.get_secret_value()
        if TOKEN_BOT is not None:

            bot = ShinenBot(
                intents=intents.get(),
                test_guilds=[781965689002393610],
                owner_id=OWNER_ID,
                activity=Activity(
                    type=disnake.ActivityType.watching,
                    name="!help",
                )
            )

            log_colored(logging.INFO, f"Bot Starting...")
            bot.load_extensions('cogs')
            bot.run(TOKEN_BOT)
        else:
            log_colored(logging.CRITICAL, "TOKEN BOT is invalid")

    except Exception as e:
        log_colored(logging.ERROR, msg=f"Error in main.py code = {e}")


if __name__ == "__main__":
    main()
