from pytrends.request import TrendReq

# googleに接続
pytrend = TrendReq(hl='ja-jp',tz=540)

# キーワードの設定　5キーワード以上は内部エラーになる
kw_list = ['アイカツ']
# googleにリクエストする。
pytrend.build_payload(kw_list=kw_list, timeframe='2020-11-28T15 2020-11-29T15', geo="JP")
# Pandasで内容をまとめる
print(pytrend.interest_over_time())