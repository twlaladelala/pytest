import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

Host = 'smtp.163.com'
USER = '18318055277@163.com'
PASS = '邮件授权码'


# 下载文件
def download_picture(path, url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(url)
    with  open(f'{path}{filename}', 'wb') as file:
        file.write(resp.content)


def send_email(form_user, to_user, subject='', content='', filenames=[]):
    # 发送邮件
    email = MIMEMultipart()
    email['From'] = form_user
    email['To'] = ';'.join(to_user)
    email['Subject'] = subject

    message = MIMEText(content, 'plain', 'utf-8')
    email.attach(message)
    for filename in filenames:
        with open(filename, 'rb') as file:
            pos = filename.rfind('/')
            display_filename = filename[pos + 1:] if pos >= 0 else filename
            display_filename = quote(display_filename)
            attachment = MIMEText(file.read(), 'base64', 'utf-8')
            attachment['content-type'] = 'application/octet-stream'
            attachment['content-disposition'] = f'attachment; filename ="{display_filename}"'
            email.attach(attachment)

    smtp = smtplib.SMTP_SSL(Host)
    smtp.login(USER, PASS)
    smtp.sendmail(form_user, to_user, email.as_string())
