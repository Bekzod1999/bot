



from hashlib import new
import requests
TOKEN = '5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'

new_update_len = -1

def get_updates(TOKEN):
    r = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = r.json()
    return updates

def send_message(chat_id, text, TOKEN):
    data = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data = data)

def get_info(updates, TOKEN):
    last_updates = updates['result'][-1]
    chat_id = last_updates['message']['chat']['id']
    text = last_updates['message']['text']
    message_id = last_updates['message']['message_id']
    return chat_id, text, message_id, TOKEN

new_message_id = -1

i = 0
while True:
    updates = get_updates(TOKEN)
    for_send_message = get_info(updates, TOKEN)
    chat_id, text, message_id, TOKEN = for_send_message

    if new_message_id != message_id:        
        send_message(chat_id, text, TOKEN)

        new_message_id = message_id
    print('initial_id=', message_id, 'next_id=', new_message_id )


































# from hashlib import new
# import requests
# TOKEN = '5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'

# new_update_len = -1

# def get_updates(TOKEN):
#     r = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
#     updates = r.json()
#     return updates

# def send_message(chat_id, text, TOKEN):
#     data = {
#         'chat_id': chat_id,
#         'text': text
#     }
#     r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data = data)

# def get_info(updates, TOKEN):
#     last_updates = updates['result'][-1]
#     chat_id = last_updates['message']['chat']['id']
#     text = last_updates['message']['text']

#     return chat_id, text, TOKEN

# while True:
#     updates = get_updates(TOKEN)
#     last_update_len = len(updates['result'])

#     if new_update_len != last_update_len:
#         for_send_message = get_info(updates, TOKEN)
#         chat_id, text, TOKEN = for_send_message
#         send_message(chat_id, text, TOKEN)

#         new_update_len = last_update_len

#     print('NEW UPDATE LEN', new_update_len, 'LAST UPDATE LEN', last_update_len)













