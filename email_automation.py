import email.mime
import email.mime.multipart
import bs4
import requests
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

now = datetime.datetime.now()
content = ''
def extract_news(url):
    print('extracting data')
    cnt = ''
    cnt += '<b> hackernews newsletter </b>' + '<br>' + '-' *50 + '<br>'
    response = requests.get(url)
    content = response.content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign':''})):
        cnt += ((str(i+1)+' ) '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='More' else '')
    return cnt

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content +=('<br><br>End of Message')

print('composing email')
From = ''
To = ''
password = '*********'

msg = MIMEMultipart()
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = From
msg['To'] = To
msg.attach(MIMEText(content, 'html'))
print('initializing server')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo()
server.login(From, password)
server.sendmail(From, To, msg.as_string())
print('email sent')
server.quit( )

