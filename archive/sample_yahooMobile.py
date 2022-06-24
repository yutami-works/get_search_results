'''
Python   3.10.5
selenium 4.2.0
'''
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
mobile_emulation = { "deviceName": "iPhone 12 Pro" }
options.add_experimental_option("mobileEmulation", mobile_emulation)

# start session
driver = webdriver.Chrome(service=service, options=options)

# 変数定義
URL = 'https://m.yahoo.co.jp'
keyword = '東條希'

# サイトにアクセス
driver.get(URL)
driver.implicitly_wait(10)
#CLOSE = driver.find_element(By.XPATH, '//*[@id="log-modal"]/section/button')
SEARCH_BOX = driver.find_element(By.XPATH, '//*[@id="log-search"]/form/div[1]/div/input')
#SEARCH_BUTTON = driver.find_element(By.XPATH, '//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/button/span/span')

SEARCH_BOX.send_keys(keyword)
SEARCH_BOX.submit()
#SEARCH_BUTTON.click()

# 検索結果ページ
driver.implicitly_wait(10)
target = driver.find_element(By.CLASS_NAME, "Algo")
# タイトル
t_title = target.find_element(By.TAG_NAME, 'h3').get_attribute('innerText')
print(t_title)
# URL
t_url = target.find_element(By.TAG_NAME, 'a').get_attribute("href")
print(t_url)

#driver.quit()