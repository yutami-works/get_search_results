'''
Python   3.10.5
selenium 4.2.0
'''
import datetime, glob, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

## call selenium ##
# ブラウザアプデ自動対応
service = Service(executable_path=ChromeDriverManager().install())

# option
options = Options()
options.add_argument('--headless')                                     # バックグラウンドモード
options.add_argument('--disable-extensions')                           # 拡張機能無効
options.add_experimental_option('detach', True)                        # 処理終了後にブラウザ閉じない
options.add_experimental_option('excludeSwitches', ['enable-logging']) # webUSBのログ消す？

driver = webdriver.Chrome(service=service, options=options)

# 定数
URL = 'https://www.yahoo.co.jp/'
X_SEARCH = '//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/input'
CN_RESULT = "Algo"
KEY_PATH = "search_key/*.txt"
RANK = 10
target_num = RANK - 1

# ファイルリスト取得
file_list = glob.glob(KEY_PATH, recursive=True)

##### main loop #####
for file in file_list:

    # タスク開始時刻取得
    exe_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # ファイル読み込み
    with open(file, 'r', encoding='utf-8') as f:
        task_name = f.name.strip('.txt').split('\\') # ここイケてない
        keywords = f.read().split("\n\n")

    # タスク開始
    print('--------------------------------------------------')
    print(f'start {task_name[1]}: {exe_time}') # ここイケてない
    print(f'first word = {keywords[0]}')
    print('--------------------------------------------------')

    # サイトにアクセス
    driver.get(URL)

    for keyword in keywords:
        driver.implicitly_wait(10)
        #EC.visibility_of_element_located((By.XPATH, X_SEARCH)) # なんかエラーになる
        SEARCH_BOX = driver.find_element(By.XPATH, X_SEARCH)
        SEARCH_BOX.send_keys(keyword)
        SEARCH_BOX.submit()

        # 検索結果取得
        #driver.implicitly_wait(10)
        EC.visibility_of_element_located((By.CLASS_NAME, CN_RESULT))
        targets = driver.find_elements(By.CLASS_NAME, CN_RESULT)
        res = len(targets)
        # URL取得
        if res == 0:
            print('次はここから再検索：' + keyword)
            #print('アクセスブロックのためリストをスキップします。（待機3秒）')
            time.sleep(3)
            break
        elif res < RANK:
            print(targets[-1].find_element(By.TAG_NAME, 'a').get_attribute("href"))
        else:
            print(targets[target_num].find_element(By.TAG_NAME, 'a').get_attribute("href"))
        # 検索ページに戻る
        driver.back()   # 戻るボタンがブロックの原因かもなので直す

    print('--------------------------------------------------')
    print(f'last word = {keywords[-1]}')

####### close selenium #####
driver.quit()