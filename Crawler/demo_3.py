import requests
r = requests.get('https://zhuanlan.zhihu.com/python-programming')
print(r.text)
print(r.content)