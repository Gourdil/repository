import requests

API_KEY = 'AIzaSyDEyLFE6dTQneIGC2HCLlbbz-wcJGkNMNw'
SEARCH_QUERY = 'algeria politics'
MAX_RESULTS = 10

url = f'https://www.googleapis.com/customsearch/v1?key={AIzaSyDEyLFE6dTQneIGC2HCLlbbz-wcJGkNMNw}&cx=017576662512468239146:omuauf_lfve&q={algeria-politics}&num={10}'
response = requests.get(url)
data = response.json()
if 'items' in data:
    for item in data['items']:
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        print(f"Snippet: {item['snippet']}\n") 