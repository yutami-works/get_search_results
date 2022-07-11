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
mobile_emulation = { "deviceName": "iPhone SE" }
options = Options()
options.add_argument('--headless')                                     # バックグラウンドモード
options.add_argument('--window-size=375,667')
options.add_experimental_option('detach', True)                        # 処理終了後にブラウザ閉じない
options.add_experimental_option('excludeSwitches', ['enable-logging']) # webUSBのログ消す？
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(service=service, options=options)
#driver.set_window_size(375,667)

## 変数定義 ##
URL = 'https://m.yahoo.co.jp'
NAME_SEARCH = 'p'
RANK = 10
target_num = RANK - 1
exe_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

# loading words list
with open('./keywords/target.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().split("\n\n")

########## main ##########
print('--------------------------------------------------')
print('start: %s' %exe_time)
print('first word = ' + keywords[0])
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
    #next = driver.find_element(By.XPATH, '//*[@id="contents__wrap"]/div[1]/div[3]/div[2]/div/div[1]/a[1]')
    # 検索結果の一覧取得
    targets = driver.find_elements(By.CLASS_NAME, "Algo")
    # URL取得
    print(targets[-1].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    # 検索ページに戻る
    driver.back()

print('--------------------------------------------------')
print('last word = ' + keywords[-1])
print('--------------------------------------------------')

driver.quit()