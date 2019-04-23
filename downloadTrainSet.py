import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
import json

cred = credentials.Certificate('evently-key.json')

firebase_admin.initialize_app(cred)
store = firestore.client()

file_path = "LabeledEvent.json"
collection_name = "labeledDescriptions"

doc_ref = store.collection(collection_name)

try:
    docs = doc_ref.get()
except google.cloud.exceptions.NotFound:
    print(u'No such collection!')

data = []

for doc in docs:
    # print(u'{} => {}'.format(doc.id, doc.to_dict()))
    data.append(doc.to_dict())

with open(file_path, 'w') as fp:
    json.dump(data, fp)

print(str(len(data))+" documents downloaded")
print('Done')