import groupy
import time

def process_message(message):
    message = message.lower().split()
    if message[0] == '!latex':
        message = ''.join(message[1:])
        return 'http://latex.codecogs.com/png.latex?\dpi{{300}}' + message
    return None

group_name = 'gr'
bot_name = ''

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
    try:
        for i in range(len(bots)):
            if bot_name in bots[i]:
                index = i
        bot = bots[index]
    except:
        bot = groupy.Bot.create(bot_name, group)
        bot.post("I'm alive!")

    # Loop to continuously run
    while True:
        try:
            x = process_message(group.messages().newest.text)
            if x != None:
                bot.post(x)
        except:
            pass

        time.sleep(3)
