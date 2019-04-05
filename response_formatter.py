import json
import requests
import random

descriptions = dict()

with open('id2name', 'r') as fp:
	id2name = json.load(fp)


for i in range(1, 50):
    url = 'https://www.eventbriteapi.com/v3/events/search/?location.address=USA&expand=organizer,venue&token=5XU2X3GXCDU2MLZ7RZVH&page=' + str(i)
    response = requests.get(url).json()
    for event in response['events']:
        if 'description' in event and 'text' in event['description'] and 'name' in event and 'text' in event['name']:
            descriptions[event['name']['text']] = {'title': event['name']['text'], 'description': event['description']['text']}
        if 'category_id' in event and event['category_id']:
        	descriptions[event['name']['text']]['eventbrite_category'] = id2name[event['category_id']]
    print(i)


descriptions_keys = [key for key in descriptions.keys()]
random.shuffle(descriptions_keys)
descriptions = [descriptions[key] for key in descriptions_keys]

with open('eventDataset', 'w') as fp:
    json.dump(descriptions, fp)














