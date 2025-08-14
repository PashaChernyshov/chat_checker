# Chat Checker — Telegram Keyword Trigger Userbot

> 🇷🇺 Русская версия ниже • English version below

---

## 🇬🇧 English

### Overview
**Chat Checker** is a lightweight Telegram **userbot** built with Python and Telethon. It listens for a specific **keyword** in selected chats and automatically posts a **predefined reply** right in the same chat.

Use it for quick alerts, reminders, and workflow automations triggered by a word or phrase.

### Features
- Monitors messages in selected chats (private, groups, channels you can read).
- Case-insensitive keyword matching.
- Instant auto-reply with your predefined text.
- Simple JSON-based configuration.

### How It Works
1. You configure the bot in `config.json`.
2. The script connects to Telegram via the [Telethon](https://github.com/LonamiWebs/Telethon) MTProto client.
3. When the keyword appears in one of the target chats, the bot replies to that message with your text (`event.reply(...)`).

> 💡 Want to DM a specific user instead of replying in the chat? See the snippet in **Advanced** below.

### Project Structure
```
Chat_checker/
├─ bot.py           # main script
├─ config.json      # configuration (do NOT commit secrets)
└─ smena_checker.session  # Telethon session (should be ignored by git)
```

### Requirements
- Python 3.9+ (recommended 3.10/3.11)
- A Telegram account + API credentials from https://my.telegram.org/apps
- A virtual environment (recommended)

### Installation
```bash
# 1) Clone your repo and enter it
git clone <your-repo-url>.git
cd <your-repo-folder>

# 2) Create and activate virtualenv (Windows PowerShell example)
python -m venv venv
venv\Scripts\activate

# macOS/Linux:
# python3 -m venv venv
# source venv/bin/activate

# 3) Install dependencies
pip install telethon
```

### Configuration
Create `config.json` in the project folder:

```jsonc
{
  "api_id": 1234567,
  "api_hash": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "session_name": "smena_checker",
  "trigger_word": "смена",
  "reply_text": "Привет! Это автоответ.",
  "target_chats": ["@your_chat", "Some Chat Name"]
}
```

- `api_id`, `api_hash`: your Telegram API credentials (keep them secret).
- `session_name`: name for your Telethon session file.
- `trigger_word`: a word/phrase to trigger the reply (matching is case-insensitive).
- `reply_text`: the message to send as a reply.
- `target_chats`: list of chats to monitor; can be `@username`, chat titles, or IDs.

### Run
```bash
python bot.py
```
The first launch will ask you to log in (code to your Telegram). After that, the session is stored and reused.

### Advanced
**Send a DM to a specific user instead of replying in the chat:** replace the reply block in `bot.py` with:
```python
await client.send_message(config["to_user_id"], config["reply_text"])
```
and add `to_user_id` (or username) to `config.json`:
```json
"to_user_id": 123456789
```

### Security Notes
- **Never commit** `config.json`, session files (`*.session`), or your virtualenv to Git.
- Add a `.gitignore` similar to:
```
venv/
*.session*
config.json
__pycache__/
*.pyc
```
- Treat your `api_id`/`api_hash` like passwords.

### Troubleshooting
- **Keyword not triggering?** Check spelling, case-insensitive matching, and that the target chat is listed correctly.
- **No access to a chat?** The user account running the userbot must be a member and able to read messages.
- **Auth issues?** Delete the `*.session` file and re-login; ensure correct phone and code.

### License
MIT (or your choice).

---

## 🇷🇺 Русская версия

### Описание
**Chat Checker** — лёгкий **юзербот** для Telegram на Python и Telethon. Он слушает выбранные чаты, ловит **ключевое слово** и автоматически отправляет **заранее заданный ответ** прямо в том же чате.

Подходит для напоминаний, оповещений и автоматизаций, запускаемых по слову/фразе.

### Возможности
- Мониторинг сообщений в выбранных чатах (лички, группы, каналы с доступом на чтение).
- Поиск ключа без учёта регистра.
- Мгновенный автоответ заданным текстом.
- Простой JSON-конфиг.

### Как это работает
1. Настраиваете `config.json`.
2. Скрипт подключается к Telegram через [Telethon](https://github.com/LonamiWebs/Telethon).
3. При появлении ключевого слова в одном из отслеживаемых чатов бот отвечает на сообщение (`event.reply(...)`).

> 💡 Хотите отправлять ЛС конкретному пользователю вместо ответа в чат? Смотрите сниппет в разделе **Advanced** выше.

### Структура проекта
```
Chat_checker/
├─ bot.py                 # основной скрипт
├─ config.json            # конфигурация (не коммитьте секреты)
└─ smena_checker.session  # сессия Telethon (добавьте в .gitignore)
```

### Требования
- Python 3.9+ (рекомендуется 3.10/3.11)
- Аккаунт Telegram + API-ключи с https://my.telegram.org/apps
- Виртуальное окружение (рекомендуется)

### Установка
```bash
# 1) Клонируйте репозиторий и зайдите в папку
git clone <your-repo-url>.git
cd <your-repo-folder>

# 2) Создайте и активируйте виртуальное окружение
python -m venv venv
venv\Scripts\activate
# macOS/Linux:
# python3 -m venv venv && source venv/bin/activate

# 3) Установите зависимости
pip install telethon
```

### Конфигурация
Создайте `config.json` в корне проекта:

```jsonc
{
  "api_id": 1234567,
  "api_hash": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "session_name": "smena_checker",
  "trigger_word": "смена",
  "reply_text": "Привет! Это автоответ.",
  "target_chats": ["@your_chat", "Название чата"]
}
```

- `api_id`, `api_hash` — ваши API-данные Telegram (храните в секрете).
- `session_name` — имя файла сессии Telethon.
- `trigger_word` — слово/фраза-триггер (поиск без регистра).
- `reply_text` — текст автоответа.
- `target_chats` — список чатов для отслеживания; можно использовать `@username`, названия или ID.

### Запуск
```bash
python bot.py
```
При первом запуске потребуется вход (код в Telegram). Сессия сохранится и будет использоваться повторно.

### Advanced
**Отправка сообщения в ЛС конкретному пользователю вместо ответа в чат:** замените блок ответа в `bot.py` на:
```python
await client.send_message(config["to_user_id"], config["reply_text"])
```
и добавьте в `config.json` поле:
```json
"to_user_id": 123456789
```

### Безопасность
- **Не коммитьте** `config.json`, файлы сессий (`*.session`) и виртуальное окружение.
- Добавьте `.gitignore`:
```
venv/
*.session*
config.json
__pycache__/
*.pyc
```
- Берегите `api_id`/`api_hash` как пароли.

### Частые проблемы
- **Триггер не срабатывает?** Проверьте слово, регистр, и что чат корректно указан в `target_chats`.
- **Нет доступа к чату?** Аккаунт, под которым запущен юзербот, должен быть участником и иметь доступ к сообщениям.
- **Проблемы с входом?** Удалите `*.session` и войдите заново; проверьте правильность номера и кода.

### Лицензия
MIT (или выберите свою).
