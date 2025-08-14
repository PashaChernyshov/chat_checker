import json
from telethon import TelegramClient, events

# Загружаем конфиг из JSON
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Создаем клиент
client = TelegramClient(
    config['session_name'], 
    config['api_id'], 
    config['api_hash'], 
    device_model='iPhone 13 Pro Max', 
    system_version="4.16.30-vxCUSTOM"
    )

@client.on(events.NewMessage(chats=config["target_chats"]))
async def handler(event):
    message_text = event.message.message.lower()
    if config["trigger_word"] in message_text:
        await event.reply(config["reply_text"])

print("Юзербот запущен...")
client.start()
client.run_until_disconnected()