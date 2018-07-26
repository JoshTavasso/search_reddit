# Search-Reddit

**Reddit Search Bot - A practice bot. First attempt with API.** 

--------------------------------------------------------------------------------------------------------------
**Description**

A bot that searches through one or more subreddits, 
looking for specified keywords in the subreddit submissions. 
If the keywords are found, the post is sent to a specified user, 
using reddit's private messaging system. 

The script begins by asking the user what reddit user to send the 
submissions to, then asks for subreddits to search in, then asks 
for keywords. Lastly, the user is asked how long the bot should 
sleep for after each search. The bot then runs indefinitely 
(unless the user terminates the program manually), searching 
through the first 100 posts in the subreddit(s) and sleeping a 
specified number of seconds after each search.

--------------------------------------------------------------------------------------------------------------

**Use Case**

Say I want to be up to date on all of the discussions about my favorite TV show. I can run this bot on the subreddit about the TV show, and I will get alerted immediately when someone brings up the topic I am interested in.

--------------------------------------------------------------------------------------------------------------

**This project uses praw, python reddit api wrapper**
