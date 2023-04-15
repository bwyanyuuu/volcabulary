import urllib.request
from bs4 import BeautifulSoup

userAgent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36 Edg/97.0.1072.69"
headers = {'User-Agent': userAgent}
CIXING = {None: ' ',
          'adverb': '副',
          'verb': '動',
          'adjective': '形',
          'noun': '名',
          'pronoun': '代',
          'preposition': "介",
          'conjunction': "連",
          'interjetion': '感',
          'modal verb': '助'}

# 請求網頁內容
def getHtml(url, headers):
    req = urllib.request.Request(url, headers = headers)
    # print("1")
    page = urllib.request.urlopen(req)
    # print("2")
    html = page.read().decode('UTF-8')
    return html

# 替換全形標點符號
def replaceLetter(word): 
    # print(type(word))
    word = word.replace('，', ', ')
    word = word.replace('；', ', ')
    word = word.replace('（', '(')
    word = word.replace('）', ')')
    return word

# 分析辭典網站回傳結果
def dictionary(word):
    word = word.split(' ')
    rq_url = "https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/" + word[0]
    for i in range(1, len(word)):
        rq_url += "-" + word[i]
    # print(rq_url)
    html = getHtml(rq_url, headers)
    # print("get")
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find_all(class_="entry-body__el")
    
    # print(len(content))
    # for c in content:
    #     cixing = CIXING[c.find(class_="dpos").text]
    #     block = c.find_all(class_="dsense")
    #     print(len(block), cixing)
    #     for b in block:
    #         for d in b.find_all(class_="def-body"):
    #             print(replaceLetter(d.find("span").text))
    # soup.find_all(class_="dpos").text
    # cixing = CIXING[soup.find(class_="dpos").text]
    # print(cixing)
    li = []
    for d in soup.find_all(class_="def-body"):
        cixing = d.find_previous(class_="dpos")
        if cixing and cixing.text in CIXING.keys():
            cixing = CIXING[cixing.text]
        elif cixing:
            cixing = cixing.text
        else:
            cixing = CIXING[cixing]
        li.append([cixing, replaceLetter(d.find("span").text)])
    return li

# def addWord(db, data):

