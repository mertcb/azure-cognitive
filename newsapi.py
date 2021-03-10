import requests
import json
from pprint import pprint


subscription_key = ""
search_term = "Student"
search_url = "https://api.bing.microsoft.com/v7.0/news/search"
headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()

search_results =response.json()
pprint(search_results['value'][0]) ## writes first news
pprint(search_results['value'][1]) ## writes second news

## simply we have sent an http request with headers and params.