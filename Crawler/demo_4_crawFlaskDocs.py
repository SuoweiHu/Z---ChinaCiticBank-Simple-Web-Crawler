# WORKING DEMO
# 这个例子展示了最简单基础的的爬取 没有防爬（客户浏览器，Cookie，防盗链等）
# 的网站的HTML文件并保存

import requests 
import sys

reload(sys)
sys.setdefaultencoding("utf8")

url = "https://pythonhosted.org/Flask-Bootstrap/"

r = requests.get(url)
out = r.content
print(out)

f = open("result.html",'w+')
f.write(out)
f.close()
