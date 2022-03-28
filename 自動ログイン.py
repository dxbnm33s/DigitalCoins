from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import datetime
import chromedriver_binary

Email = ""
Password = ""


#ブラウザを開く
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(3)


#トップページのURLを取得
url = "https://cex.ethereum-express.com/"
browser.get(url)
time.sleep(3)

#ログインページへ推移
element = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/a[1]')

time.sleep(3)
element.click()


#Emailアドレスとパスワードを入力
element = browser.find_element_by_name("email")
element.clear()
element.send_keys(Email)
element = browser.find_element_by_name("password")
element.clear()
element.send_keys(Password)

#ログインボタンを押す
browser_from = browser.find_element_by_xpath('/html/body/div[1]/div/form/button')
time.sleep(3)
browser_from.click()
time.sleep(3)


#Exchangeページに推移
element1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/a[1]')
element1.click()
time.sleep(3)


#EEX/USDの数値を取得
element2 = browser.find_element_by_xpath('//*[@id="app"]/main/div/div/div[1]/div[1]/text()')
time.sleep(3)
print(element2.text)

rate = float(element2.text)


#遷移後のURL
browser.get('https://wallet.ethereum-express.com/')

#Import Walletボタンを押す 
element4 = browser.find_element_by_xpath('/html/body/div/section/div[4]/div/div[1]/button[2]')
element4.click()
time.sleep(3)

#Seed phraseに記入
SeedPhrases = "obvious core appear boat ripple ski sell excite various text gap lyrics"
element5 = browser.find_element_by_xpath('/html/body/div/section/div[4]/div/form/label[1]/textarea')
element5.clear()
element5.send_keys(SeedPhrases)

#New passwordに記入
element5 = browser.find_element_by_xpath('/html/body/div/section/div[4]/div/form/label[2]/input')
element5.click()
time.sleep(3)
element5.send_keys(Password)

#Confirm passwordに記入
element5 = browser.find_element_by_xpath('/html/body/div/section/div[4]/div/form/label[3]/input')
element5.click()
time.sleep(3)
element5.send_keys(Password)

#LOG IN TO WALLET
element5 = browser.find_element_by_xpath('/html/body/div/section/div[4]/div/form/button')
element5.click()
time.sleep(3)

#現在のEEX総額を取得
element5 = browser.find_element_by_xpath('/html/body/div/div/div/section/div[2]/div[1]/div/div/p[2]')
time.sleep(3)
print(element5.text)
sumeex = float(element5.text)



#EEX総額とETD/USDの積を出力

dollars = rate * sumeex
print(dollars)



#Googleの検索画面に遷移

url2 = "https://www.google.co.jp/"
browser.get(url2)
time.sleep(3)
element6 = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
element6.click()
time.sleep(3)


#検索欄に「〜ドル　日本円」を入力
element6.send_keys(str(dollars) +"ドル　日本円")
element7 = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
element7.click()
time.sleep(3)

#現在の日本円の数値を取得して出力
element8 = browser.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')

japaneseYen = element8.text

print(japaneseYen)

print("７万円の投資による現在のリターンは、" + japaneseYen + "円です。")




