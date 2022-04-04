import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText

email = MIMEMultipart()
email["Subject"] = Header("离职证明文件，请查收", 'utf-8')  # 标题
email["From"] = Header("深圳某某某科技有限公司")  # 发件人
email["To"] = Header("1456315032@qq.com", 'utf-8')  # 收件人
# 正文内容
content = (""" 乌克兰战争的局势最近迎来了重大变化。3月29日，俄罗斯国防部副部长亚历山大•福明表示，'
    '俄罗斯国防部决定从根本上减少基辅和切尔尼戈夫方向的作战行动。随后几天，基辅附近俄军部队开始有组织地向俄罗斯和白俄罗斯境内进行撤退：3月31日，'
    '无人机侦察显示俄军已经撤出了基辅市西北仅18英里的安东诺夫机场；同一天，乌克兰国家切尔诺贝利核事故隔离区管理局通过社交媒体表示，俄军已全部撤出切尔诺贝利隔离区；'
    '4月2日乌克兰宣布，已收复了基辅周边伊尔平、布查、戈斯托梅利等30多个城镇，整个基辅地区，已从俄军手中获得“解放”。乌克兰收复基辅　乌克兰收复基辅""")
email.attach(MIMEText(content, 'plain', 'utf-8'))

# 发送附件
with open('table/工作簿1.xls', 'rb') as file:
    attachment = MIMEText(file.read(), 'base64', 'utf-8')
    attachment['content-type'] = 'application/octet-stream'
    attachment['content-disposition'] = "attachment; filename='aaa.xls"
    email.attach(attachment)

# 创建链接对象 ssl 安全的链接
smtp_obj = smtplib.SMTP_SSL('smtp.163.com')
# smtp_obj.connect('smtp.163.com',456)
# 登录邮箱账号 授权码
smtp_obj.login('18318055277@163.com', '邮箱授权码')
# 发送邮件
smtp_obj.sendmail('18318055277@163.com', ['1456315032@qq.com'], email.as_string())
