"""
=======================================================
=========================
html tag / class  (tieba)
=========================
outer box 容器
div class_ = "t_con cleafix"
-
left column: replies  回复数
span class_ = "threadlist_rep_num center_text"
-
right column: title 标题/ 二级页面链接
a j_th_tit 
-
right column: author 作者
a class_ = "frs-author-name j_user_card"
-
right column: time 创建时间
span class_ = "pull-right is_show_create_time"
-
bottom: one line 简介
div class_="threadlist_abs threadlist_abs_onlyline "
=========================
html tag / class (topic)
=====≠===================
CONTAINER div,class_="l_post l_post_bright j_l_post clearfix  "
AUTHOR_CONTAINER CONTAINER('div')[0]
CONTENT_CONTAINER CONTAINER('div')[1]
AUTHOR AUTHOR_CONTAINER.div.div['author']
CONTENT CONTENT_CONTAINER.div.cc('div')[1]


=====≠===================
Path 
=========================
"https://tieba.baidu.com/f?kw=塞博朋克2077"
"https://tieba.baidu.com"
"https://tieba.baidu.com/f?kw=%E8%B5%9B%E5%8D%9A%E6%9C%8B%E5%85%8B2077&ie=utf-8&pn="
=======================================================
"""

import requests
from bs4 import BeautifulSoup 
import json 

# Craw Page Function
def crawTiebaPage(tieba='图', page_number = 1, page_factor = 50, header={}, data={}):
    # 百度贴吧是使用构造URL的因此使用此方法
    base_url = "https://tieba.baidu.com/f?"
    encode_quuery   = "ie=utf-8"
    tieba_query     = "kw=" + tieba
    page_query      = "pn=" + str(page_number * page_factor)
    rendered_url = base_url + encode_quuery + "&" + tieba_query + "&" + page_query

    # response = requests.get(rendered_url, data=data, headers=header) # Request with header 
    response = requests.get(rendered_url)                   # 发现用Cookie请求会导致部分看过的帖子被注释
    if(DEBUG): print("# Request with header has been sent")
    response_content = response.content.decode('utf-8')     # 获得渲染后的HTML文件 并用UTF-8编码格式进行解码
    if(DEBUG): print("# Response received")
    # print(response_content)

    # File I/O: Read initial data in JSON file
    result_dict = {}
    with open(PATH, encoding = 'utf-8') as f:
        s = f.read()
        result_dict = json.loads(s)
    result_dict.pop("meta")
    result_dict = {"meta":{"Record_count":0}} | (result_dict)

    # Process
    soup = BeautifulSoup(response_content, 'html.parser')   # 使用网页分析库 进行语义分析
    if DEBUG: print("# Processing the response with html parser")
    containers = soup.find_all('li', class_ = 'j_thread_list clearfix')
    for cont in containers:
        sections = cont.div('div')
        # Get unique id related data
        _tid_ = cont['data-tid']
        # Get detailed data
        l_sec    = sections[0]
        r_sec    = sections[1]
        _title_  = r_sec.div('div')[0].a.text
        _link_   = "https://tieba.baidu.com" + (r_sec.div('div')[0].a)['href']
        _author_ = ((r_sec.div('div')[1])('span')[0].span.a).text
        _time_   = ((r_sec.div('div')[1])('span')[3]).text
        _brief_  = (r_sec('div')[1]).text
            # # Debug printing
            # print(_tid_)
            # print(_title_)
            # print(_author_)
            # print(_link_)
            # print(_time_)
            # print(_brief_)
            # print("=="*13)
        if(SUB_PAGE): _posts_ = crawTopicPage(_link_)
        else: _posts_ = "Not crawed"

        # Store result as dict
        result = {
            "Title"         : _title_,
            "Author"        : _author_,
            "Link"          : _link_,
            "Last Update"   : _time_,
            "Oneline"       : _brief_,
            "Post"          : _posts_
        }
        result_dict[_tid_] = result
        

    # File I/O: Write new data to JSON file
    if DEBUG: print("# Saving the result to json file")
    result_dict['meta'] = {"Record_count":len(result_dict)}
    s = json.dumps(result_dict, indent=4, ensure_ascii=False)
    with open(PATH, 'w+', encoding = 'utf-8') as f:
        f.write(s)

    if DEBUG: print("# Program yields")
    return True

