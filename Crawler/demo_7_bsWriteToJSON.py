# WORKING DEMO

import requests         
from bs4 import BeautifulSoup 
# import sys
# import pprint         # For pretty printing (formatting but have encoding problems)
import json             # For exporting options (save as json file)

# reload(sys)               
# sys.setdefaultencoding("utf8")

url = 'https://www.zhihu.com/'
head_cookie = '_zap=4fe3b27d-0c36-4219-b3fe-234f411eeefe; d_c0="AMAerlbRHRGPTlCTgWCVGJsRKXe0eRiEDLw=|1586838810"; _ga=GA1.2.1102621494.1586838813; q_c1=fdc1b1a971ff4c68854c9601c0cf6633|1603637525000|1588652844000; tst=r; z_c0="2|1:0|10:1605327999|4:z_c0|92:Mi4xb0Z2VEF3QUFBQUFBd0I2dVZ0RWRFU1lBQUFCZ0FsVk5mNnFjWUFEWW5rbkhfczF2Z05oWEVsejd6dXdRdlYxS2d3|a83edfe6d3e2368d4af480269d9ddd45a73943418040cd5c991d68dde6597ce1"; _xsrf=VhzkxVXbgtbhWmYyh8PnjH0NqIxqo1AE; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1606636239,1607567158,1607652483,1607995090; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1607995090; SESSIONID=YPlwchIqXdxWh15rtCHg4w8iEMmWnia98KapCfUaVj2; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1607995091|1607995081; JOID=VFEUBUKVlnN5Ca0eEZVG7NxXN2AHw84YAWXKX2fC_QMpbpMka0GXoyYJqhEZxHIVUO7b00C-AH7ZfIDqkT9rk5g=; osd=UVgdC0iQn3p3A6gXGJtM6dVeOWoCyscWC2DDVmnI-AogYJkhYkiZqSMAox8TwXscXuTe2kmwCnvQdY7glDZinZI='
head_referer = 'https://www.zhihu.com/'
head_userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
header = {"user-agent":head_userAgent, "referer":head_referer, "cookie":head_cookie}
data = {}

r = requests.get(url, data=data, headers=header)    
content = r.content.decode("utf-8")
soup = BeautifulSoup(content,'html.parser')
cells = soup.find_all('div', class_="Card TopstoryItem TopstoryItem--old TopstoryItem-isRecommend")
print("# Status code: " + str(r.status_code))

# Read existing file
result_list = []
with open('src/demo_7/result.json', encoding = 'utf-8') as f:
    s = f.read()
    result_list = json.loads(s)

# Add records
for cell in cells:
    text_ansTitle = cell.find('h2').text
    text_ansBriefing = cell.find('span',class_="RichText ztext CopyrightRichText-richText").text
    text_votingUp = cell.find('button', class_="Button VoteButton VoteButton--up")["aria-label"]
    text_votingDown = cell.find('button', class_="Button VoteButton VoteButton--down")['aria-label']

    temp_result = {
        "title" : str(text_ansTitle),
        "brief" : str(text_ansBriefing),
        "voting": str(text_votingUp)[2:]
    }
    result_list.append(temp_result)

# Write to file
s = json.dumps(result_list, indent=4, ensure_ascii=False)
with open('src/demo_7/result.json', 'w+', encoding = 'utf-8') as f:
    f.write(s)
