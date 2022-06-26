# get_search_results
検索結果スクレイピングツール（仮）

## 概要
現状は[jungordm0x0m](https://crowdworks.jp/public/employers/1359924)の「コピペでPC簡単作業！」を自動化するツールとして運用

## 主な機能
キーワードリストに記載されている単語をYahooJapanで検索し、検索結果の最後にヒットしたページのURLを取得していく。

検索するキーワードはkeywords/target.txtを参照している。

jungordm0x0mのタスクに記載されている単語をコピペできるように、改行2つ区切りで配列化している。

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

#### 2. スクリプト実行
```shell
$ python get_yahoo_results.py
```