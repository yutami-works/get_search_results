'''
Python   3.10.5
selenium 4.2.0
'''
# 待機は拘るところではないので一旦time.sleepで実装
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ブラウザのバージョンアップにドライバを対応させる
service = Service(executable_path=ChromeDriverManager().install())

# オプション
options = Options()
options.add_experimental_option('detach', True) # 処理終了後にブラウザ閉じない
options.add_experimental_option('excludeSwitches', ['enable-logging']) # webUSBのログ消す？

# start session
driver = webdriver.Chrome(service=service, options=options)

# 定数
URL = 'https://www.google.co.jp/'
RANK = 3

# 変数
target_num = RANK - 1
with open('./keywords/target.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().split("\n")

# サイトにアクセス
driver.get(URL)

for keyword in keywords:
    driver.implicitly_wait(10)
    SEARCH_BOX = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    SEARCH_BOX.send_keys(keyword)
    SEARCH_BOX.submit()

    # 検索結果ページ
    # 一旦time.sleep
    time.sleep(1)
    #driver.implicitly_wait(10)
    #next = driver.find_element(By.XPATH, '//*[@id="contents__wrap"]/div[1]/div[3]/div[2]/div/div[1]/a[1]')
    # 検索結果の一覧取得
    targets = driver.find_elements(By.CLASS_NAME, "yuRUbf")
    # URL取得
    print(keyword)
    print(targets[target_num].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    # 検索ページに戻る
    driver.back()

driver.quit()