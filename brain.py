import groupy
import time
import requests
import pyimgur

IMGUR_ACCESS = ''


def process_message(message):
    message = message.lower().split()
    if message[0] == '!latex':
        message = ''.join(message[1:])
        url ='http://latex.codecogs.com/gif.latex? ' + message
        r = requests.get(url)
        f = open('test.gif', 'wb')
        f.write(r.content)
        f.close()
        im = pyimgur.Imgur(IMGUR_ACCESS)
        uploaded_image = im.upload_image('test.gif', title="latex bot")
        return uploaded_image.link
    return None

group_name = 'Test'
bot_name = 'latexbot'

if __name__ == '__main__':
    index = 0
    groups = groupy.Group.list()
    for i in range(len(groups)):
        print(i)
        if group_name in str(groups[i]).split()[0]:
            index = i
            break
    group = groups[index]

    index = 0
    bots = groupy.Bot.list()
    for i in range(len(bots)):
        if bot_name in str(bots[i]).split():
            index = i
    bot = bots[index]

    # Loop to continuously run
    while True:
        x = process_message(group.messages().newest.text)
        if x != None:
            bot.post(x)
        time.sleep(3)
