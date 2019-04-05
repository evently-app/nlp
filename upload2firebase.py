import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
import json

cred = credentials.Certificate('evently-key.json')

firebase_admin.initialize_app(cred)
store = firestore.client()

file_path = "eventDataset"
collection_name = "unlabeled"


def batch_data(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

with open(file_path) as json_file:
	eventDatas = json.load(json_file)

count = 1

for batched_data in batch_data(eventDatas, 499):
    batch = store.batch()
    for data_item in batched_data:
        doc_ref = store.collection(collection_name).document("event"+str(count))
        batch.set(doc_ref, data_item)
        count+=1
    batch.commit()


print('Done')