# WORKING DEMO

# 这个例子展示了爬取 设有防爬（客户浏览器，Cookie，防盗链等）
# 的网站的HTML文件，使用设置 user-agent, referer, cookie

import requests 
import sys

reload(sys)
sys.setdefaultencoding("utf8")

DEMO_GET_WITH_HEADER = True
DEMO_GET_WITH_COOKIE = True

url = 'https://www.zhihu.com/'
head_cookie = '_zap=4fe3b27d-0c36-4219-b3fe-234f411eeefe; d_c0="AMAerlbRHRGPTlCTgWCVGJsRKXe0eRiEDLw=|1586838810"; _ga=GA1.2.1102621494.1586838813; q_c1=fdc1b1a971ff4c68854c9601c0cf6633|1603637525000|1588652844000; tst=r; z_c0="2|1:0|10:1605327999|4:z_c0|92:Mi4xb0Z2VEF3QUFBQUFBd0I2dVZ0RWRFU1lBQUFCZ0FsVk5mNnFjWUFEWW5rbkhfczF2Z05oWEVsejd6dXdRdlYxS2d3|a83edfe6d3e2368d4af480269d9ddd45a73943418040cd5c991d68dde6597ce1"; _xsrf=VhzkxVXbgtbhWmYyh8PnjH0NqIxqo1AE; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1606636239,1607567158,1607652483,1607995090; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1607995090; SESSIONID=YPlwchIqXdxWh15rtCHg4w8iEMmWnia98KapCfUaVj2; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1607995091|1607995081; JOID=VFEUBUKVlnN5Ca0eEZVG7NxXN2AHw84YAWXKX2fC_QMpbpMka0GXoyYJqhEZxHIVUO7b00C-AH7ZfIDqkT9rk5g=; osd=UVgdC0iQn3p3A6gXGJtM6dVeOWoCyscWC2DDVmnI-AogYJkhYkiZqSMAox8TwXscXuTe2kmwCnvQdY7glDZinZI='
head_referer = 'https://www.zhihu.com/'
head_userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
header_withCookie = {"user-agent":head_userAgent, "referer":head_referer, "cookie":head_cookie}
header_withOutCookie = {"user-agent":head_userAgent, "referer":head_referer}
data = {}

if(DEMO_GET_WITH_HEADER):
    if(DEMO_GET_WITH_COOKIE):
        # Request with header (user-agent, referer, cookie) 
       r = requests.get(url, data=data, headers=header_withCookie) 
    else:
        # Request with header (user-agent, referer, cookie) 
       r = requests.get(url, data=data, headers=header_withOutCookie) 
else:
    # Request without header 
    r = requests.get(url, data=data)                    

print("# Status code: " + str(r.status_code))
f = open("result.html", "w+")
f.write(r.content.encode('utf-8'))
print("# Result saved to result.html")



