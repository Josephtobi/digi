from mailjet_rest import Client
import os


class Email:
    @staticmethod
    def send_email(mail):
        api_key = 'd969a9ccad24ff6e6f32e4f4b57dae2d'
        api_secret = '1365c504878997833b4a29633e5b3098'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
            {
            "From": {
                "Email": "josephtobi53@gmail.com",
                "Name": "joseph"
            },
            "To": [
                {
                "Email": mail['to']
                # "Name": "joseph"
                }
            ],
            "Subject": mail['subject'],
            "TextPart": mail['body'],
            # "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
            # "CustomID": "AppGettingStartedTest"
            }
        ]
        }
        result = mailjet.send.create(data=data)
        print (result.status_code)
        print (result.json())

        return {"status code":result.status_code,
                "json":result.json()
                }
