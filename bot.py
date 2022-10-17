import requests
# token = '5641284279:AAFzEZUATMNCGv7ctEF77CvGLxT6D0f6GpU'
newToken = '5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'
# url2 = 'https://api.telegram.org/bot5641284279:AAFzEZUATMNCGv7ctEF77CvGLxT6D0f6GpU/getMe'

list1 = []
while True:
    data = requests.get(url=f'https://api.telegram.org/bot{newToken}/getUpdates')
    data = data.json()
    
    getText = data['result'][-1]['message']['text']
    chat_id = data['result'][-1]['message']['chat']['id']
    # chat_id = 335988975
    data1 = {
        'chat_id': chat_id,
        'text': getText
    }

    list1.append(data['result'][-1])
    if len(list1) < 2:
        data3 = requests.get(url=f'https://api.telegram.org/bot{newToken}/SendMessage', json=data1)
    else:
        if list1[-1]['message']['message_id'] != list1[-2]['message']['message_id']:
            data3 = requests.get(url=f'https://api.telegram.org/bot{newToken}/SendMessage', json=data1)