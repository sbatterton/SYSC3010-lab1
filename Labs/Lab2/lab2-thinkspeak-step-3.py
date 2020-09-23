import requests
import json

def getThingSpeak():
    url = 'https://api.thingspeak.com/channels/1152501/feeds.json?api_key='
    key = '9SSGV5BF1QOBQX3G'
    header = '&results=10'

    finalURL = url + key + header

    get_data = requests.get(finalURL).json()

    field1 = get_data['feeds']

    for x in field1:
        print(x['field1'])

if __name__ == '__main__':
    getThingSpeak()
