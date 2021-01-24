import MeCab
import re
import zipfile
import urllib.request
import os.path
import glob
import itertools
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import japanize_matplotlib


def main():
    # ファイルパスの取得
    download_file = download(URL)
    # 本文のみ抽出
    text = convert(download_file)
    # 文単位のリストに分割
    sentences = text.split("。")

    mecab = MeCab.Tagger("-Ochasen")

    # 文単位の名詞リストを生成
    noun_list = [
        [v.split()[2] for v in mecab.parse(sentence).splitlines()
         if (len(v.split()) >= 3 and v.split()[3][:2] == '名詞')]
        for sentence in sentences
    ]

    # 文単位の名詞ペアリストを生成
    pair_list = [
        list(itertools.combinations(n, 2))
        for n in noun_list if len(noun_list) >= 2
    ]

    # 名詞ペアリストの平坦化
    all_pairs = []
    for u in pair_list:
        all_pairs.extend(u)

    # 名詞ペアの頻度をカウント
    cnt_pairs = Counter(all_pairs)

    tops = sorted(
        cnt_pairs.items(),
        key=lambda x: x[1], reverse=True
    )[:50]

    noun_1 = []
    noun_2 = []
    frequency = []

    # データフレームの作成
    for n, f in tops:
        noun_1.append(n[0])
        noun_2.append(n[1])
        frequency.append(f)

    df = pd.DataFrame({'前出名詞': noun_1, '後出名詞': noun_2, '出現頻度': frequency})

    print(df)

    # 重み付きデータの設定
    weighted_edges = np.array(df)

    # グラフオブジェクトの生成
    G = nx.Graph()

    print(G)

    # 重み付きデータの読み込み
    G.add_weighted_edges_from(weighted_edges)

    # ネットワーク図の描画
    plt.figure(figsize=(10, 10))
    nx.draw_networkx(G,
                     node_shape="s",
                     node_color="c",
                     node_size=500,
                     edge_color="gray",
                     font_family="IPAexGothic")  # フォント指定

    plt.show()


def download(URL):
    # zipファイルのダウンロード
    zip_file = re.split(r'/', URL)[-1]
    urllib.request.urlretrieve(URL, zip_file)
    dir = os.path.splitext(zip_file)[0]

    # zipファイルの解凍と保存
    with zipfile.ZipFile(zip_file) as zip_object:
        zip_object.extractall(dir)
    os.remove(zip_file)

    # テキストファイルのパスを取得
    path = os.path.join(dir, '*.txt')
    list = glob.glob(path)
    return list[0]


def convert(download_text):
    # ファイルの読み込み
    data = open(download_text, 'rb').read()
    text = data.decode('shift_jis')

    # 本文の抽出
    text = re.split(r'\-{5,}', text)[2]
    text = re.split(r'底本：', text)[0]
    text = re.split(r'［＃改ページ］', text)[0]

    # 不要部分の削除
    text = re.sub(r'《.+?》', '', text)
    text = re.sub(r'［＃.+?］', '', text)
    text = re.sub(r'｜', '', text)
    text = re.sub(r'\r\n', '', text)
    text = re.sub(r'\u3000', '', text)
    text = re.sub(r'「', '', text)
    text = re.sub(r'」', '', text)

    return text


if __name__ == '__main__':
    URL = 'https://www.aozora.gr.jp/cards/000148/files/772_ruby_33099.zip'
    main()
