import sys                      # 更改编码UTF8
# import time                   # 强制等待加载
import requests                 # 请求网页
import json                     # 保存为JSON
# import pandas as pd           # 如果用DataFrame
import xlsxwriter               # 如果用XlsxWriter
from bs4 import BeautifulSoup   # 解析网页
# import lxml                   # LXML Parser

PATH = 'src/demo_14'
URL_BASE = 'http://www.ajztb.com'
URL_SDIR = 'jyxx'
URL_FILE = 'moreinfo.html'

def save_toJson(text, path):
    s = json.dumps(text, indent=4, ensure_ascii=False)
    with open(path, "w+") as f:
        f.write(s)
        f.close()
    f.close()
def save_toExcel(text,path):
    with xlsxwriter.Workbook(path) as workbook:
        worksheet = workbook.add_worksheet()
        for row_num, data in enumerate(text):
            worksheet.write_row(row_num, 0, data)


def gen_url(pageIndex, categoryNum = '003002',subCategoryNum=''):
    # Ease for later modification
    queries = {
        'categoryNum' : str(categoryNum),
        'pageIndex'   :str(pageIndex)
    }
    
    # Generate query sub string 
    query_str = ""
    for item in queries.items():
        query_str += item[0] + '=' + item[1] + '&'
    query_str = query_str[:-1]

    # Render for the final URL
    url = URL_BASE + '/' + URL_SDIR + '/' + URL_FILE + '?' + query_str
    print(url)
    return url
     
def craw_page(url, header_ = {}, data_ = {}):
    response = requests.get(url, headers=header_, data=data_)
    return response.content.decode('utf-8')
    
def parse_mainPage(page_source, recursive, parser='html.parser'):
    soup = BeautifulSoup(page_source, parser)
    content_container = soup.find('div', class_='ewb-list-main')                # Wrapper for the category page
    posts_container   = content_container.find('ul',class_='ewb-notice-items')  # Unordered list  
    posts = posts_container.find_all('li')                                      # List of related items 
    result_list = []
    for post in posts:
        title = post.find('a').text
        rel_link = post.find('a')['href']
        link = URL_BASE + rel_link
        date = post.find('span',class_='r ewb-notice-date').text
        # print("#"*100)
        # print("DEBUG - title: \n\t" + title)     
        # print("DEBUG - link: \n\t" + link)
        # print("DEBUG - date: \n\t" + date)
        temp_result = {'title':title,'link':link, 'date':date}

        if(recursive):                                  # 是否爬取二级网页的内容
            url_secondary = temp_result['link']                 # 二级页面链接
            res_secondary = craw_page(url_secondary)            # 响应内容
            result_secondary = parse_detailPage(res_secondary)  # 解析找到字段
        else:
            result_secondary={}
        temp_result['detail'] = str(result_secondary).replace('\n','')

        # print(temp_result)
        result_list.append(temp_result)
    return result_list

def parse_detailPage(page_source, parser='html.parser'):
    soup = BeautifulSoup(page_source, parser)
    detail_container = soup.find('div',class_='detail-body')
    # TODO :YET TO BE IMPLMENTED
    return detail_container.text

def parse_noticePage(page_source, parser='html.parser'):
    soup = BeautifulSoup(page_source, parser)
    notice_container = soup.find('div', class_='ewb-notice-bd')
    posts_container  = notice_container.find_all('ul')[0]
    news_container   = notice_container.find_all('ul')[1]
    
    result_list = []

    # 公告
    posts = posts_container.find_all('li')
    for post in posts:
        title = post.text
        title = title.replace('\n','')
        link = URL_BASE + post.a['href']
        time = post.span.text
        time = time.replace('\n','')
        time = time.replace(' ','')
        # print(title, link, time)
        result = [time, title, link]
        result_list.append(result)
        
    # 新闻
    news = news_container.find_al('li',class_='ewb-notice-items')[1]
    print(news)

    return result_list

def retrivePagesJyxx(cat_num,pg_from,pg_to,pg_step,recursive=False):
    result_list = []
    for pg_num in range(pg_from, pg_to+1):
        pg_url   = gen_url(pg_num*pg_step,cat_num)      # 生成URL资源链接
        response = craw_page(pg_url)                    # 使用REQUESTS请求获得网页HTML资源
        result   = parse_mainPage(response,recursive)   # 解析网页获得字典列表
        result_list = result_list + result  #(this ensure most recent pages comes first)
    return result_list


    print(news_container.text)

def retriveNoticeJyxx():
    url = 'http://www.ajztb.com/'
    response = craw_page(url)
    parsed_notice = parse_noticePage(response)
    # print(parsed_notice)
    return parsed_notice

def main():
    url = 'http://www.ajztb.com/'
    temp = craw_page(url)
    # print(temp)

    # ============== 爬公告 =================
    # result = retriveNoticeJyxx()
    # result = [['日期','信息','链接']]+result 
    # save_toExcel(result,PATH+'/result.xlsx')
    # ======================================

    # ============== 爬多页 =================
    result = {'count' : 0}
    result['data'] = retrivePagesJyxx(__categoryNum__,__pageFrom__,__pageTo__,__pageStep__,__recursive__)
    result['count'] = len(result['data'])
    save_toJson(result,PATH+'/result.json')
    temp = result["data"]
    text = []
    for item in temp:
        item = item.values()
        text.append(item)
    # print(text)
    text = [["标题",'链接','发布时间','详情 (未完成)']] +  text
    save_toExcel(text,PATH+'/result.xlsx')
    # ======================================


if __name__ == "__main__":
    # 建设工程 003001
    # 政府采购 003002 ...
    __categoryNum__ = '003001' 

    # 页面范围
    __pageFrom__    = 1
    __pageTo__      = 10 #(inclusive)
    __pageStep__    = 1
    
    # 是否要爬二级页面
    __recursive__   = False
    main()