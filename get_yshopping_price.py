'''
Python   3.10.5
selenium 4.2.0
'''
import time, datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

## call selenium ##
# ブラウザアプデ自動対応
service = Service(executable_path=ChromeDriverManager().install())

# option
options = Options()
options.add_argument('--headless')                                     # バックグラウンドモード
options.add_experimental_option('detach', True)                        # 処理終了後にブラウザ閉じない
options.add_experimental_option('excludeSwitches', ['enable-logging']) # webUSBのログ消す？

driver = webdriver.Chrome(service=service, options=options)

## 変数定義 ##
URL = 'https://shopping.yahoo.co.jp/'
NAME_SEARCH = 'p'
CN_PRICE = "_15NzwMnSG6fE"
exe_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

# loading words list
with open('./keywords/target.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().split("\n\n")

########## main ##########
print('--------------------------------------------------')
print('start: ' + exe_time)
print('--------------------------------------------------')

# サイトにアクセス
driver.get(URL)

for keyword in keywords:
    driver.implicitly_wait(10)
    SEARCH_BOX = driver.find_element(By.NAME, NAME_SEARCH)
    SEARCH_BOX.send_keys(keyword)
    SEARCH_BOX.submit()

    # 検索結果ページ
    driver.implicitly_wait(10)
    # 先頭商品の価格取得
    target_price = driver.find_element(By.CLASS_NAME, CN_PRICE).get_attribute('innerHTML')
    print(keyword + '：' +target_price + '円')
    # 検索ページに戻る
    driver.back()

print('--------------------------------------------------')

driver.quit()