# import requests
# TOKEN = '5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'

# def getRequests(TOKEN):
#     updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates').json()
#     getUpdatesDogPhotos = requests.get(f'https://random.dog/woof.json').json()
#     getUpdatesCatPhotos = requests.get(f'https://aws.random.cat/meow').json()
#     return updates, getUpdatesDogPhotos, getUpdatesCatPhotos

# def getInfo(getUpdates, getDogPhotoUrl, getCatPhotoUrl, TOKEN):
#     resultUp = getUpdates['result'][-1]
#     getChatId = resultUp['message']['chat']['id']
#     getDogUrl = getDogPhotoUrl['url']
#     getCatUrl = getCatPhotoUrl['file']
#     getText = resultUp['message']['text']
#     getmessageId = resultUp['message']['message_id']
#     return getChatId, getDogUrl, getCatUrl, getText, getmessageId, TOKEN

# def sendPhotoDog(acceptChatId, acceptPhotoUrl, acceptText, TOKEN):
#     data = {
#         'chat_id': acceptChatId,
#         'photo': acceptPhotoUrl,
#         'text': acceptText 
#     }
#     r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', data=data)

# def sendButton(chat_id, TOKEN):
#     button = {'text': 'DOG'}
#     button2 = {'text': 'CAT'}

#     keyboard = [
#         [button, button2]
#     ]

#     reply_markup = {'keyboard': keyboard, 'resize': True}

#     data = {
#         'chat_id': chat_id,
#         'reply_markup': reply_markup
#     }
#     requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json=data)


# newChatId = -1

# while True:
#     whileUpdates = getRequests(TOKEN)
#     whileGetUpdates, whileGetDogPhotoUrl, whileGetCatPhotoUrl = whileUpdates
#     whileGetInfo = getInfo(whileGetUpdates, whileGetDogPhotoUrl, whileGetCatPhotoUrl, TOKEN)
#     getChatId, wGetDogUrlPhoto, whileSendPhotoCatUrl, getText, getMessageId, wToken = whileGetInfo
#     sendButton(getChatId, wToken)
    
#     if (getText == 'DOG' or getText == 'dog') and (newChatId != getMessageId):
#         sendPhotoDog(getChatId, wGetDogUrlPhoto, getText, wToken)
#         newChatId = getMessageId
#     elif (getText == 'CAT' or getText == 'cat') and newChatId != getMessageId:
#         sendPhotoDog(getChatId, whileSendPhotoCatUrl, getText, wToken)
#         newChatId = getMessageId












































import requests
TOKEN = '5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'

def getRequests(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates').json()
    getDogUrlPhoto = requests.get(f'https://random.dog/woof.json').json()
    getCatUrlPhoto = requests.get(f'https://aws.random.cat/meow').json()
    return updates, getDogUrlPhoto, getCatUrlPhoto

def getInfo(updates, getDogUrlPhoto, getCatUrlPhoto, TOKEN):
    resultUp = updates['result'][-1]
    getChatId = resultUp['message']['chat']['id']

    getDogUrl = getDogUrlPhoto['url']
    getCatUrl = getCatUrlPhoto['file']

    getText = resultUp['message']['text']
    getMessageId = resultUp['message']['message_id']
    return getChatId, getDogUrl, getCatUrl, getText, getMessageId, TOKEN

def sendPhotoDogAndCat(getChatId, acceptPhotoUrl, getText, TOKEN):
    data = {
        'chat_id': getChatId,
        'photo': acceptPhotoUrl,
        'text': getText 
    }
    r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', data=data)

def sendButton(getChatId, textData, TOKEN):
    button = {'text': '🐶DOG'}
    button2 = {'text': '😹CAT'}

    keyboard = [
        [button, button2]
    ]
    reply_markup = {'keyboard': keyboard, 'resize_keyboard':    True}
    data = {
        'chat_id': getChatId,
        'text': textData,
        'reply_markup': reply_markup
    }
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json=data)

newChatId = -1

while True:
    updates = getRequests(TOKEN)
    wUp, getDogUrlPhoto, getCatUrlPhoto = updates
    whileGetInfo = getInfo(wUp, getDogUrlPhoto, getCatUrlPhoto, TOKEN)
    getChatId, wGetDogUrlPhoto, wGetCatUrlPhoto, getText, getMessageId, wToken = whileGetInfo
    
    
    if (getText == '🐶DOG' or getText == 'dog') and (newChatId != getMessageId):
        sendPhotoDogAndCat(getChatId, wGetDogUrlPhoto, getText, wToken)
        sendButton(getChatId, 'That is dog', wToken)
        newChatId = getMessageId
    elif (getText == '😹CAT' or getText == 'cat') and newChatId != getMessageId:
        sendPhotoDogAndCat(getChatId, wGetCatUrlPhoto, getText, wToken)
        sendButton(getChatId, 'That is cat', wToken)
        newChatId = getMessageId