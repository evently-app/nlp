# NLP
## Collect Event Datas
1. Find mapping from eventbrite category id to name
    1. [Eventbrite Categories](https://www.eventbrite.com/platform/docs/by-category) Here is the official list of Event Categories used by Eventbrite.
    2. Run **extract_categories.py** to create the mapping from event id to name.
2. Scrape from Eventbrite API
    1. Run **response_formatter.py** and collect event data in batch. Only store each event's description, title and category name (from our eventid2name mapping obtained in last step).
3. Upload Formatted Event Data to Firestore
    1. Obtain firebase service key json file (**Do not put in Github, or any public place**)
    2. Run **upload2firebase.py** to upload event data to "labeled" collection in firestore.
