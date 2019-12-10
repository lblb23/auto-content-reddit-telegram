import argparse
import time

import praw
import telegram
import yaml
from tinydb import TinyDB, Query

parser = argparse.ArgumentParser()
parser.add_argument('--config', default='config.yaml', dest='config_path',
                    help='path to config file')

args = parser.parse_args()

with open(args.config_path, 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

reddit = praw.Reddit(client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     user_agent=config['user_agent'],
                     username=config['username'],
                     password=config['password'])

subreddit = reddit.subreddit(config['subreddit'])

db = TinyDB('are_published.json')

bot = telegram.Bot(config['telegram_bot_token'])

for post in getattr(subreddit, config['type_content'])(limit=20):

    check_published = Query()
    result = db.search(check_published.id_post == post.id)

    if len(result) > 0:
        continue

    print(post.title, post.id, post.url)

    # Parse gifs
    """
    import urllib.request
    import requests
    import json

    if 'gfycat.com' in post.url:
        r = requests.get(url='https://api.gfycat.com/v1/gfycats/' + post.url.split('/')[-1])
        video_url = json.loads(r.text)['gfyItem']['mp4Url']
        filename = video_url.split('/')[-1]
        urllib.request.urlretrieve(video_url, filename)
        try:
            bot.send_video(chat_id="@test_adult", video=open(filename, 'rb'), supports_streaming=True,
                           caption=post.title)
        except:
            print('Timeout', post.id)
            db.insert({'id_post': post.id, 'result': 'timeout'})
            continue
    else:
    """

    if post.is_video is not True:
        bot.send_photo(chat_id=config['channel_name'], photo=post.url,
                       caption=post.title)

    db.insert({'id_post': post.id})

    time.sleep(10)
