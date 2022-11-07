import requests

url_ddg = "https://api.duckduckgo.com"
resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
rsp_data = resp.json()
print(rsp_data["Heading"])
'''
url_list = []
for photo in json_data:
    url_list.append(photo['url'])
print(len(url_list))
print(len(set(url_list)))
'''