from email.message import EmailMessage

import ssl
import smtplib

email_sender ="aveddebbarmaofficial@gmail.com"
email_password= 'evgi cdji ioys tnyv' #Here The password is a relevant password in the context#

email_receiver ='avedebbarmajio@gmail.com'

subject = "Don't forget to subscribe"
body = '''
Email sent to verify python code
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: # 465 just a default number for ports
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,emai, em.as_string())


