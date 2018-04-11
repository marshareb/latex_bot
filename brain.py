import botme
import time
import requests
import pyimgur

def process_message(message):
    message = message.lower().split()
    try:
        print(message[0])
    except:
        return None
    if message[0] == '!latex':
        message = ''.join(message[1:])
        url ='http://latex.codecogs.com/png.latex? ' + message
        r = requests.get(url)
        f = open('test.png', 'wb')
        f.write(r.content)
        f.close()
        return 'test.png'
    return None

if __name__ == '__main__':    
    bot = botme.Manager('')
    bot.start_bot('latexbot')
    # Loop to continuously run
    while True:
        x = process_message(bot.retrieve_message()[1])
        if x != None:
            bot.post_picture('test.png')
        time.sleep(3)
