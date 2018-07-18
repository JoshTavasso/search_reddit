# jtavasso 6/19/2018
# Searching For Wanted Reddit Posts

'''
A practice bot. First try with API.

A bot that searches through one or more subreddits, 
looking for specified keywords in the subreddit submissions. 
If the keywords are found, the post is sent to a specified user, 
using reddit's private message system. 

The script begins by asking the user what reddit user to send the 
submissions to, then asks for subreddits to search in, then asks 
for keywords. Lastly, the user is asked how long the bot should 
sleep for after each search. The bot then runs indefinitely 
(unless the user terminates the program manually), searching 
through the first 100 posts in the subreddit, and sleeping a 
specified number of seconds after each search.

'''

# reddit python library
import praw

# get the reddit api object
from modules.reddit.config import REDDIT

# functions for sending message and getting desired subreddits
from modules.reddit.functions import get_subreddit_list, check_word_and_send

# user related functions
from modules.ui.user import end, get_input

# for putting the bot to sleep
from time import sleep

'''
list of submissions to be used to prevent
sending duplicate submissions
'''
SUBMISSIONS = []

def search(name: str, subreddits: 'subreddits', key_words: list) -> None:
	''' Iterates through the first 100 submissions in the 'new' 
		category of the given subreddits, checks if the key
		words are in the submission title and sends a message
		to the given username if so
	'''
	for sub in subreddits.new(): # iterating through first 100 subs in the 'new' category
		try:
			if sub not in SUBMISSIONS:
				check_word_and_send(name,sub,key_words)
		except:
			print('Unexpected Error, continuing onwards')

		finally:
			SUBMISSIONS.append(sub)

def main():
	''' The main function which sets up the bot and 
		runs it
	'''
	name, sub_input, key_words, time_to_sleep = get_input()
	subreddits = get_subreddit_list(sub_input)

	while True:
		try:
			search(name, subreddits, key_words)
			print('going to sleep for {} seconds...'.format(time_to_sleep))
			sleep(time_to_sleep)
			print('running again..')

		except KeyboardInterrupt:
			return end()

		except:
			print('A strange error occured. Your internet must be down..')

	
if __name__ == '__main__':
	main()

