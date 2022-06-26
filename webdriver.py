# seleniumモジュール

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def chromedriver ():
    # ブラウザのバージョンアップにドライバを自動対応
    service = Service(executable_path=ChromeDriverManager().install())

    # オプション
    options = Options()
    options.add_experimental_option('detach', True) # 処理終了後にブラウザ閉じない
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # webUSBのログ消す？

    # start session
    driver = webdriver.Chrome(service=service, options=options)
    return driver