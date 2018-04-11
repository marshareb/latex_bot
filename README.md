# Latex Bot
A bot for groupme to post latex.

# Instructions to Download

In the Python console, run 

```
pip install -r requirements
```

Next, go to https://dev.groupme.com/ and in the top right hit the Access Token button. In brain.py in the argument for botme.Manager(''), add your groupme key. Latex Bot is now ready to run.

# Configuring Latex Bot

Simply run

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
