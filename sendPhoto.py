import requests
TOKEN = '5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'

def getRequests(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates').json()
    getUpdatesDogPhotos = requests.get(f'https://random.dog/woof.json').json()
    getUpdatesCatPhotos = requests.get(f'https://aws.random.cat/meow').json()
    return updates, getUpdatesDogPhotos, getUpdatesCatPhotos

def getInfo(getUpdates, getDogPhotoUrl, getCatPhotoUrl, TOKEN):
    resultUpdates = getUpdates['result'][-1]
    getChatId = resultUpdates['message']['chat']['id']
    getDogUrl = getDogPhotoUrl['url']
    getCatUrl = getCatPhotoUrl['file']
    getText = resultUpdates['message']['text']
    getmessageId = resultUpdates['message']['message_id']
    return getChatId, getDogUrl, getCatUrl, getText, getmessageId, TOKEN

def sendPhotoDog(acceptChatId, acceptPhotoUrl, acceptText, TOKEN):
    data = {
        'chat_id': acceptChatId,
        'photo': acceptPhotoUrl,
        'text': acceptText 
    }
    r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', data=data)

def sendButton(chat_id, TOKEN):
    button = {'text': 'DOG'}
    button2 = {'text': 'CAT'}

    keyboard = [
        [button, button2]
    ]

    reply_markup = {'keyboard': keyboard, 'resize': True}

    data = {
        'chat_id': chat_id,
        'reply_markup': reply_markup
    }
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json=data)


newChatId = -1

while True:
    whileUpdates = getRequests(TOKEN)
    whileGetUpdates, whileGetDogPhotoUrl, whileGetCatPhotoUrl = whileUpdates
    whileGetInfo = getInfo(whileGetUpdates, whileGetDogPhotoUrl, whileGetCatPhotoUrl, TOKEN)
    whileSendChatId, whileSendPhotoDogUrl, whileSendPhotoCatUrl, whileSendText, whileGetMessageId, whileToken = whileGetInfo
    sendButton(whileSendChatId, whileToken)
    
    if (whileSendText == 'DOG' or whileSendText == 'dog') and (newChatId != whileGetMessageId):
        sendPhotoDog(whileSendChatId, whileSendPhotoDogUrl, whileSendText, whileToken)
        newChatId = whileGetMessageId
    elif (whileSendText == 'CAT' or whileSendText == 'cat') and newChatId != whileGetMessageId:
        sendPhotoDog(whileSendChatId, whileSendPhotoCatUrl, whileSendText, whileToken)
        newChatId = whileGetMessageId