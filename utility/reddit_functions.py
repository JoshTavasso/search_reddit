'''
reddit_functions.py

reddit related functions
'''

# reddit python library
import praw

# reddit api object
from utility.config import REDDIT

def _process_message(name: str, sub: 'url', subject: str) -> None:
	''' Given a redditor username, url to a submission, sends
		a message to the username using the given subject parameter
		as the subject of the message and the url as the message
		body
	''' 
	REDDIT.redditor(name).message(subject, sub.url)
	print('Message sent to:', name, 'regarding:', sub.title)

def check_word_and_send(name: str, sub: 'submission', key_words: list) -> None:
	''' iterates through the key words given and checks
		if the word is in the submission title. If it is, we send 
		the message to the given username.
	'''
	for word in key_words:
		try:
			if word in sub.title:
				_process_message(name, sub, sub.title)

		except praw.exceptions.APIException:
			_process_message(name, sub, "Post that you wanted, but title was too long!")

		except:
			print('Unexpected Error, continuing onwards')