'''
Python   3.10.5
selenium 4.2.0
'''
# 待機は拘るところではないので一旦time.sleepで実装
import time, pprint

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
URL = 'https://www.yahoo.co.jp/'
RANK = 10

# 変数
target_num = RANK - 1
with open('./keywords/target.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().split("\n\n")

keyword = '東條希'

# サイトにアクセス
driver.get(URL)
driver.implicitly_wait(10)

SEARCH_BOX = driver.find_element(By.XPATH, '//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/input')
SEARCH_BUTTON = driver.find_element(By.XPATH, '//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/button/span/span')

SEARCH_BOX.send_keys(keyword)
SEARCH_BUTTON.click()

# 検索結果ページ
# 戻るボタン拾って時間稼ぎ
driver.implicitly_wait(10)
next = driver.find_element(By.XPATH, '//*[@id="contents__wrap"]/div[1]/div[3]/div[2]/div/div[1]/a[1]')
# 検索結果の一覧取得
targets = driver.find_elements(By.CLASS_NAME, "Algo-anotherSuggest")
results_num = len(targets)
print(results_num)
# 10番目がない時は次のページ
if results_num < target_num:
    next.click()
    target_num = target_num - results_num
    driver.implicitly_wait(10)
    next = driver.find_element(By.XPATH, '//*[@id="contents__wrap"]/div[1]/div[3]/div[2]/div/div[1]/a[1]')
    targets = driver.find_elements(By.CLASS_NAME, "Algo-anotherSuggest")
    results_num = len(targets)
    print(results_num)

pprint.pprint(targets)
# URL取得
print(targets[9].find_element(By.TAG_NAME, 'a').get_attribute("href"))
#print(targets[target_num].find_element(By.TAG_NAME, 'h3').get_attribute('innerText'))
# 検索ページに戻る
driver.back()

driver.quit()