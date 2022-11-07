import requests


def ddg_query():
    presidents_list = []
    url_ddg = "https://api.duckduckgo.com"
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    for data in rsp_data["RelatedTopics"]:
        info = data["Text"]
        president = info.split(" -")[0]
        presidents_list.append(president)
    return presidents_list
