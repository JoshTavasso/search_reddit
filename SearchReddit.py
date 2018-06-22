# jtavasso 6/19/2018
# Searching For Wanted Reddit posts

'''
A bot that searches through one or more 
subreddits, looking for specified keywords
in the subreddit submissions. If the keywords are 
found, the post is sent to a specified user, using
reddit's private message system.

The script begins by asking the user what reddit user
to send the submissions to, then asks for subreddits to
search in, then asks for keywords. Lastly, the user is
asked how long the bot should sleep for after each search.

The bot then runs indefinitely (unless the user 
terminates the program manually), searching through 
all of the posts on the subreddit every 10 seconds.

'''

import praw
from time import sleep

# The setup:

CLIENT = 'NkTmzbz9_Akg5w'
SECRET = 'vAeI7tarAe2MQdhUYZZI4NCkWls'
BOT_NAME = 'JoshSearchBot'
BOT_PASSWORD = 'JoshSearchBot'
AGENT = 'created by JOSH'
REDDIT = praw.Reddit(client_id = CLIENT, client_secret = SECRET, username = BOT_NAME, password = BOT_PASSWORD, user_agent = AGENT)

'''
list of submissions to be used to prevent
sending duplicate submissions
'''
SUBMISSIONS = []

def processMessage(name: str, sub: 'url', subject: str) -> None:
	''' Given a redditor username, url to a submission, sends
		a message to the username using the given subject parameter
		as the subject of the message and the url as the message
		body
	''' 
	REDDIT.redditor(name).message(subject, sub.url)
	print('Message sent to:', name, 'regarding:', sub.title)

def checkWordAndSendMessage(name: str, sub: 'submission', key_words: list) -> None:
	''' iterates through the key words given and checks
		if the word is in the submission title. If it is, we send 
		the message to the given username.
	'''
	for word in key_words:
		try:
			if word in sub.title:
				processMessage(name, sub, sub.title)

		except praw.exceptions.APIException:
			processMessage(name, sub, "Post that you wanted, but title was too long!")

		except:
			print('Unexpected Error, continuing onwards')

def runBot(name: str, subreddits: 'subreddits', key_words: list) -> None:
	''' Iterates through the first 100 submissions in the 'new' 
		category of the given subreddits, checks if the key
		words are in the submission title and sends a message
		to the given username if so
	'''
	for sub in subreddits.new(): # iterating through first 100 subs in the 'new' category
		try:
			if sub not in SUBMISSIONS:
				checkWordAndSendMessage(name,sub,key_words)
		except:
			print('Unexpected Error, continuing onwards')

		finally:
			SUBMISSIONS.append(sub)

def getSubReddit() -> 'subreddit':
	''' Asks the user to enter what subreddits
		they would like this bot to search in.
		Returns a subreddit object
	'''
	subreddit = input('Enter subreddits to search in, seperated by spaces (ex: UCI Apple): ')
	subs = subreddit.split()
	return REDDIT.subreddit('+'.join(subs))

def getKeyWords() -> list:
	''' Asks the user to enter some keywords to
		look for and returns a list of those keywords
	'''
	data_input = input('Enter some keywords to look for, seperated by spaces (ex: pokemon smash): ')
	return data_input.split()

def end() -> None:
	''' Prints the message for terminating
		the bot
	'''
	print('\nTERMINATING BOT')
	print('bye!')

def rest(t: 'time in seconds') -> None:
	''' Puts the bot to sleep for a certain
		amount of seconds
	'''
	print('going to sleep for {} seconds...'.format(t))
	sleep(t)
	print('running again..')

def main():
	''' The main function which sets up the bot and 
		runs it
	'''
	name = input('Input a username to send the submissions to: ')
	subreddits = getSubReddit()
	key_words = getKeyWords()
	time_to_sleep = int(input('Please specify how long the bot should sleep after each search, in seconds (ex: 10 for 10 seconds): '))

	while True:
		try:
			runBot(name, subreddits, key_words)
			rest(time_to_sleep)

		except KeyboardInterrupt:
			return end()

		except:
			print('Oh no! A strange error occured. Your internet must be down..')

	
if __name__ == '__main__':
	main()
