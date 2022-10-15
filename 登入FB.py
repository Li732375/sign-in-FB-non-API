##自動化登入取首兩篇文章並登出關閉
##貼文訊息結構難分析
##欲擷取更多文章(第三篇以上)的話會有障礙
##因為臉書的網站架構是把第三篇以後(記得是五篇)的通通集合打包
##多層次和亂碼的 id，導致定位困難

##介面完成
##測試完成

from selenium import webdriver
from os import system
import time, stdiomask

#https://www.facebook.com/
site = 'https://www.facebook.com/'
#帳號
account = input('帳號?')
#密碼
password = stdiomask.getpass(prompt = '密碼：', mask = '密')

# 關閉通知
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument('disable-infobars')
#1背景執行
#option.add_argument('headless')

# 啟動selenium 務必確認driver 檔案跟python 檔案要在同個資料夾中
driver = webdriver.Chrome(options = options)
driver.get(site)
time.sleep(1.5)

#輸入email 
context = driver.find_element_by_css_selector('#email')
context.send_keys(account) 
time.sleep(0.5)

#輸入password
context = driver.find_element_by_css_selector('#pass')
context.send_keys(password)
time.sleep(0.5)

#按下登入紐
#因為臉書有兩種登入頁面
try:
    commit = driver.find_element_by_css_selector('#loginbutton')
except:
    commit = driver.find_element_by_css_selector('button[data-testid= \'royal_login_button\']')

commit.click()
time.sleep(1)

#抓第一筆貼文
info = driver.find_element_by_css_selector('.userContentWrapper')
print(info.text)

print('\n---------------------------------------\n')

#抓第二筆貼文
info_1 = driver.find_element_by_css_selector('div[id = \'substream_1\']')
print(info_1.text)

#按下三角形
commit = driver.find_element_by_css_selector('#pageLoginAnchor')
commit.click()
time.sleep(1)

#按下登出紐
commit = driver.find_element_by_css_selector('li[data-gt=\'{"ref":"async_menu","logout_menu_click":"menu_logout"}\']')
commit.click()
time.sleep(1)

#關閉瀏覽器全部標籤頁
driver.quit()

print('完成\n')
system('pause')
