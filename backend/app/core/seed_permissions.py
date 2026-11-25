from app.extensions import db
from app.models.permission import Permission


DEFAULT_PERMISSIONS = [

    ("admin","routers","create"),
    ("admin","routers","update"),
    ("admin","routers","delete"),

    ("admin","networks","create"),
    ("admin","networks","update"),
    ("admin","networks","delete"),

    ("manager","routers","read"),
    ("manager","routers","update"),

    ("manager","devices","read"),

    ("technician","dashboard","read"),

    ("viewer","dashboard","read"),

    ("viewer","routers","read"),

    ("viewer","devices","read"),

]


def seed():

    if Permission.query.count():

        return

    for role, resource, action in DEFAULT_PERMISSIONS:

        db.session.add(

            Permission(

                role=role,

                resource=resource,

                action=action

            )

        )

    db.session.commit()