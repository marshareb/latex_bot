# Latex Bot
A bot for groupme to post latex.

# Instructions to Download

In the Python console, run 

```
pip install -r requirements
```


Next, you'll need to add a .groupy.key file to your home directory, and in it copy and paste your access token. In order to do that,
you'll go to https://dev.groupme.com and click on the access token tab in the top right.

Finally, you'll need to make an Imgur account and go to https://api.imgur.com/oauth2/addclient and register your client. Find the client_id, and save that in the variable IMGUR_ACCESS.

# Configuring Latex Bot

In the brain.py file, modify the variables group_name and bot_name to what group you want and what you want the bot's name to be. Then, in a console on the computer you which to host Latex bot, run the command

```
nohup python3 brain.py &
```

This will allow him to monitor your groups for as long as the script is running.

# How to Use Latex Bot

The basic structure for calling Latex bot is

```
!latex [Insert Expression Here]
```

So, for example,

```
!latex sin(x)+1
```

will output sin(x)+1 into your chat.