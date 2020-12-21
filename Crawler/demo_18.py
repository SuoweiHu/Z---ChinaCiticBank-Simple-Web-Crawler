from lxml import etree

a = '''
<body>
    <h><a href='www.biaoti.com'>head<div>HELLO</div></a></h>
    <p>段落1</p>
    <p>段落2</p>
</body>
'''


html = etree.HTML(a)
html.xpath('//h') # [<Element h at 0x2122e64e4c8>]

# 用//text() 提取标签内容
# 如果用该方法提取字段，方法会递归的找到所有子节点/孙节点/曾孙节点的内容
html.xpath('//h//text()') # ['head','HELLO']

# /text()和//text()的区别在于不可以提取孙节点的内容
# 如果用该方法提取字段，仅仅子节点的内容会被返回
html.xpath('//h/a/text()') # ['head']

# xpath语法默认提取全部
html.xpath('//p/text()') # ['段落1', '段落2']
html.xpath('//p[1]/text()') # ['段落1']
html.xpath('//body//text()') # ['\n    ', 'head', '\n    ', '段落1', '\n    ', '段落2', '\n']

# # 提取标签属性
html.xpath('//h/a/@href') # ['www.biaoti.com']


a = '''<title>标题</title>
<body>
    <ul class='list1'>
        <li>列表1第1项</li>
        <li>列表1第2项</li>
    </ul>
    <p class='first'>文字1</p>
    <p class='second'>文字2</p>
    <ul class='list2'>
        <li>列表2第1项</li>
        <li>列表2第2项</li>
    </ul>
</body>'''

html = etree.HTML(a)
html.xpath('//ul[2]/li/text()') # 在xpath语句中使用索引，限制只在第二个ul中寻找
html.xpath('//ul/li[1]/text()') # 在每个ul中取第一个li
# ['列表2第1项', '列表2第2项']

html.xpath('//ul[last()]/li/text()')       # 取最后一个 (注意：这里用[-1]返回的为空)
html.xpath('//ul[last()-1]/li/text()')     # 倒数第二个 (注意：这里用[-2]返回的为空)
html.xpath('//ul[position()<3]/li/text()') # 前两个    (注意：这里用[0:1]会抛出错误)


def main():
    return

if __name__ == '__main__':
    main()
