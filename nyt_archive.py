#The Archive API returns an array of NYT articles for a given month, going back to 1851. 
# Its response fields are the same as the Article Search API. 
# The Archive API is very useful if you want to build your own database of NYT article metadata. 
# You simply pass the API the year and month and it returns a JSON object with all articles for that month.
#  The response size can be large (~20mb).

import urllib.request
import json
import re

api_key = <YOUR API KEY HERE>
#Archive API
endpoint = "https://api.nytimes.com/svc/archive/v1"
year=2020
month=1
#api_call = endpoint+f"/{year}/{month}.json?api-key={api_key}"
#urllib.request.urlretrieve(api_call, 'archive_nyt_2020_6.txt')

#json_object = json.dumps(json.loads(urllib.request.urlopen(api_call).read()), indent=1)

#with open('archive_2020_01.json', 'w') as f:
    #f.write(json_object)

with open('archive_2020_01.json', 'r') as f:
     archive_data = json.load(f)

with open('parsed_2020_01.txt', 'w') as f:
    for article in archive_data["response"]["docs"]:
        summary= f"headline: {article['headline']['main']}\n\
print_headline: {article['headline']['print_headline']}\n\
abstract: {article['abstract']}\n\
keywords: {':::'.join([keyword['value'] for keyword in article['keywords']])}\n\n"
        #print(summary)
        f.write(summary)

