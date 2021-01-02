from bs4 import BeautifulSoup
import urllib.request as req

# 為替情報XMLを取得
url = "https://news.yahoo.co.jp/articles/6e3ca529dc95714b773ca32ff47091d0ba0d04dd"
res = req.urlopen(url)
#print(res,"res")
print("*******************")
# HTMLを解析
soup = BeautifulSoup(res, "html.parser")

#print(soup,"soup")
print("*****************")
# 任意のデータを抽出 --- (※1)
print(type(soup),"soup")
#texts = soup.find_all("p")
texts=soup.select("div main div div article p")
#print(soup.get_text())
print(type(texts[0]),"texts")
for i in texts:
    #texts=i
    texts=i.string
    print(i.get_text())
#    texts=i
#    print(texts)
