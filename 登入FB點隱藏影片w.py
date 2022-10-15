##測試完成
##介面完成

##自動化登入取首兩篇文章並登出關閉
##貼文訊息結構難分析
##欲擷取更多文章(第三篇以上)的話會有障礙
##因為臉書的網站架構是把第三篇以後(記得是五篇)的通通集合打包
##多層次和亂碼的 id，導致定位困難


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from os import system
import stdiomask, random
from time import time, sleep, localtime, ctime
import sys
import traceback

#設定視窗尺寸
system("mode con cols=58 lines=20")

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
#options.add_argument('headless')

def curTime():
    h = str(localtime(time()).tm_hour) if len(str(localtime(time()).tm_hour)) == 2 else '0' + str(localtime(time()).tm_hour)
    m = str(localtime(time()).tm_min) if len(str(localtime(time()).tm_min)) == 2 else '0' + str(localtime(time()).tm_min)
    s = str(localtime(time()).tm_sec) if len(str(localtime(time()).tm_sec)) == 2 else '0' + str(localtime(time()).tm_sec)
    t = h + ':' + m + ':' + s
    
    return t

print(curTime())

while True:  
    for j in range(5):
        # 啟動selenium 務必確認driver 檔案跟python 檔案要在同個資料夾中
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
        #driver = webdriver.Chrome(options = options)
        driver.get(site)
        sleep(1.5)

        #輸入email 
        context = driver.find_element_by_css_selector('#email')
        context.send_keys(account) 
        sleep(0.5)

        #輸入password
        context = driver.find_element_by_css_selector('#pass')
        context.send_keys(password)
        sleep(0.5)

        #按下登入紐
        #因為臉書有兩種登入頁面
        try:
            commit = driver.find_element_by_css_selector('#loginbutton')
        except:
            commit = driver.find_element_by_css_selector('button[data-testid =\'royal_login_button\']')

        commit.click()
        sleep(1)

        #點選watch
        driver.get('https://www.facebook.com/watch/')
        sleep(3)

        #給予隨機數作目標
        length = random.randint(20, 55) + 2     

        while True:
            count = 0
            #防止因意外造成的閃退
            try:
                print('隱藏 ' + str(length - 2) + ' 部')
                sleep(2.8)
        
                for i in range(2, length):
                    #找到三個點
                    commit = driver.find_elements_by_xpath('//*[@id=\'watch_feed\']/div/div/div/div/div/div[' + str(i) + ']/div/div/div[1]/div[1]/div[3]/div/i')
                    commit[0].click()
                    sleep(random.randint(0, 8) *0.1 + 1.2)

                    #找到"隱藏貼文"選項
                    commit = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[4]')
                    commit.click()
                    sleep(random.randint(0, 5) *0.1 + 1.3)
        
                    #滾動至下一個
                    commit = driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div/div/div/div/div[' + str(i) + ']/div/div/div[3]/div')
                    driver.execute_script('arguments[0].scrollIntoView();', commit)
                    sleep(random.randint(0, 9) *0.1 + 2)

                    count += 1
                    print( curTime() + ' 已隱藏 ' + str(count) + ' 部')              
                break

            except IndexError:
                print('挖到底啦~重新刷新網頁~')
                driver.refresh()
                length -= count
                if length < 0:
                    length *= -1
                sleep(4)
                continue
            
            except :
                print('發生意外狀況~\n')
                traceback.print_exc()
                print('\n重新刷新網頁~')
                driver.refresh()
                length -= count
                if length < 0:
                    length *= -1
                sleep(4)
                continue
                
        #按下三角形
        context = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div')
        context.click()
        sleep(3)

        #按下登出紐
        context = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]')
        context.click()
        sleep(2)

        #關閉瀏覽器全部標籤頁
        driver.quit()

        #隨時間重複
        nexttime = random.randint(10, 60)
        print(' - ' + curTime() + ' 等待第 ' + str(j+2) + ' 輪 ' + str(nexttime) + ' 分鐘')
        nexttime = nexttime *60
        nexttimeW = nexttime/100*2
        size = 50
        long = '\r[%-' + str(size - 1) + 's] %d%% '
        size += 1
        for i in range(size):
            sleep(nexttimeW)
            sys.stdout.write(long % ('='* i, i* 2))
            sys.stdout.flush()     

    #隨時間重新登入
    nextlogin = random.randint(8, 15)
    print('\n -- ' + curTime() + ' 等待下次重登 ' + str(nextlogin) + ' 小時')
    nextlogin = nextlogin *60*60
    nextloginW = nextlogin/100*2
    size = 50
    long = '\r[%-' + str(size - 1) + 's] %d%% '
    size += 1
    for i in range(size):
        sleep(nextloginW)
        sys.stdout.write(long % ('#'* i, i* 2))
        sys.stdout.flush() 
    
print('完成\n')
system('pause')
