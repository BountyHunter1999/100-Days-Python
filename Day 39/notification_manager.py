import os
import smtplib
from twilio.rest import Client

# for running in python anywhere
from twilio.http.http_client import TwilioHttpClient


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self, s_email, email_p, t_token, s_num, t_sid):
        self.s_email = s_email
        self.email_p = email_p
        self.t_token = t_token
        self.s_num = s_num
        self.s_num = s_num
        self.t_sid = t_sid

    def send_email(self, r_email, msg):
        message = f"SUBJECT: LOW PRICE ALERT!!! \n\n{msg}"
        with smtplib.SMTP("smtp.gmail.com") as con:
            con.starttls()
            con.login(self.s_email, self.email_p)
            con.sendmail(self.s_email, r_email, msg=message)

    def send_sms(self, r_num, msg, p_anywhere=False):
        # for python anywhere
        if p_anywhere:
            proxy_client = TwilioHttpClient()
            proxy_client.session.proxies = {"https": os.environ['https_proxy']}
            client = Client(self.t_sid, self.t_token, http_client=proxy_client)
        else:
            # normal
            client = Client(self.t_sid, self.t_token)

        message = client.messages.create(
            body=msg,
            from_=f"{self.s_num}",
            to=f"{r_num}"
        )

        return message.status
