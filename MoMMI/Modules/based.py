import random
import re
from typing import Match
from discord import Message
from MoMMI import master, always_command, MChannel

@always_command("based")
async def based(channel: MChannel, _match: Match, message: Message) -> None:
    if not channel.server_config("based.enabled", True):
        return

    match = re.search(r"^\s*(based|gebaseerd|basé)[\s*?.!)]*$", message.content, re.IGNORECASE)
    if match is None:
        return
    
    based = "Based on what?"
    unbased = "Not Based."

    if match.group(1).lower() == "gebaseerd":
        based = "Gebaseerd op wat?"
        unbased = "Niet Gebaseerd."
        
    elif match.group(1).lower() == "basé":
        based = "Sur quoi?"
        unbased = "Pas basé."
        
    if random.random() > 0.005:
        await channel.send(based)
    else:
        await channel.send(unbased)
