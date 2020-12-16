# @ Author: Suowei Hu
# @ Date: 2020.12.16
# @ Comment: demo

import sys                                              # 加载编码格式，命令行入参
import time                                             # 设置强制延迟
from bs4 import BeautifulSoup                           # 网页解析
from selenium import webdriver                          # Chrome浏览器驱动
from selenium.webdriver.common.keys import Keys         # 键盘输入/快渐渐输入
from selenium.webdriver.chrome.options import Options   # 浏览器设置（设置无洁面浏览器，不加载图片）
# from selenium.webdriver.phantomjs.options import Options  # PhantomJS自动化无界面浏览器

LOGIN_INFO={
    'act' : '13735502141',
    'pad' : 'husuowei200029'
}
URL_DICT={                                          
    "login": "https://music.163.com/",              # Example URLS
    "user" : "https://music.163.com/#/user/home",   # https://music.163.com/#/user/home?id=505508015
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
FILE_PATH={
    "user"      : "src/demo_11/user/",
    "playlist" : "src/demo_11/playlist/",
    "song"     : "src/demo_11/song/"
}
def tryOut_templateUserPage_():
    # ========== 
    # Note this is a demo function hence lots redundance functions will be kept 
    # ==========

    # url = 'https://music.163.com/#/playlist?id=5375119825'
    # url = 'https://music.163.com/#/user/home?id=505508015'
    # url = 'http://www.jsphp.net/python/show-24-270-1.html'
    # __userAgent__   = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    # __referer__     = 'https://music.163.com/'
    # __header__ = Header(__userAgent__, __referer__)

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

def driver_factory(headless = False):
    if(headless):
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(executable_path = DEP_PATH['webdriver']['chrome'])
        return driver 
    else:
        driver = webdriver.Chrome(executable_path = DEP_PATH['webdriver']['chrome'])
        return driver

def scroll(driver, repeat = 5):
    for i in range(1, repeat):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)

def perf_login():
    base_url = URL_DICT["login"]
    __driver__.get(base_url)
    __driver__.implicitly_wait(10)
    __driver__.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/a').click()         # 单击登录按钮
    __driver__.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[2]/div/div[3]").click()                      # 单击其他登录方式
    __driver__.find_element_by_id('j-official-terms').click()       # 单击用户条款
    # __driver__.switch_to.frame("g_iframe")                        # 进入内联标签
    __driver__.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div[1]/div[2]/a').click()          # 单击手机登录
    input_account = __driver__.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div/input')    # 单击用户名框
    input_password = __driver__.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[2]/input')           # 单击密码框
    input_account.send_keys(LOGIN_INFO['act'])                      # 输入用户名
    input_password.send_keys(LOGIN_INFO['pad'])                     # 输入密码
    __driver__.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]/div[5]/a").click()                        # 单击登陆
    # __driver__.page_source                                        # 获得登陆后网页源码 
    # __driver__.close()                 # 关闭登录页面 (经过测试关闭之后SessionID就会失效)

def craw_userPage(id=505508015):
    f_path = FILE_PATH['user']
    # 发起请求URL
    base_url = URL_DICT['user']
    get_query = "?id=" + str(id) 
    render_url = base_url + get_query
    # 发起请求
    __driver__.get(render_url)          # WebDriver平台打开URL
    __driver__.implicitly_wait(5)       # 隐样等待加载，最多五秒
    # scroll(__driver__)                  # 滚动到底部（AJAX动态加载）
    __driver__.switch_to.frame("g_iframe")      # 切换到搜索结果的内联标签
    # __driver__.save_screenshot(f_path+"z.png") # 截图（方便DEBUG查看网页是否加载完）
    response = __driver__.page_source   # 得到浏览器渲染好的HTML网页
    # __driver__.close()                  # 关闭当前网页
    with open(f_path+'temp.html','w+') as f:
        f.write(response)
    return response

def craw_playlistPage(id=2867860282):
    f_path = FILE_PATH['playlist']
    # 发起请求URL
    base_url = URL_DICT['playlist']
    get_query = "?id=" + str(id) 
    render_url = base_url + get_query
    # 发起请求
    __driver__.get(render_url)          # WebDriver平台打开URL
    __driver__.implicitly_wait(5)       # 隐样等待加载，最多五秒
    # scroll(__driver__)                  # 滚动到底部（AJAX动态加载）
    __driver__.switch_to.frame("g_iframe")      # 切换到搜索结果的内联标签
    # __driver__.save_screenshot(f_path+"z.png") # 截图（方便DEBUG查看网页是否加载完）
    response = __driver__.page_source   # 得到浏览器渲染好的HTML网页
    # __driver__.close()                  # 关闭当前网页
    with open(f_path+'temp.html','w+') as f:
        f.write(response)
    return response

def craw_songPage(id=1445299059):
    f_path = FILE_PATH['song']
    # 发起请求URL
    base_url = URL_DICT['song']
    get_query = "?id=" + str(id) 
    render_url = base_url + get_query
    # 发起请求
    __driver__.get(render_url)          # WebDriver平台打开URL
    __driver__.implicitly_wait(5)       # 隐样等待加载，最多五秒
    # scroll(__driver__)                  # 滚动到底部（AJAX动态加载）
    __driver__.switch_to.frame("g_iframe")      # 切换到搜索结果的内联标签
    # __driver__.save_screenshot(f_path+"z.png") # 截图（方便DEBUG查看网页是否加载完）
    response = __driver__.page_source   # 得到浏览器渲染好的HTML网页
    # __driver__.close()                  # 关闭当前网页
    with open(f_path+'temp.html','w+') as f:
        f.write(response)
    return response

def parse_songPage():
    result_dict 

def main():
    perf_login()
    craw_userPage()
    craw_playlistPage()
    craw_songPage()
    __driver__.quit()

if __name__ == '__main__':
    __driver__ = driver_factory(headless = False)
    main()