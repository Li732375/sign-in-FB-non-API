##測試完成
##介面完成

##自動化登入取首兩篇文章並登出關閉
##貼文訊息結構難分析
##欲擷取更多文章(第三篇以上)的話會有障礙
##因為臉書的網站架構是把第三篇以後(記得是五篇)的通通集合打包
##多層次和亂碼的 id，導致定位困難


from selenium import webdriver
from os import system
import time, stdiomask, random

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
#背景執行
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
    commit = driver.find_element_by_css_selector('button[data-testid =\'royal_login_button\']')

commit.click()
time.sleep(0.5)

#點選watch
driver.get('https://www.facebook.com/watch/?from=bookmark')
time.sleep(1.3)

#給予隨機數作目標
length = random.randint(0, 100) + 2
count = 0
print('隱藏 ' + str(length - 2) + ' 部')

#防止因意外造成的閃退
try:
    for i in range(2, length):
        #找到三個點
        commit = driver.find_elements_by_xpath('//*[@id=\'watch_feed\']/div/div/div/div/div/div[' + str(i) + ']/div/div/div[1]/div[1]/div[3]/div/i')
        commit[0].click()
        time.sleep(random.randint(0, 8) *0.1 + 0.5)

        #找到"隱藏貼文"選項
        commit = driver.find_element_by_xpath('//*[@id=\'content\']/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[4]')
        commit.click()
        time.sleep(random.randint(0, 5) *0.1 + 0.7)
    
        #滾動至下一個
        commit = driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div/div/div/div/div[' + str(i) + ']/div/div/div[3]/div')
        driver.execute_script('arguments[0].scrollIntoView();', commit)
        time.sleep(random.randint(0, 9) *0.1 + 0.9)

        count += 1
        print('已隱藏' + str(count) + '部')
        
finally:
    #按下三角形
    context = driver.find_element_by_css_selector('#pageLoginAnchor')
    context.click()
    time.sleep(1)

    #按下登出紐
    context = driver.find_element_by_css_selector('li[data-gt=\'{"ref":"async_menu","logout_menu_click":"menu_logout"}\']')
    context.click()
    time.sleep(1)

    #關閉瀏覽器全部標籤頁
    driver.quit()

print('完成\n')
system('pause')
