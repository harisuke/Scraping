import urllib.request as req
import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.google.co.jp/search'

# グーグルへ接続
req1 = requests.get(url, params={'q': 'パイソン'})
#print(req.text)
html_list=req1.text.split('href="/url?q=' )
#req=BeautifulSoup(req,"html.parser")
#html_list=req.split('href="/url?q=')
print("ok1")
def split_html(html_list,split_word):
    address_list = []
    for i in html_list:
        kari_list = i.split(split_word)
        count = -1
        for j in kari_list:
            count += 1
            postcode = re.match('https', j)
            if postcode:

                address_list.append(kari_list[count])
    return address_list

html_list =split_html(html_list,"/&amp;sa=")
html_list =split_html(html_list,'">')
html_list =split_html(html_list,'&')
html_list =split_html(html_list,'%')
html_list =set(html_list)
for i in  html_list:
    print(i)


title_text_list=[]
for i in html_list:
    print(i)
    url = i  # URLを指定
    response = req.urlopen(url)
    parse_html = BeautifulSoup(response, "html.parser")
    list = parse_html.find_all("body")  # 抜き出す箇所を指定
    title_text_list.append(list[0].get_text())
    print(title_text_list)
