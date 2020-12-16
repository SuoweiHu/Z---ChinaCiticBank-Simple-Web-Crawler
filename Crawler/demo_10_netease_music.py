import requests 
import sys
from bs4 import BeautifulSoup


def craw_site(url, header={}, data={}, cookie=""):
    header["cookie"] = cookie
    r_response = requests.get(url, headers=header, data=data)
    r_context = r_response.content.decode("utf-8")
    # r_context = r_response.text
    return r_context

class Header:
    data = {}
    def __init__(self, userAgent, referer, cookie='', accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'):
        self.data['user-agent'] = userAgent
        self.data['referer'] = cookie 
        self.data['cookie'] = referer
        self.data['accept'] = accept




def main():
    debug_headers = {
        "User-Agent"    : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Referer"       :  "https://music.163.com/"
    }
    # print(craw_site(url=url, header = __header__.data))
    print(craw_site(url=url, header = debug_headers))
    # print(craw_site(url=url, header = {})


if __name__ == '__main__':
    url             = 'http://music.163.com/user/home?id=505508015'
    # url             = 'http://music.163.com/playlist?id=759651972'
    # url             = 'https://y.music.163.com/m/user?id=505508015'
    # __userAgent__   = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
    __userAgent__   = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    __referer__     = 'https://music.163.com/'
    __cookie__      = 'JSESSIONID-WYYY=Q2YnFxemeuSkoQzbVssyytK5KT87kuzm%5CJmy5vadfJixFDPPyfkubSUQWou%2FxZJGlfAm5rWre8xHl4Qxaag2pzE3oiXMcEFmVEyDMcFX5s%2FPmVhIgmcnawYEdnuyMz3K%2BVvDkM2mSZ2bgpkKZHGzO4zDFXg6ZfMFKqvC02%5CIdq2hDQGZ%3A1608083120913; _iuqxldmzr_=32; _ntes_nnid=c3536432632ed8e9bc6acbb2746cb559,1608081320972; _ntes_nuid=c3536432632ed8e9bc6acbb2746cb559; NMTID=00Orp7roKWYKCdiMUSHnrviXNsaPmEAAAF2aR2shA; WEVNSM=1.0.0; WNMCID=yptxfr.1608081321212.01.0; WM_NI=5nj%2BqUzEg5ii4V3lWGIhz4lspj3GcTAhdx%2Fbjo%2Bdpc1javBEU6pJH4FY2CCVOvUYL38c4sWfrDNKL0GOgYcGxAJGzbjW3GFR3XcleQQ5Dj208%2BtCrwYr3UHfqVV%2FyqZlOVE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee98cf60f88aabb6eb74e9eb8fa2d15a868e9a85f16b9cee98b6aa6b8ef5fa95b52af0fea7c3b92af7b2a6ccf45fba9ba9d6ec63f88afd8dd64d8bb8b6d5ef79b4b6fda8e26083b8ac99ae6aaab1e585f369f3b6af97c14f97eac0abcb408687fea4c25e8daa9bbacf39fcbdfc94d66eb29c82accf3c8591a9bae24dbc9f86a8f96aaa89fda8c55af188ad8de85b93eb8c8bb13cfcf5bca4f17d9baefdb6cb6eb38a9ad0fc7b9ab481b7c837e2a3; WM_TID=%2Br19GmUlEbxABUEAFEIqLXzSE%2BaJ7u97'
    __header__ = Header(__userAgent__, __referer__, __cookie__)
    main()