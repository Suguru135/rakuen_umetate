from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import rakuen
import time
from getpass import getpass



if __name__ == "__main__":

    #ログイン
    id_str = input("ID: ")
    password_str = getpass('パスワード: ')
    
    #設定
    times = 3
    no_str = '6'
    name_str = 'びーびー'
    contents_str = ('最終確認\n'
                    'test')
    

    #webdriverを準備
    chrome_options = Options()
    chrome_options.set_headless(True)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(10)


    if rakuen.authenticate(driver, id_str, password_str):
        for i in range(times):
            if rakuen.post(driver, no_str, name_str, password_str, contents_str):
                print('投稿')

            else:
                print("投稿失敗")

            time.sleep(2.5)

    else:
        print('認証失敗')
    


    #webdriverを閉じる
    driver.close()
    driver.quit()
	
	

