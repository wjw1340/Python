import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

url = 'http://202.114.242.231:8036/default.html'
pattern = r'title=【考试安排】.*?职业生涯.*?>'
#[补|缓|补缓]考
r = requests.get(url)
r.encoding = 'ANSI'
data = r.text
with open('jwc.txt','w') as f:
	f.write(data)
res = re.findall(pattern,data)
if len(res) > 0:
    from_addr = '873138975@qq.com'
    password = 'qkduqvrhcduvbgaa'
    to_addr =  '873138975@qq.com'
    smtp_server = 'smtp.qq.com'

    topic = '职业生涯规划补考时间'
    content = '职业生涯考试时间出来了\nhttp://202.114.242.231:8036/default.html'   

    msg = MIMEText(content, 'plain', 'utf-8')                                    
    msg['From'] =  from_addr
    msg['To'] = to_addr
    msg['Subject'] = topic

    server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议端口
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    print('OK')
    server.quit()
else:
    exit()
