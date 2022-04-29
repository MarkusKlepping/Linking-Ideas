from app.users.models import Upload
from werkzeug.security import generate_password_hash


def create_upload(form_data):
    new_upload = Upload(
        idea = form_data.get("email"),
        contact = form_data.get("username"),
        team = generate_password_hash(form_data.get("password")),
        title = form_data.get("title")
    )
    new_upload.save()
    return new_upload