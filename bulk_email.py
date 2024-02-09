import smtplib, ssl
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
import sys
import json

# Path to configuration file with login details
path_to_json = "details-example.json"
config = json.load(open(path_to_json))

email_username = config["Username"]
email_password = config["password"]
sig = config["sig"]

# These are the SMTP details for GMail, Other providers will be different.
smpt_address = "smtp.gmail.com"
smpt_port = 465

excel_data = pd.read_excel("data.xlsx")
data = pd.DataFrame(excel_data, columns=['email','link'])
total_rows = len(data)

# Function to print the progress bar in terminal
def print_progress(i):
    j = i / total_rows
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('='*int(20*j), 100*j))
    sys.stdout.flush()
    sleep(0.25)

# Function to send the email
def send_email(email, link):
    text = """\
    
    Hi,

    Your link is:

    {link}

    {sig}
    """.format(link=link, sig=sig)

    html = """\
    <html>
    <body>
        <p>
        Hi,<br/>
        Your link is:</p>
        {link}
        <br/>
        <br/>
        {sig}
    </body>
    </html>
    """.format(link=link, sig=sig)

    message = MIMEMultipart("alternative")
    message["Subject"] = "Subject"
    message["From"] = email_username

    part1 = MIMEText(text,"plain")
    part2 = MIMEText(html,"html")
    message.attach(part1)
    message.attach(part2)
    message["To"] = email
    to_send = ssl.create_default_context()

    with smtplib.SMTP_SSL(smpt_address, smpt_port, context=to_send) as e:
        e.login(email_username, email_password)
        e.sendmail(email_username,email,message.as_string())

count = 0
for index in data.index:
    email = data['email'][index]
    link = data['link'][index]
    count += 1
    print_progress(count)
    if pd.isna(email) == False:
      send_email(email, link)