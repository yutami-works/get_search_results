# get_search_results
検索結果スクレイピングツール（仮）

## 概要
現状は[jungordm0x0m](https://crowdworks.jp/public/employers/1359924)の「コピペでPC簡単作業！」「コピペで簡単スマホ作業！」を自動化するツールとして運用。

## 主な機能
キーワードリストに記載されている単語をYahooJapanで検索し、検索結果の最後にヒットしたページのURLを取得していく。<br>
検索するキーワードは、各作業ディレクトリに<タスク名>.txtを作成し、ループで参照している。<br>
jungordm0x0mのタスクに記載されている単語をコピペできるように、改行2つ区切りで配列化している。<br>

## 残課題
- エラーハンドリングしていない（find_elementに失敗するとループが止まってしまう）
  →暫定的な対応としてfind_elementが0ならリストをスキップ
    →スキップにしてもリトライにしても時間でアクセス禁止なので待機時間が必要
      →取得できなくても変数nullとして処理が進むのでリトライの実装方法要検討
- そもそも10位のURLを取得していない（ラス配取りでごまかしている）
  →これはこなしてきた肌感的にこだわる必要なさそう
- そもそもワードリスト作成手動なのダサくね？
  →URLのリストからループでdescriptionの値を引っ張ってきてワードリスト作成とかできそう
    →これを応用すれば作業結果の貼り付けもできそう？

## バージョン情報
|  ---      |  version  |
|  ----     |  ----     |
|  Python   |  3.10.5   |
|  selenium |  4.2.0    |

## 環境構築手順（Windows）
#### 1. Pythonのインストール
https://www.python.org/

#### 2. Pythonインストール確認
```shell
$ python --version
```

#### 3. Seleniumのインストール
```shell
$ pip install selenium
```

#### 4. webdriver_managerのインストール
```shell
$ pip install webdriver_manager
```

#### 5. モジュールインストール確認
```shell
$ pip list
```

#### 6. リポジトリをクローン
```shell
$ git clone {url}
```

## 実行手順
#### 1. ディレクトリ移動
```shell
$ cd "クローンしたディレクトリ"
```
※エクスプローラ上でcmdでも可

#### 2. 検索ワードリスト作成
作業ディレクトリに<タスク名>.txtを作成し、検索ワードをコピペ（1ワード\n\n区切り）

#### 3. スクリプト実行
YahooJapanの場合
```shell
$ python get_yjsearch_results.py
```
スマホ版YahooJapanの場合
```shell
$ python get_ymobile_results.py
```
Yahooショッピングの場合
```shell
$ python get_yshopping_results.py
```