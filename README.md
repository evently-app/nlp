# NLP
## Collect Event Datas from all over US
1. Find mapping from eventbrite category id to name
    1. [Eventbrite Categories](https://www.eventbrite.com/platform/docs/by-category) Here is the official list of Event Categories used by Eventbrite.
    2. Run **extract_categories.py** to create the mapping from event id to name.
2. Scrape from Eventbrite API
    1. Run **response_formatter.py** and collect event data in batch. Only store each event's description, title and category name (from our eventid2name mapping obtained in last step).
3. Upload Formatted Event Data to Firestore
    1. Obtain firebase service key json file (**Do not put in Github, or any public place**)
    2. Run **upload2firebase.py** to upload event data to "unlabeled" collection in firestore.
## Tagging is done using the [tagging service](https://github.com/evently-app/tagging-app)
## Trained classification model and predict category tags for our events
4. Download the labeled events data from firestore
	1. Run **downloadTrainSet.py** to download labeled events from "labeledDescriptions" collection in firestore.
5. Train the text classification model
	1. Run **model.ipynb**
6. Do the inference on unlabeled data
	1. Run **Inference.ipynb**
