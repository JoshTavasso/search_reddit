'''
init.py
Setting up the Reddit API
'''
import praw

CLIENT = 'NkTmzbz9_Akg5w'
SECRET = 'vAeI7tarAe2MQdhUYZZI4NCkWls'
BOT_NAME = 'JoshSearchBot'
BOT_PASSWORD = 'JoshSearchBot'
AGENT = 'created by JOSH'
REDDIT = praw.Reddit(
					client_id = CLIENT, 
					client_secret = SECRET, 
					username = BOT_NAME, 
					password = BOT_PASSWORD, 
					user_agent = AGENT)