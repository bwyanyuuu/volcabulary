import requests

def getWords(word):
    url = 'https://api.mojidict.com/parse/functions/union-api'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }

    payload = {
        "functions":[
            {
                "name":"search-all",
                "params":{
                    "text": word,
                    "types":[
                        102,
                        106,
                        103
                    ]
                }
            },
            {
                "name":"mojitest-examV2-searchQuestion-v2",
                "params":{
                    "text": word,
                    "limit":1,
                    "page":1
                }
            }
        ],
        "_SessionToken":"r:e9dc731c360a15567189fe8c414e564b",
        "_ClientVersion":"js3.4.1",
        "_ApplicationId":"E62VyFVLMiW7kvbtVq3p",
        "g_os":"PCWeb",
        "g_ver":"v4.5.4.20230403",
        "_InstallationId":"2d77cdbc-c40f-4ffd-a9fe-249af413a5a7"
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        # json_data = response.json()
        # print(json_data)
        return response.json()
    else:
        print("Error:", response.text)
        return None

def getTheWord(id):
    url = 'https://api.mojidict.com/parse/functions/nlt-fetchManyLatestWords'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }

    payload = {
        "itemsJson":[
            {
                "objectId": id
            }
        ],
        "skipAccessories":False,
        "_SessionToken":"r:e9dc731c360a15567189fe8c414e564b",
        "_ClientVersion":"js3.4.1",
        "_ApplicationId":"E62VyFVLMiW7kvbtVq3p",
        "g_os":"PCWeb",
        "g_ver":"v4.5.4.20230403",
        "_InstallationId":"2d77cdbc-c40f-4ffd-a9fe-249af413a5a7"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        # json_data = response.json()
        # print(json_data)
        print(response.json())
        return response.json()
    else:
        print("Error:", response.text)
        return None

def analyzeWords(words):
    print(words["result"]["results"]["search-all"]["result"]["word"]["searchResult"])
    result = []
    for w in words["result"]["results"]["search-all"]["result"]["word"]["searchResult"]:
        try:
            result.append([w['targetId'], w["title"], w["excerpt"][:w["excerpt"].index("（")]])
        except:
            result.append([w['targetId'], w["title"], w["excerpt"]])
    return result

def analyzeTheWord(word):
    print(word)
    print(word["result"]["result"][0]["details"][0]["title"])
    print(word["result"]["result"][0]["subdetails"])
    cixing = word["result"]["result"][0]["details"][0]["title"]
    spell = word["result"]["result"][0]["word"]["spell"]
    pron = word["result"]["result"][0]["word"]["pron"]
    result = []
    for w in word["result"]["result"][0]["subdetails"]:
        try:
            result.append([cixing, w["title"][:w["title"].index("。")], w["title"][w["title"].index("。")+2:-1]])
        except:
            result.append([cixing, w["title"], w["title"]])
    return spell, pron, result

def hiragana(word):
    url = 'https://api.kuroshiro.org/convert'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }

    payload = {
        "str":word,
        "to":"hiragana",
        "mode":"furigana",
        "romajiSystem":"nippon"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        print("Error:", response.text)
        return None
# analyzeWords("だるま")
# analyzeTheWord("だるま")
# getTheWord("ljvqRpsnJg")
# print(analyzeWords(getWords("だるま")))
# print(analyzeTheWord(getTheWord('198948949')))