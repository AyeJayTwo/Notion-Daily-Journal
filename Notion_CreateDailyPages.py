import requests
import json
import datetime
from secretvariables import *


url = 'https://api.notion.com/v1/pages'
urldb = 'https://api.notion.com/v1/databases/'
urlsearch = 'https://api.notion.com/v1/search'

headers = {
    'Authorization': SECRET_TOKEN,
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16'
}
# Pull the current date which I use for a lot of page titles
current_time = datetime.datetime.now()
formattedDate = str(current_time.month)+'/' + \
    str(current_time.day)+'/'+str(current_time.year)[2:]

## Check if daily page already exists
search = {'query': formattedDate+' Daily Entry'}
r = requests.post(urlsearch, headers=headers, data=json.dumps(search))
results = json.loads(r.text)['results']

if len(results) > 0:
    print('Daily page already exists')
    new_dailyJournal = results[0]['id']
else:
    print('Creating Daily Page...')
    payload = {
        'parent': {'database_id': dailyJournal},
        'properties': {
            'Name': {
                'title': [{
                    'text': {'content': formattedDate+" Daily Entry"}
                }]
            }
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))

    new_dailyJournal = json.loads(r.text)['id']

## Check if food log page already exists
search = {'query': formattedDate+' Food Log'}
r = requests.post(urlsearch, headers=headers, data=json.dumps(search))
results = json.loads(r.text)['results']

if len(results) > 0:
    print('Daily food log already exists')
    new_FoodLog = results[0]['id']

else:
    print('Creating Food Log Page...')
    payload = {
        'parent': {'database_id': foodLog},
        'properties': {
            'title': {
                'title': [{
                    'text': {'content': formattedDate+" Food Log"}
                }]
            }
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))

    new_FoodLog = json.loads(r.text)['id']

## Check if exercise page already exists
search = {'query': formattedDate+' Workout'}
r = requests.post(urlsearch, headers=headers, data=json.dumps(search))
results = json.loads(r.text)['results']

if len(results) > 0:
    print('Exercise page already exists')
    new_Exercise = results[0]['id']

else:
    print('Creating Exercise Page...')
    payload = {
        'parent': {'database_id': workouts},
        'properties': {
            'title': {
                'title': [{
                    'text': {'content': formattedDate+" Workout"}
                }]
            }
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))

    new_Exercise = json.loads(r.text)['id']


## Check if metaview page already exists
search = {'query': formattedDate}
r = requests.post(urlsearch, headers=headers, data=json.dumps(search))
results = json.loads(r.text)['results']

if len(results) > 3:  # TODO: This isn't a great solution for checking, kinda a stop gap in the instance where I make other 'dated' pages
    print('Meta page already exists')
    metaPage = results[0]['id']

else:
    print('Creating Meta Page...')
    payload = {
        'parent': {'database_id': metaDB},
        'properties': {
            'title': {'title': [{'text': {'content': formattedDate}}]},
            'Date 1': {'date': {'start': current_time.isoformat()}},
            # Links back to created or identified pages
            'Exercise': {'relation': [{'id': new_Exercise}]}, 
            'Food Log': {'relation': [{'id': new_FoodLog}]},
            'Daily Journal': {'relation': [{'id': new_dailyJournal}]}
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))

print("Go forth and journal!")