import requests as r
import json

url = 'https://api.groupme.com/v3'

class Manager:
    def __init__(self, key):
        self.key = str('?token=' + key) # To make things a little easier for the get and post commands
        self.bot_id = None
        self.group_id = None
        self.pic_key = str(key) # Makes things easier for the image command

    # PROCESS FOR USING PREEXISTING BOTS
    def start_bot(self, name):
        x = r.get(str(url + '/bots' + self.key))
        for i in x.json()['response']:
            if i['name'] == name:
                self.bot_id = i['bot_id']
                self.group_id = i['group_id']
        if self.bot_id is not None:
            print('Found bot')
        else:
            j = input('Could not find bot with this name. Would you like to make a bot with this name? Y/N')
            while j != 'y' and j != 'n':
                j = input('Need to type Y or N.')
            if j.lower() == 'y':
                j = input("What group would you like to put this in?")
                self.create_bot(name, j)
            elif j.lower() == 'n':
                raise TypeError('Need valid bot')

    # PROCESS FOR CREATING NEW BOTS. FORMAT IS (botname, groupname)
    def create_bot(self, name, groupname):
        x = r.get(str(url + '/groups' + self.key))
        for i in x.json()['response']:
            if i['name'] == groupname:
                self.group_id = i['group_id']
        if self.group_id is None:
            j = input('Cannot find group with this name. Would you like to create a group? Y/N ')
            while j != 'y' and j != 'n':
                j = input('Need to type Y or N.')
            if j.lower() == 'y':
                x = r.post(str(url + '/groups' + self.key), data = json.dumps({'name' : groupname}))
                self.bot_id = x.json()['response']['id']
            elif j.lower() == 'n':
                raise TypeError('Need group')
        x = r.post(str(url + '/bots' + self.key), data = json.dumps({'bot': {'name': name, 'group_id': self.group_id}}))
        if str(x) != '<Response [201]>':
            print('Group may already have a bot. Looking for bot...')
            check = False
            x = r.get(str(url + '/bots' + self.key))
            for i in x.json()['response']:
                if i['group_id'] == self.group_id:
                    botname = i['name']
                    self.bot_id = i['bot_id']
                    check = True
            if check == False:
                print('Unexpected error. Try again later.')
            else:
                print('Found bot. Bot name is ' + str(botname))
        else:
            self.bot_id = x.json()['response']['bot_id']
            print('Bot successfully made!')

    # POST MESSAGE IN GROUP
    def post_message(self, message):
        if self.bot_id is None:
            raise ValueError('Need to establish bot')
        r.post(str(url + '/bots/post' + self.key), data = json.dumps({'bot_id' : self.bot_id, 'text': message}))
        print('Success')

    # POSTS PICTURE (PICTURE MUST BE IN FOLDER)
    def post_picture(self, picturename, message=''):
        if self.bot_id is None:
            raise ValueError('Need to establish bot')
        pic = open(picturename, 'rb')
        type = picturename.split('.')[1]
        x = r.post('https://image.groupme.com/pictures', headers={'X-Access-Token': self.pic_key, 'Content-Type': 'image/' + str(type)}, data = pic)
        r.post(str(url + '/bots/post' + self.key), data=json.dumps({'bot_id': self.bot_id, 'text': message,
                                                                    'picture_url': x.json()['payload']['picture_url']}))

    # GET LAST MESSAGE IN GROUP (RETURNS TUPLE, E.G. (NICKNAME, MESSAGE))
    def retrieve_message(self):
        if self.bot_id is None:
            raise ValueError('Need to establish bot')
        x = r.get(str(url + '/groups/' + self.group_id + self.key))
        return (x.json()['response']['messages']['preview']['nickname'],
                x.json()['response']['messages']['preview']['text'])

    def get_members(self):
        if self.bot_id is None:
            raise ValueError('Need to establish bot')
        x = r.get(str(url + '/groups/' + str(self.group_id) + self.key))
        return [i['nickname'] for i in x.json()['response']['members']]
    
'''
How to use:

If you have not made a bot yet, start by using bot = Manager(GROUPME_KEY) and then use the create_bot command, with
the group name and the bot name you want. If you already have a bot for that group, Manager will select that bot instead.
After creating a bot, there are three core commands -- bot.post_message, bot.retrieve_message(), and bot.post_picture().
The names are pretty self explanatory. In order to use bot.post_picture(), make sure you have the image saved in the
folder with the bot code.
'''
