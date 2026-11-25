import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

admin_email = os.getenv("ADMIN_EMAIL", "admin@example.com")
admin_username = os.getenv("ADMIN_USERNAME", "admin")
admin_password = os.getenv("ADMIN_PASSWORD")

if not admin_password:
    raise RuntimeError("Set ADMIN_PASSWORD before creating an administrator account.")

with app.app_context():
    db.create_all()

    if User.query.filter_by(email=admin_email).first():
        print("Admin already exists.")
        raise SystemExit(0)

    admin = User(
        username=admin_username,
        email=admin_email,
        first_name="System",
        last_name="Administrator",
        role="admin",
        is_active=True,
    )

    admin.set_password(admin_password)

    db.session.add(admin)
    db.session.commit()

    print("Admin created successfully.")