import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.google.co.jp/search'

# グーグルへ接続
req = requests.get(url, params={'q': 'パイソン'})
#print(req.text)
html_list=req.text.split('href="/url?q=' )
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