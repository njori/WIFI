from app.email.mailer import Mailer
from flask_mail import Message
from app.extensions import mail

class EmailService:

    ADMIN_EMAILS = [

        "admin@company.com"

    ]

    @classmethod
    def router_offline(cls, router):

        Mailer.send(

            subject="Router Offline",

            recipients=cls.ADMIN_EMAILS,

            body=f"""

Router: {router.name}

IP: {router.ip_address}

Status: OFFLINE

Last Seen:

{router.last_seen}

"""

        )

    @classmethod
    def router_online(cls, router):

        Mailer.send(

            subject="Router Online",

            recipients=cls.ADMIN_EMAILS,

            body=f"""

Router:

{router.name}

is online again.

"""

        )

    @classmethod
    def unknown_device(cls, device):

        Mailer.send(

            subject="Unknown Device",

            recipients=cls.ADMIN_EMAILS,

            body=f"""

Device Detected

Hostname:

{device.hostname}

IP:

{device.ip_address}

MAC:

{device.mac_address}

"""

        )

    @classmethod
    def high_cpu(cls, router):

        Mailer.send(

            subject="High CPU Usage",

            recipients=cls.ADMIN_EMAILS,

            body=f"""

Router:

{router.name}

CPU Usage:

{router.cpu_usage}%

"""

        )

    @classmethod
    def high_memory(cls, router):

        Mailer.send(

            subject="High Memory Usage",

            recipients=cls.ADMIN_EMAILS,

            body=f"""

Router:

{router.name}

Memory Usage:

{router.memory_usage}%

"""

        )

    @staticmethod
    def send_report(

        subject,

        body,

        attachment

    ):

        msg = Message(

            subject=subject,

            recipients=["admin@example.com"]

        )

        msg.body = body

        with open(

            attachment,

            "rb"

        ) as fp:

            msg.attach(

                attachment.split("/")[-1],

                "application/octet-stream",

                fp.read()

            )

        mail.send(msg)