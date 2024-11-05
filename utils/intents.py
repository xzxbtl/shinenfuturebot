from disnake import Intents


def get():
    intents = Intents.default()
    intents.message_content = True
    intents.guilds = True
    intents.voice_states = True
    return intents
