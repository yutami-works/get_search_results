'''
Python   3.10.5
selenium 4.2.0
'''
import time, datetime, glob
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
URL = 'https://www.yahoo.co.jp/'
X_SEARCH = '//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/input'
RANK = 10
target_num = RANK - 1
exe_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

# loading words list
with open('./keywords/target.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().split("\n\n")

########## main ##########
print('--------------------------------------------------')
print(f'start: {exe_time}')
print(f'first word = {keywords[0]}')
print('--------------------------------------------------')

# サイトにアクセス
driver.get(URL)

for keyword in keywords:
    driver.implicitly_wait(10)
    SEARCH_BOX = driver.find_element(By.XPATH, X_SEARCH)
    SEARCH_BOX.send_keys(keyword)
    SEARCH_BOX.submit()

    # 検索結果ページ
    driver.implicitly_wait(10)
    # 検索結果の一覧取得
    targets = driver.find_elements(By.CLASS_NAME, "Algo")
    res = len(targets)
    # URL取得
    if res == 0:
        print('再検索：' + keyword)
    elif res < RANK:
        print(targets[-1].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    else:
        print(targets[target_num].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    # 検索ページに戻る
    driver.back()

print('--------------------------------------------------')
print(f'last word = {keywords[-1]}')
print('--------------------------------------------------')

driver.quit()