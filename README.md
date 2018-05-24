# Latex Bot
A bot for groupme to post latex.

# Instructions to Download

In the Python console, run 

```
pip install -r requirements
```


# Configuring Latex Bot

First, go to https://dev.groupme.com/ and in the top right hit the Access Token button. In brain.py in the argument for botme.Manager(''), add your groupme key.
Next, change the variables in the bot.create_bot() function from test and latexbot to whatever you want. Then, simply run

```
nohup python3 brain.py &
```

and answer all of the questions prompted in the command line. This will allow him to monitor your groups for as long as the script is running.

# How to Use Latex Bot

The basic structure for calling Latex bot is

```
!latex [Insert Expression Here]
```

So, for example,

```
!latex \sin(x)+1
```

will output \sin(x)+1 into your chat.
