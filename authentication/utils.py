from django.core.mail import EmailMessage



class Util:
    @staticmethod
    def send_email(data):
        email_mssg=EmailMessage(
            subject=data['subject'],
            body=data['body'],
            to=[data['to']]
            )
    