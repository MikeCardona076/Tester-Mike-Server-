import smtplib 
from email.message import EmailMessage
from decouple import  config

class SendEmail(EmailMessage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['From'] = config('EMAIL_USER')
        self['To'] = config('EMAIL_USER')
        self['Subject'] = 'Tester Mike Notification'
        self.set_content(f'''This is a test email from Tester Mike, unfortunately the server is down''')

    def run_send_email(self):
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(config('EMAIL_USER'), config('EMAIL_PASSWORD'))
            smtp.send_message(self)
            smtp.quit()

