import requests
import json
import datetime
from secretvariables import *


url_pages = 'https://api.notion.com/v1/pages'
url_db = 'https://api.notion.com/v1/databases/'
url_search = 'https://api.notion.com/v1/search'

headers = {
    'Authorization': SECRET_TOKEN,
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16'
}
# Pull the current date which I use for a lot of page titles
current_time = datetime.datetime.now()
formatted_date = current_time.strftime("%m/%d/%y")

## Check if daily page already exists
search = {'query': formatted_date+' Daily Entry'}
r = requests.post(url_search, headers=headers, data=json.dumps(search))
results = json.loads(r.text)['results']

if len(results) > 0:
    print('Daily page already exists')
    new_daily_journal = results[0]['id']
else:
    print('Creating Daily Page...')
    payload = {
        'parent': {'database_id': daily_journal},
        'properties': {
            'Name': {
                'title': [{
                    'text': {'content': formatted_date+" Daily Entry"}
                }]
            }
        }
    }
    r = requests.post(url_pages, headers=headers, data=json.dumps(payload))

    new_daily_journal = json.loads(r.text)['id']

## Check if food log page already exists
search = {'query': formatted_date+' Food Log'}
r = requests.post(url_search, headers=headers, data=json.dumps(search))
results = json.loads(r.text)['results']

if len(results) > 0:
    print('Daily food log already exists')
    new_food_log = results[0]['id']

else:
    print('Creating Food Log Page...')
    payload = {
        'parent': {'database_id': food_log},
        'properties': {
            'title': {
                'title': [{
                    'text': {'content': formatted_date+" Food Log"}
                }]
            }
        }
    }
    r = requests.post(url_pages, headers=headers, data=json.dumps(payload))

    new_food_log = json.loads(r.text)['id']

## Check if exercise page already exists
search = {'query': formatted_date+' Workout'}
r = requests.post(url_search, headers=headers, data=json.dumps(search))
results = json.loads(r.text)['results']

if len(results) > 0:
    print('Exercise page already exists')
    new_exercise_log = results[0]['id']

else:
    print('Creating Exercise Page...')
    payload = {
        'parent': {'database_id': workout_log},
        'properties': {
            'title': {
                'title': [{
                    'text': {'content': formatted_date+" Workout"}
                }]
            }
        }
    }
    r = requests.post(url_pages, headers=headers, data=json.dumps(payload))

    new_exercise_log = json.loads(r.text)['id']


## Check if metaview page already exists
search = {'query': formatted_date}
r = requests.post(url_search, headers=headers, data=json.dumps(search))
results = json.loads(r.text)['results']

if len(results) > 3:  # TODO: This isn't a great solution for checking, kinda a stop gap in the instance where I make other 'dated' pages
    print('Meta page already exists')
    metaPage = results[0]['id']

else:
    print('Creating Meta Page...')
    payload = {
        'parent': {'database_id': meta_view},
        'properties': {
            'title': {'title': [{'text': {'content': formatted_date}}]},
            'Date 1': {'date': {'start': current_time.isoformat()}},
            # Links back to created or identified pages
            'Exercise': {'relation': [{'id': new_exercise_log}]}, 
            'Food Log': {'relation': [{'id': new_food_log}]},
            'Daily Journal': {'relation': [{'id': new_daily_journal}]}
        }
    }
    r = requests.post(url_pages, headers=headers, data=json.dumps(payload))

print("Go forth and journal!")