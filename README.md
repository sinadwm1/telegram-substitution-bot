# Telegram Text Substitution Bot

[راهنمای فارسی](README_FA.md)

A small Telegram bot that maps Latin letters to a fixed set of alternate characters and returns the transformed text. This is a text substitution demo, **not encryption**.

## Run

1. Revoke the token present in the original local script and create a new token in BotFather.
2. Set `BOT_TOKEN` in the process environment. `.env.example` shows the variable name but is not loaded automatically.
3. Install and run:

```bash
pip install -r requirements.txt
python bot.py
```

The bot uses long polling. It has not been tested against the live Telegram API during preparation. Released under the MIT License.
