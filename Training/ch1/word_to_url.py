import requests
import re

url = 'https://www.google.co.jp/search'

# グーグルへ接続
req = requests.get(url, params={'q': 'パイソン'})



html_list=req.text.split('"' )
address_list=[]
count=-1
for i in html_list:
    count+=1
    postcode = re.match('http',i)
    if postcode:
        print(html_list[count])
        address_list.append(html_list[count])
#    else:
#        print ("失敗")