# Craw Topic Function
def crawTopicPage(url):
    topic_response= requests.get(url)
    topic_content = topic_response.content.decode("utf-8")

    # print(topic_content)

    topic_soup = BeautifulSoup(topic_content, 'html.parser')
    containers = topic_soup.find_all('div',class_="l_post l_post_bright j_l_post clearfix")
    topic_result_dict = {"meta":{"Post_count":0}}
    for container in containers:
        pid = container['data-pid']
        author_container = container('div')[0]
        content_container = container('div')[6]
        tail_container = container.find('div',class_="post-tail-wrap")
        author = (author_container.find_all('a'))[1].text
        if(len(content_container('div')) > 1): content = (content_container('div')[2].text)
        else: content = ""
        time = (tail_container('span',class_="tail-info")[-1].text)
        n_post = (tail_container('span',class_="tail-info")[-2].text)
        client = (tail_container('span',class_="tail-info")[-0].text)
        # print(pid)
        # print(author)
        # print(content)
        # print(time)
        # print(n_post)
        # print(client)
        # print("=" * 10)
        topic_result = {
            "Author" : author,
            "Comment": content,
            "#Post" : n_post,
            "TimeStamp": time,
            "Platform" : client
        }
        topic_result_dict[pid] = (topic_result)
        topic_result_dict['meta']['Post_count'] = len(topic_result_dict)
    
    return (topic_result_dict)

    


def main():
    # Header 
    head_cookie = 'BAIDUID=CDC9C6E19F270E84C790388294B98D2C:FG=1; PSTM=1587037202; BIDUPSID=B909F22E383C7C5D760C7F984866D47E; BDUSS=TAxQzVnVmwwcGM1OWN4WVg1TTNOWFFFUTZKV0NsNW1mMUVuaFBkR0M1TEpsMFJmRVFBQUFBJCQAAAAAAAAAAAEAAABJ1lYwSFNXxKrD-7O-1LUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMkKHV~JCh1fb; BDUSS_BFESS=TAxQzVnVmwwcGM1OWN4WVg1TTNOWFFFUTZKV0NsNW1mMUVuaFBkR0M1TEpsMFJmRVFBQUFBJCQAAAAAAAAAAAEAAABJ1lYwSFNXxKrD-7O-1LUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMkKHV~JCh1fb; BAIDUID_BFESS=39D18F975506089CF0DD3AB2F245CA82:FG=1; delPer=0; PSINO=5; H_PS_PSSID=1461_33074_33121_33061_31254_33099_33100_32846_26350_33199_33237_33148_33266; ab_sr=1.0.0_YjViNjUyY2Q0NzEzYzYzZjNhY2MwNjVhY2U3MWVmMWM5YWJhMmNkOWI4OTkwNDRmOTc4MWZiNGExM2I4ZDk0MTJkOGRhY2I3MWEwOGE0YWEzMWM0MjJiZGM2OGZhNzQzMjAxZTg4YTNhNzkyYTgyNTY4ODlhNGRmNzFmMTliOTA='
    head_referer = 'https://www.baidu.com/'
    head_userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

    header = {"user-agent":head_userAgent, "referer":head_referer, "cookie":head_cookie}  

    # Data 
    data = {}

    # Iterate 
    page_upperBound = 1
    for page in range(0,page_upperBound):
        print("# ======== Crawling page " + str(page) + " of "+ str(page_upperBound) +" ========")
        crawTiebaPage(page_number=page)

if __name__ == '__main__':
    
    PATH = 'src/demo_9/result.json'
    DEBUG = False
    SUB_PAGE = True
    
    # arg_items = sys.argv
    # arg_length = len(num_argv)
    # # Argument list 
    # #   arg1 : tieba name
    # #   arg2 : number of pages
    # #   arg3 : user cookies

    main()




