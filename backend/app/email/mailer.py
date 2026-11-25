from flask_mail import Message

from app.extensions import mail


class Mailer:

    @staticmethod
    def send(subject, recipients, body):

        message = Message(

            subject=subject,

            recipients=recipients,

            body=body

        )

        mail.send(message)