import json

with open('eventbrite_categories', 'r') as fp:
	categories = json.load(fp)['categories']

id2name = dict()

for category in categories:
	if "id" in category and "name" in category:
		id2name[category["id"]] = category["name"]

with open('id2name', 'w') as fp:
    json.dump(id2name, fp)

