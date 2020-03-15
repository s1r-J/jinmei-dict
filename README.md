jinmei-dict
====

下記の辞書データから人名だけを抜き出し、
読み仮名（カタカナ）をキーとして、候補となる書き文字をリストで保持するようなJSON形式に整形しています。

- [NAIST-jdic](https://ja.osdn.net/projects/naist-jdic/wiki/FrontPage)
- [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd)
- 自作辞書データ(`data/addon.csv`)

2020年3月15日時点では、  
姓は読み仮名が54,957語で漢字候補は99,413語、名の読み仮名が15,740語で漢字候補は111,669語となっています。

利用できる辞書データの探索と自作辞書へのデータ追加が課題です。

## Description

`sei.json`は姓のデータです。`mei.json`は名のデータです。  

scriptsフォルダ以下には人名データを抜き出してJSONに整形するスクリプト（Python）があります。  
使い方は以下のとおりです。

1. 各辞書データのCSVファイル（mecab形式）を用意します。
2. scripts/jinmei-dict.pyを実行します。（Python3）
```
python jinmei-jdic.py '~/naist-jdic.csv' '~/mecab-user-dict-seed.yyyyMMdd.csv' '~/addon.csv'
```

## Usage

jinmeiフォルダ以下に姓・名それぞれのJSONデータがあります。

かんたんに使うだけなら、GitHub Pagesで作成した[サイト](https://s1r-j.github.io/jinmei-dict/)で読み仮名から人名漢字を検索する事ができます。

## Licence

[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

## Author

[s1r-J](https://github.com/s1r-J)
