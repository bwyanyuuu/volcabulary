import requests, json

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
        json_data = response.json()
        print(json_data)
        return response.json()
    else:
        print("Error:", response.text)
        return None

def analyzeWords(words):
    j = {
    "result":{
        "code":200,
        "results":{
            "search-all":{
                "code":200,
                "result":{
                    "word":{
                        "searchResult":[
                            {
                                "targetId":"198983454",
                                "targetType":102,
                                "title":"達磨 | だるま ◎",
                                "excerpt":"[名] 〈佛〉达磨。（中国禅宗の始祖。インドのバラモンの出身と伝え、6世紀初め中国に渡り、各地で禅を教えた。） ",
                                "isFree":True
                            },
                            {
                                "targetId":"198917185",
                                "targetType":102,
                                "title":"ダルマ | だるま ◎",
                                "excerpt":"[名] dharma佛教的达摩；修行。（禅宗の始祖、達磨大師の坐禅姿をうつした縁起物玩具。赤塗りで、座におもりをつけ、倒してもすぐ立つようにつくった張り子製の起きあがり物が、全国各地でつくられている。） ",
                                "isFree":True
                            },
                            {
                                "targetId":"198976869",
                                "targetType":102,
                                "title":"雪だるま | ゆきだるま ③",
                                "excerpt":"[名詞] 雪人；堆雪人。（雪を固めて達磨の形にこしらえたもの。）",
                                "isFree":True
                            },
                            {
                                "targetId":"198976936",
                                "targetType":102,
                                "title":"雪達磨 | ゆきだるま ③",
                                "excerpt":"[名] 雪人。（雪を丸めてだるまの形にし、木炭や炭団(たどん)で目鼻口をつけたもの。） ",
                                "isFree":True
                            }
                        ]
                    },
                    "grammar":{
                        "searchResult":[
                            
                        ]
                    },
                    "example":{
                        "searchResult":[
                            {
                                "targetId":"bsUpGIk0Kz",
                                "targetType":103,
                                "title":"火だるま"
                            }
                        ]
                    }
                }
            },
            "mojitest-examV2-searchQuestion-v2":{
                "670":[
                    
                ],
                "671":[
                    
                ],
                "result":[
                    
                ],
                "limit":1,
                "page":1,
                "examsNum":73,
                "code":200
            }
        }
    }
}

def analyzeTheWord(word):
    j = {
    "result":{
        "1":[
            
        ],
        "result":[
            {
                "word":{
                    "excerpt":"[名] 〈佛〉达磨。（中国禅宗の始祖。インドのバラモンの出身と伝え、6世紀初め中国に渡り、各地で禅を教えた。） ",
                    "spell":"達磨",
                    "accent":"◎",
                    "pron":"だるま",
                    "romaji":"daruma",
                    "createdAt":"2019-05-07T03:51:28.072Z",
                    "updatedAt":"2023-04-11T18:40:03.059Z",
                    "isFree":True,
                    "quality":1000,
                    "viewedNum":1800,
                    "objectId":"198983454"
                },
                "details":[
                    {
                        "title":"名",
                        "index":0,
                        "createdAt":"2019-05-07T03:51:30.314Z",
                        "updatedAt":"2019-10-24T12:55:30.905Z",
                        "wordId":"198983454",
                        "objectId":"68922"
                    }
                ],
                "subdetails":[
                    {
                        "title":"〈佛〉达磨。（中国禅宗の始祖。インドのバラモンの出身と伝え、6世紀初め中国に渡り、各地で禅を教えた。）",
                        "index":0,
                        "createdAt":"2019-05-07T03:51:31.667Z",
                        "updatedAt":"2019-10-24T13:01:49.466Z",
                        "wordId":"198983454",
                        "detailsId":"68922",
                        "objectId":"95851"
                    },
                    {
                        "title":"不倒翁，扳不倒儿。（達磨大師の座禅の姿にまねた張り子の人形。手足がなく、紅衣をまとった僧の形で、底を重くして、倒してもすぐ起き上がるように作る。）",
                        "index":1,
                        "createdAt":"2019-05-07T03:51:33.070Z",
                        "updatedAt":"2019-10-24T13:01:56.926Z",
                        "wordId":"198983454",
                        "detailsId":"68922",
                        "objectId":"95852"
                    },
                    {
                        "title":"圆（形物）。（丸いもの、赤いものなど1の形に似たものの称。）",
                        "index":2,
                        "createdAt":"2019-05-07T03:51:32.749Z",
                        "updatedAt":"2019-10-24T13:01:56.639Z",
                        "wordId":"198983454",
                        "detailsId":"68922",
                        "objectId":"95853"
                    }
                ],
                "examples":[
                    {
                        "title":"達磨ストーブ。",
                        "index":0,
                        "trans":"圆火炉。",
                        "createdAt":"2019-05-07T03:51:34.142Z",
                        "updatedAt":"2019-10-24T13:08:48.243Z",
                        "wordId":"198983454",
                        "subdetailsId":"95853",
                        "isFree":True,
                        "quality":1000,
                        "isChecked":False,
                        "objectId":"71720",
                        "notationTitle":"<ruby ><rb>達磨</rb><rp>(</rp><rt roma=\"daruma\" hiragana=\"だるま\" lemma=\"達磨\" lemma-t=\"\"></rt><rp>)</rp></ruby><span class=\"moji-toolkit-org\"  lemma=\"ストーブ-stove\" lemma-t=\"stove\">ストーブ</span><span class=\"moji-toolkit-org\"  lemma=\"。\" lemma-t=\"\">。</span>"
                    },
                    {
                        "title":"達磨船。",
                        "index":1,
                        "trans":"驳船。",
                        "createdAt":"2019-05-07T03:51:35.470Z",
                        "updatedAt":"2023-03-01T01:16:39.162Z",
                        "wordId":"198983454",
                        "subdetailsId":"95853",
                        "isFree":True,
                        "quality":1000,
                        "isChecked":False,
                        "viewedNum":2,
                        "objectId":"71721",
                        "notationTitle":"<ruby ><rb>達磨</rb><rp>(</rp><rt roma=\"daruma\" hiragana=\"だるま\" lemma=\"達磨\" lemma-t=\"\"></rt><rp>)</rp></ruby><ruby n4 n5><rb>船</rb><rp>(</rp><rt roma=\"sen\" hiragana=\"せん\" lemma=\"船\" lemma-t=\"\"></rt><rp>)</rp></ruby><span class=\"moji-toolkit-org\"  lemma=\"。\" lemma-t=\"\">。</span>"
                    }
                ]
            }
        ],
        "code":200
    }
}

getTheWord("ljvqRpsnJg")