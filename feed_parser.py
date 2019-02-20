# 구글 뉴스 스크래핑하기
import feedparser
from urllib.parse import quote
from openpyxl import Workbook
import ssl
import smtplib
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders



base_url = "https://rss.joins.com/sonagi/"

xlsx = Workbook()
sheets = ["total", "business"]
element = ["날짜", "제목", "url", "기자"]
map = {sheets[0] : "joins_sonagi_total_list.xml", sheets[1] : "joins_sonagi_money_list.xml"}

ssl._create_default_https_context = ssl._create_unverified_context

def sender(recipients):

    body = '준희님, 크롤링 데이터 보내드립니다.\r수고하세요.'
    msg = MIMEMultipart()

    msg['Subject'] = '[수집완료] 크롤링데이터'
    msg['From'] = 'jhlee910609@gmail.com'
    msg['To'] = (', ').join(recipients.split(','))

    msg.attach(MIMEText(body,'plain'))

    file = "new_list.xlsx"
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(file, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jhlee910609@gmail.com', 'wnsgml337?')
    server.send_message(msg)
    server.quit()

for new_sheet_name in sheets:
    new_sheet = xlsx.create_sheet(new_sheet_name)
    new_sheet.append(element)
    news_list = feedparser.parse(base_url + map[new_sheet_name])
    for news in news_list["items"]:
        new_sheet.append([news['published'][:10], news["title"], '=HYPERLINK("{}", "{}")'.format(news["link"], news["link"], news["author"])])

file_name ='new_list.xlsx'
xlsx.save(file_name)
# sender("jhlee910609@naver.com")











