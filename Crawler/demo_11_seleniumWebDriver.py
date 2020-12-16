# @ Author: Suowei Hu
# @ Date: 2020.12.16
# @ Comment: demo

import sys                                              # 加载编码格式，命令行入参
import time                                             # 设置强制延迟
from selenium import webdriver                          # Chrome浏览器驱动
from selenium.webdriver.common.keys import Keys         # 键盘输入/快渐渐输入
from selenium.webdriver.chrome.options import Options   # 浏览器设置（设置无洁面浏览器，不加载图片）
# from selenium.webdriver.phantomjs.options import Options  # PhantomJS自动化无界面浏览器

URL_DICT={                                          # Example
    "user" : "https://music.163.com/#/home",        # https://music.163.com/#/user/home?id=505508015
    "playlist" : "https://music.163.com/#/playlist",# https://music.163.com/#/playlist?id=5375119825
    "song" : "https://music.163.com/#/song",        # https://music.163.com/#/song?id=1350330823

}

DEP_PATH={
    "webdriver" : 
    {
        "chrome"    : "chromedriver/87_0_4280_88",  # Chrome Version 87.0.4280.88 (Official Build) (x86_64)
        "phantomjs" : "phantomjs/bin/phantomjs"     # Phatomjs Version: ?
    }
}

PATH={
    "user-age"      : "src/demo_11/user",
    "playlist-page" : "src/demo_11/playlist",
    "song-page"     : "src/demo_11/song"
}



def craw_userPage():
    # ========== 
    # Note this is a demo function hence lots redundance functions will be kept 
    # ==========

    # options = Options()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path=DEP_PATH['webdriver']['chrome'])
    # driver = webdriver.PhantomJS(executable_path="phantomjs/bin/phantomjs")
    
    time.sleep(1)
    # driver.render("result.png")
    driver.get(url)
    driver.maximize_window()

    # time.sleep(seconds)                 # 强制等待：等同于C++的Yield()
    driver.implicitly_wait(3)           # 隐式等待：等待页面全部加载完就执行， 参数为最多等待时间
    # element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'su')))
                                        # 显式等待：显示等待是针对某一个元素进行相关等待判定, 一共等待 5 秒钟，每 0.5s 找一次，直到通过 ID 找到

    for i in range(1, 5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)

    driver.switch_to.frame("g_iframe") # 使用GET搜索之后跳转到了新的页面，所以必须要driver.switch_to.frame

    
    # iframe = driver.find_element_by_id('auto-id-LQKx0hR1U3P1Xp5r')
    # driver.switch_to.frame(iframe)

    driver.save_screenshot("result.png")
    print(driver.page_source)

    driver.close()
    driver.quit()


def craw_songPage(headless = False):
    if(headless):
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(executable_path = DEP_PATH['webdriver']['chrome'])
    



def main():
    craw_userPage()

if __name__ == '__main__':
    # url = 'https://music.163.com/#/playlist?id=5375119825'
    url = 'https://music.163.com/#/user/home?id=505508015'
    # url = 'http://www.jsphp.net/python/show-24-270-1.html'
    # __userAgent__   = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    # __referer__     = 'https://music.163.com/'
    # __header__ = Header(__userAgent__, __referer__)
    main()