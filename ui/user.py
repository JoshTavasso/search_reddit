'''
user.py

User related functions
'''

def _get_subreddit_input() -> str:
	''' Asks the user to enter what subreddits
		they would like this bot to search in
		and returns the input
	'''
	return input('Enter subreddits to search in, seperated by spaces (ex: UCI Apple): ')

def _get_key_words() -> list:
	''' Asks the user to enter some keywords to
		look for and returns a list of those keywords
	'''
	data_input = input('Enter some keywords to look for, seperated by spaces (ex: pokemon smash): ')
	return data_input.split()

def get_input() -> tuple:
	'''Retrieves the user input and
		returns it
	'''
	name = input('Input a username to send the submissions to: ')
	subreddit_input = _get_subreddit_input()
	key_words = _get_key_words()
	time_to_sleep = int(input('Please specify how long the bot should sleep after each search, in seconds (ex: 10 for 10 seconds): '))

	return name,subreddit_input,key_words,time_to_sleep

def end() -> None:
	''' Prints the message for terminating
		the bot
	'''
	print('\nTERMINATING BOT')
	print('bye!')

