# contains reddit object

# reddit python library
from praw import Reddit

# for storing bot data
import json

# get bot data (api keys and such)
with open('modules/reddit/config.json', 'r') as keys:
	info = json.load(keys)

# the reddit object, allowing us to access reddit
REDDIT = Reddit(
				client_id = info["CLIENT"], 
				client_secret = info["SECRET"], 
				username = info["BOT_NAME"], 
				password = info["BOT_PASSWORD"], 
				user_agent = info["AGENT"])