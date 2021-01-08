import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

def SendMail(report_filepath,log_filepath,filename1):

    my_sender = '1984370982@qq.com'  # 发件人邮箱账号
    my_pass = 'oveaopypjxsyfafj'  # 发件人邮箱密码
    my_user = 'ysun_zufe@163.com'  # 收件人邮箱账号，我这边发送给自己

    msg = MIMEMultipart()
    msg['From'] = formataddr(["FromTest", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = Header(filename1+"测试报告", 'utf-8')  # 邮件的主题，也可以说是标题

    msg.attach(MIMEText('\n\n\n附件是'+filename1+'测试报告', 'plain', 'utf-8'))

    att1 = MIMEText(open(report_filepath, 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="test_report.html"'
    msg.attach(att1)
    att2 = MIMEText(open(log_filepath, 'rb').read(), 'base64', 'utf-8')
    att2['Content-Type'] = 'application/octet-stream'
    att2['Content-Disposition'] = 'attachment; filename="test_log.log"'
    msg.attach(att2)
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
