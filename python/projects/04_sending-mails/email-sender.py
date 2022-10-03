import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = "sathya swaroop"
email['to'] = "yeswanth2sathya@gmail.com"
email['subject'] = "Trying to send email using python"

email.set_content(html.substitute({'name':'sathya'},'html'))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(email)
    print("Done !")