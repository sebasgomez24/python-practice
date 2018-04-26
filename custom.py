from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

host = "smtp.gmail.com"
port = 587
username = "s.24.gmz@gmail.com"
password = "iamgroot_2018"
from_email = username
to_list = ["s.24.gmz@gmail.com"]

try:
    email_conn = SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Hello there!"
    the_msg['From'] = from_email
    plain_txt = "Testing the message"
    html_txt = """
    <html>
        <head></head>
        <body>
            <p>Hey!<br/>
                Testing this email <b>message</b>. Made by <a href='http://sebastiangomez.us'>SebasDesigns</a>.
            </p>
        </body>
    </html>
    """
    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("error sending message")

obj = MessageUser()
obj.add_user("Sebastian", 125.34, email='s.24.gmz@gmail.com')
obj.add_user("Javier", 175.23, email='s.24.gmz@gmail.com')
obj.add_user("Maria", 323.22, email='s.24.gmz@gmail.com')
obj.add_user("Nicco", 112.33 email='s.24.gmz@gmail.com')
obj.get_user()
