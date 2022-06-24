'''
Python   3.10.5
selenium 4.2.0
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ブラウザのバージョンアップにドライバを自動対応
service = Service(executable_path=ChromeDriverManager().install())

# オプション
options = Options()
options.add_experimental_option('detach', True) # 処理終了後にブラウザ閉じない
options.add_experimental_option('excludeSwitches', ['enable-logging']) # webUSBのログ消す？

# start session
driver = webdriver.Chrome(service=service, options=options)

# 定数
URL = 'https://www.yahoo.co.jp/'
RANK = 10

# 変数
target_num = RANK - 1

# 検索ワード読み込み
with open('./keywords/target.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().split("\n\n")

print('--------------------------------------------------')
print('start getting search results...')
print('--------------------------------------------------')

# サイトにアクセス
driver.get(URL)

for keyword in keywords:
    driver.implicitly_wait(10)
    SEARCH_BOX = driver.find_element(By.XPATH, '//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/input')
    SEARCH_BUTTON = driver.find_element(By.XPATH, '//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/button/span/span')

    SEARCH_BOX.send_keys(keyword)
    SEARCH_BUTTON.click()

    # 検索結果ページ
    # 読み込み待機は一旦time.sleepで実装
    time.sleep(1)
    #driver.implicitly_wait(10)
    #next = driver.find_element(By.XPATH, '//*[@id="contents__wrap"]/div[1]/div[3]/div[2]/div/div[1]/a[1]')
    # 検索結果の一覧取得
    targets = driver.find_elements(By.CLASS_NAME, "Algo")
    # URL取得
    print(keyword)
    print(targets[-1].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    # 検索ページに戻る
    driver.back()

driver.quit()