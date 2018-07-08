'''
user.py
User related functions
'''

import praw
from init import REDDIT
from time import sleep

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

def getInput() -> tuple:
	'''Retrieves the user input and
		returns it
	'''
	name = input('Input a username to send the submissions to: ')
	subreddits = getSubReddit()
	key_words = getKeyWords()
	time_to_sleep = int(input('Please specify how long the bot should sleep after each search, in seconds (ex: 10 for 10 seconds): '))

	return name,subreddits,key_words,time_to_sleep

