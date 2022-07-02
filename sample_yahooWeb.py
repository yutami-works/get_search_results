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

# 変数定義
URL = 'https://www.yahoo.co.jp/'
X_SEARCH = '//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/input'
keyword = '東條希'

# サイトにアクセス
driver.get(URL)
driver.implicitly_wait(10)
SEARCH_BOX = driver.find_element(By.XPATH, X_SEARCH)
SEARCH_BOX.send_keys(keyword)
SEARCH_BOX.submit()

# 検索結果ページ
driver.implicitly_wait(10)
#target = driver.find_element(By.CLASS_NAME, "Algo")
targets = driver.find_elements(By.CLASS_NAME, "Algo")
if len(targets) == 0:
    print(f'検索結果なし' + keyword)
# タイトル
t_title = targets.find_element(By.TAG_NAME, 'h3').get_attribute('innerText')
print(t_title)
# URL
t_url = targets.find_element(By.TAG_NAME, 'a').get_attribute("href")
print(t_url)

print(len(targets))
#driver.quit()