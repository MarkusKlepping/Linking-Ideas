from flask_login import user_logged_in
from app.users.models import Upload



def create_upload(form_data, user):
    new_upload = Upload(
        idea = form_data.get("idea"),
        contact = form_data.get("contact"),
        team = form_data.get("team"),
        title = form_data.get("title"),
        user_id = user.id
    )
    new_upload.save()
    return new_upload