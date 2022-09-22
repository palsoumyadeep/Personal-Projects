from bs4 import BeautifulSoup
import requests

# for sending email
import smtplib

# for email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# for system date and time manipulation
import datetime
now = datetime.datetime.now()

def extract_content(url):
    print('Extracting data from website')
    cnt = ""
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for tag in soup.find_all('tr', attrs={"class": "athing"}):
        cnt += (tag.text+"\n"+'<br>')

    return cnt


content = ''
content += extract_content('https://news.ycombinator.com/')
content += '<br>---------<br>'
content += '<br><br>End of Message'


# email authentication
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'jeetpal.125@gmail.com' # company email
TO = 'palda074@gmail.com' # can be a single receiver or a python list
PASS = 'jmeljclrvrcaknvu'  # enter app specific password gmail password won't work

# CREATING MESSAGE FOR EMAIL
msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]'+ str(now.day)+'-'+ str(now.month)+'-' + str(now.year)
# for dynamic subject
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))


print('Initiating Server')
server = smtplib.SMTP(SERVER, PORT)

server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')
server.quit()
