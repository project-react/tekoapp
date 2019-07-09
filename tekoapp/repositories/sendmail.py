import config
import smtplib

def send_mail(subject, msg, des_mail):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.FLASK_APP_MAIL_ADRESS, config.FLASK_APP_MAIL_PASSWORD)
        message='Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.FLASK_APP_MAIL_ADRESS, des_mail, message)
        server.quit()
        return True
    except:
        return False