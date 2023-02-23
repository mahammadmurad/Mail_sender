import smtplib
from email.message import EmailMessage

email = EmailMessage ()
email ['from'] = ' ' #enter your name 
email ['to'] = ' '   #enter mail address to send
email ['subject'] = ' ' #enter subject of mail

email.set_content(' ') #write content of mail

with smtplib.SMTP (host= 'smtp.gmail.com' , port= 587 ) as  smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login('#enter your mail address' , '#enter your mail\'s password for applications )
    smtp.send_message(email)

    print('Done!')
