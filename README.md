# Autocontent from Reddit to Telegram
Example of autoposting content (only pictures) from subreddit "Instagramreality"

[Implementation](https://t.me/reddit_instagramreality)

## Getting Started

1. Create a Reddit App. Manual: https://www.storybench.org/how-to-scrape-reddit-with-python/
2. Create own Telegram bot. Manual: https://core.telegram.org/bots
3. Create own Telegram channel. 
4. Add telegram bot to admins of your channel.
5. Edit config.yml with your info.
5. Run main.py
```
python3 main.py
```

## Hosting this bot on pythonanywhere.com

1. Sign up on [pythonanywhere.com](https://www.pythonanywhere.com/).
2. Upload files to server or clone repo.
3. Add daily scheduled task:
```
python3 /home/{YOUR_USERNAME}/main.py
```

## Database of content

This bot saves the post_id for checking duplicates posts in are_published.json.

## Main requirements

* [PRAW](https://praw.readthedocs.io/en/latest/)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
