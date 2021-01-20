import requests
import re

url = 'https://www.google.co.jp/search'

# グーグルへ接続
req = requests.get(url, params={'q': 'パイソン'})



address_list=req.text.split('"' )

count=-1
for i in address_list:
    count+=1
    postcode = re.match('http' , i)
    if postcode:
        print(address_list[count])
#    else:
#        print ("失敗")
