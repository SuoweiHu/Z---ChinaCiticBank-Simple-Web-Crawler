import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# ========
# Mail utilities
PATH = 'src/demo_16'
HOST = {
    'server'    : 'smtp.163.com',
    'account'   : 'suowei_h_temp@163.com', #myTempMai willBeDeactivated
    'password'  : 'JUIFZIYOWSJFQYIG'       #husuowei200029
}
MAIL = {
    'sender'    : 'suowei_h_temp@163.com',
    'receivers' : ['suowei.h@icloud.com'],
    'title'     : 'TEST - 爬到新信息',
    'message'   : '爬到如下新信息:\n',
    'data'      : '\t xxxx, yyyyy, zzzz \n' * 10 
}

# =========
# Send mail
def sendEmail163(data=MAIL['data'],atts=['result.xlsx']):
    mail_host = HOST['server']                     # SMTP服务器(这里用的163)
    mail_user = HOST['account']                    # 用户名（这里用的临时邮箱，很可能会注销吊）
    mail_pass = HOST['password']                   # 授权码（密码hu****029）
    sender    = MAIL['sender']                     # 发件人邮箱
    receivers = MAIL['receivers']                  # 接收邮件列表
    title     = MAIL['title']                      # 邮件主题
    content   = MAIL['message'] + data             # 邮件内容

    message = MIMEMultipart()
    msg_con = MIMEText(content) 

    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    message.attach(msg_con)
    message["Accept-Language"]="zh-CN" # 设置消息为中文
    message["Accept-Charset"]="utf-8"  # 指定编码

    for att_name in atts:              # 添加附件
        file_type = 'excel'
        att1 = MIMEText(open(PATH + '/' + att_name, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename=' + att_name
        message.attach(att1)               
 
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)         # 登录验证 163 邮箱
        smtpObj.sendmail(sender, receivers, message.as_string())# 发送
        print("mail has been send successfully.")

    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    sendEmail163()