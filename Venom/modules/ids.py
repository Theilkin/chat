from pyrogram import filters
from pyrogram.enums import ParseMode

from Venom import VenomX


@VenomX.on_cmd("id")
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[Mesajın ID - si:]({message.link})** `{message_id}`\n"
    text += f"**[Sizin ID:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[İstifadəçi ID - si:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("Bu istifadəçi mövcud deyil.", quote=True)

    text += f"**[Qrup ID - si:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[Yanıtlanmış mesaj ID - si:]({reply.link})** `{reply.id}`\n"
        text += f"**[Yanıtlanmış İstifadçi ID - si:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"Yönləndirilmiş kanal, {reply.forward_from_chat.title}, ID - si `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"Yanıtlanmış (Chat/Kanal) ID - si `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )
