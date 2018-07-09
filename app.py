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

'''
Reddit Python library.
'''
import praw

# get the reddit api object
from init import REDDIT

# user related functions
import user

# for putting the bot to sleep
from time import sleep

'''
list of submissions to be used to prevent
sending duplicate submissions
'''
SUBMISSIONS = []

def process_message(name: str, sub: 'url', subject: str) -> None:
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
				process_message(name, sub, sub.title)

		except praw.exceptions.APIException:
			process_message(name, sub, "Post that you wanted, but title was too long!")

		except:
			print('Unexpected Error, continuing onwards')

def run(name: str, subreddits: 'subreddits', key_words: list) -> None:
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
	name, subreddits, key_words, time_to_sleep = user.get_input()

	while True:
		try:
			run(name, subreddits, key_words)

		except KeyboardInterrupt:
			return user.end()

		except:
			print('Oh no! A strange error occured. Your internet must be down..')

		else:
			print('going to sleep for {} seconds...'.format(time_to_sleep))
			sleep(time_to_sleep)
			print('running again..')

	
if __name__ == '__main__':
	main()

