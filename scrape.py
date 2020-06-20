import json
import requests
import pandas as pd

URL = "https://api.cilabs.com/conferences/cc20/lists/speakers?per_page=100"

response = requests.get(URL)

data = response.json()

with open('data/raw_response.txt', 'w') as outfile:
    json.dump(data, outfile)

speakers = []

for speaker in data['data']:
    speakers.append([
    speaker['id'],
    speaker['first_name'],
    speaker['last_name'],
    speaker['job_title'],
    speaker['bio'],
    speaker['company_name']])

speakers_df = pd.DataFrame.from_records(speakers, columns=['speaker_id', 'first_name', 'last_name', 'job_title', 'bio', 'company_name'])

speakers_df.to_csv('data/speakers.csv')