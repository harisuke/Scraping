from bs4 import BeautifulSoup
import urllib.request as req


url="http://kino-code.work/python-scraping/"   #URLを指定
response=req.urlopen(url)

parse_html = BeautifulSoup(response,"html.parser")

list=parse_html.find_all("body")   #抜き出す箇所を指定

print(list)