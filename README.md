jinmei-dict
====

下記の辞書データから人名だけを抜き出し、
読み仮名（カタカナ）をキーとして、候補となる書き文字をリストで保持するようなJSON形式に整形しています。

さらに、厚生労働省のウェブサイトにあった異体字リストを参考に異体字対応表（`scripts/itaiji.json`）を作成し、
辞書データから取得した書き文字を異体字に変換して追加登録しました。

- [NAIST-jdic](https://ja.osdn.net/projects/naist-jdic/wiki/FrontPage)
- [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd)
- 自作辞書データ(`data/addon.csv`)

2020年4月2日時点では、  
姓は読み仮名が54,970語で漢字候補は210,676語、名の読み仮名が15,740語で漢字候補は186,651語となっています。

利用できる辞書データの探索と自作辞書へのデータ追加が課題です。

## Description

`sei.json`は姓のデータです。`mei.json`は名のデータです。  

scriptsフォルダ以下には人名データを抜き出してJSONに整形するスクリプト（Python）があります。  
使い方は以下のとおりです。

1. 各辞書データのCSVファイル（mecab形式）を用意します。
2. 異体字リスト（`scripts/itaiji.json`）をスクリプトと同じ位置に配置します。
3. scripts/jinmei-dict.pyを実行します。（Python3）
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
