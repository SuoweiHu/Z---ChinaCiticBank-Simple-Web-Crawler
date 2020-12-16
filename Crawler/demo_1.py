import urllib
import urllib2

# 若使用 POST 方法（网址上不会显示参数）
values = {
    "user_name" : "suowei_hu",
    "password" : "my_password"
}
data = urllib.urlencode(values)
request = urllib2.Request("http://passport.csdn.net/account/login",data)
response = urllib2.urlopen(request)
print response.read()


# 若使用 GET 方法（参数直接先是在地址链接上）
values = {
    "user_name" : "suowei_hu",
    "password" : "my_password"
}
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
url_get = url + "?" + data
request = urllib2.Request(url_get)
response = urllib2.urlopen(request)
print response.read()


# 设置一些 Headers 的属性来模拟浏览器的操作
# （有些网站不会同意程序直接用上面的方式进行访问，如果识别有问题，就不会响应）
headers = { 
    "User-Agent" : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", #浏览器相关的属性
    "Referer" : "http://www.zhihu.com/article" #从哪个网页链接过来的
} 
values = {
    "user_name" : "suowei_hu",
    "password" : "my_password"
}
data = urllib.urlencode(values)  
url = 'http://www.server.com/login'
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read()


#代理设置
# （有些网站通过统计同一个 IP 的访问次数，并禁止一段时间内访问次数过多的 IP，代理就可以一段时间换一个 IP）
enable_proxy = True
proxy_handler = urllib2.ProxyHandler(
    {"http" : "http://some-proxy-0.com:8080",
    "http" : "http://some-proxy-1.com:8080",
    "http" : "http://some-proxy-2.com:8080"}
)
null_proxy_handler = urllib2.ProxyHandler({})
if (enable_proxy): opener = urllib2.build_opener(proxy_handler)
else: opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
values = {
    "user_name" : "suowei_hu",
    "password" : "my_password"
}
data = urllib.urlencode(values)
request = urllib2.Request("http://passport.csdn.net/account/login",data)
response = urllib2.urlopen(request)
print response.read()


#超时设置
#（为消除网站响应过慢造成的影响）
# 若需要传 Data
values = {
    "user_name" : "suowei_hu",
    "password" : "my_password"
}
data = urllib.urlencode(values)
request = urllib2.Request("http://passport.csdn.net/account/login",data, 10) # timeout = 10
response = urllib2.urlopen(request)
print response.read()
# 若不需要 Data
request = urllib2.Request("http://www.baidu.com")
response = urlib2.urlopen(request,timeout = 10)
print response.read()

# URLError 
# (原因： 服务器不存在，连接不到服务器)
try:
    requset = urllib2.Request('http://www.baidu.com')
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
    # 若连接不到会显示以下消息
    # [Errno 11004] getaddrinfo failed
