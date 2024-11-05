import logging
from logging import handlers
from colorama import Fore, Style

logger = logging.getLogger('ShinenBOT')
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = handlers.RotatingFileHandler(
    filename='discord_shinen_bot.log',
    maxBytes=10 * 1024 * 1024,  # 10 МБ
    backupCount=5,
    encoding='utf-8'
)
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


# Функция для вывода цветных сообщений в консоль
def log_colored(level, msg, *args, **kwargs):
    color = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
    }.get(level, Fore.WHITE)
    logger.log(level, f"{color}{msg}{Style.RESET_ALL}", *args, **kwargs)


"""
# Пример использования логгера
@disnake.ext.commands.command()
async def test(ctx: disnake.ApplicationContext):
    log_colored(logging.INFO, "Тестовое сообщение!")
    log_colored(logging.WARNING, "Предупреждение: что-то не так!")
    log_colored(logging.ERROR, "Критическая ошибка!")
"""
