# For @UniBorg
# (c) Shrimadhav U K

from telethon import events, functions, types
from jarvis.utils import jarvis_cmd

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest

@jarvis.on(jarvis_cmd("listmyusernames"))

async def mine(event):
    """ For .reserved command, get a list of your reserved usernames. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)
