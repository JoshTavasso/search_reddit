# Search-Reddit
A practice bot. First try at API.

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
