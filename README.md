# Chat Checker — Telegram Keyword Trigger Userbot

> 🇷🇺 Русская версия ниже • English version below

---

## 🇬🇧 English

### Overview
**Chat Checker** is a lightweight Telegram **userbot** built with Python and Telethon. It monitors selected chats for a specific **keyword** and automatically posts a **predefined reply** in the same chat.

Use it for quick alerts, reminders, and automation triggered by a word or phrase.

---

### Features
- Monitors messages in private chats, groups, or channels.
- Case-insensitive keyword search.
- Instant auto-reply with your custom message.
- Easy setup via a JSON config file.

---

### How It Works
1. You create `config.json` with your Telegram API credentials and settings.
2. The bot connects to Telegram via the [Telethon](https://github.com/LonamiWebs/Telethon) MTProto client.
3. When the keyword appears in a target chat, the bot replies automatically.

---

### Requirements
- Python **3.9+** (recommended 3.10/3.11)
- A Telegram account
- API ID & API Hash from [my.telegram.org](https://my.telegram.org/apps)
- [Telethon](https://github.com/LonamiWebs/Telethon) library

---

### Installation
```bash
# 1) Clone your repo and go into it
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate
# macOS/Linux:
# python3 -m venv venv && source venv/bin/activate

# 3) Install dependencies
pip install telethon
```

---

### Configuration
Create a file `config.json` in the project folder and insert your own credentials:

```jsonc
{
  "api_id": 1234567,
  "api_hash": "xxxxxxxxxxxxxxxxxxxxxxxx",
  "session_name": "smena_checker",
  "trigger_word": "смена",
  "reply_text": "Hello! This is an auto-reply.",
  "target_chats": ["@your_chat", "Chat Name"]
}
```

---

### Where to get `api_id` and `api_hash`
1. Go to [https://my.telegram.org](https://my.telegram.org).
2. Log in with your phone number.
3. Go to **API development tools**.
4. Create a new application.
5. Copy `api_id` and `api_hash` into `config.json`.

---

### Run the bot
```bash
python bot.py
```
- On the first run, the bot will ask for your Telegram phone number and a login code.
- After login, it will create a `.session` file to reuse your authorization.

---

### Advanced
Send a direct message instead of replying in chat:
```python
await client.send_message(config["to_user_id"], config["reply_text"])
```
Add to `config.json`:
```json
"to_user_id": 123456789
```

---

### Security Notes
- **Do not commit** your real `config.json` or `.session` file to public repositories.
- Treat your `api_id` and `api_hash` like passwords.
- Use `.gitignore`:
```
venv/
*.session*
__pycache__/
*.pyc
```

---

## 🇷🇺 Русская версия

### Описание
**Chat Checker** — это лёгкий **юзербот** для Telegram на Python и Telethon. Он отслеживает выбранные чаты, ищет **ключевое слово** и автоматически отправляет **заранее заданный ответ** в тот же чат.

Подходит для напоминаний, сигналов и автоматизации по триггеру.

---

### Возможности
- Работает в личных чатах, группах и каналах.
- Ищет слово без учёта регистра.
- Отвечает мгновенно заранее заданным текстом.
- Простая настройка через `config.json`.

---

### Как это работает
1. Создаёте `config.json` с вашими API-данными Telegram и настройками.
2. Скрипт подключается к Telegram через [Telethon](https://github.com/LonamiWebs/Telethon).
3. При появлении ключевого слова бот отвечает автоматически.

---

### Требования
- Python **3.9+** (рекомендуется 3.10/3.11)
- Аккаунт Telegram
- API ID и API Hash с [my.telegram.org](https://my.telegram.org/apps)
- Установленная библиотека **Telethon**

---

### Установка
```bash
# 1) Клонируйте репозиторий и перейдите в него
git clone https://github.com/<ваш-логин>/<ваш-репо>.git
cd <ваш-репо>

# 2) Создайте и активируйте виртуальное окружение
python -m venv venv
venv\Scripts\activate
# macOS/Linux:
# python3 -m venv venv && source venv/bin/activate

# 3) Установите зависимости
pip install telethon
```

---

### Настройка
Создайте в папке проекта файл `config.json` и вставьте в него свои данные:

```jsonc
{
  "api_id": 1234567,
  "api_hash": "xxxxxxxxxxxxxxxxxxxxxxxx",
  "session_name": "smena_checker",
  "trigger_word": "смена",
  "reply_text": "Привет! Это автоответ.",
  "target_chats": ["@your_chat", "Название чата"]
}
```

---

### Где взять `api_id` и `api_hash`
1. Перейдите на [https://my.telegram.org](https://my.telegram.org).
2. Авторизуйтесь по номеру телефона.
3. Зайдите в **API development tools**.
4. Создайте новое приложение.
5. Скопируйте `api_id` и `api_hash` в `config.json`.

---

### Запуск бота
```bash
python bot.py
```
- При первом запуске бот запросит ваш номер телефона и код из Telegram.
- После входа создаст файл `.session` для повторного использования авторизации.

---

### Advanced
Чтобы отправлять сообщение в личку, а не в чат:
```python
await client.send_message(config["to_user_id"], config["reply_text"])
```
Добавьте в `config.json`:
```json
"to_user_id": 123456789
```

---

### Безопасность
- **Не заливайте** настоящий `config.json` и `.session` в публичный репозиторий.
- Берегите `api_id` и `api_hash` как пароли.
- Добавьте `.gitignore`:
```
venv/
*.session*
__pycache__/
*.pyc
```
