import requests


def ddg_query():
    presidents_list = []
    url_ddg = "https://api.duckduckgo.com"
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    for data in  rsp_data["RelatedTopics"]:
        president = data["Text"]

        presidents_list.append(president)
    return presidents_list

def main():
    list = ddg_query()
    print(list)


if __name__ == '__main__':
    main()