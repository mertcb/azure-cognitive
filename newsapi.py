import requests
import json
from pprint import pprint


subscription_key = ""
search_term = "Üniversite"
search_url = "https://api.bing.microsoft.com/v7.0/news/search"
headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()

search_results =response.json()
pprint(search_results)