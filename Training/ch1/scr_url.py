from bs4 import BeautifulSoup
import urllib.request as req

# 為替情報XMLを取得
url = "https://news.yahoo.co.jp/rss/topics/it.xml"
res = req.urlopen(url)
#print(res,"res")
print("*******************")
# HTMLを解析
soup = BeautifulSoup(res, "html.parser")
#print(soup,"soup")
print("*****************")
# 任意のデータを抽出 --- (※1)
#links = soup.find_all("item")
links = soup.select("link")
print("link=",links)
print("link=",links)