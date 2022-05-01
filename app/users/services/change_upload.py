def change_upload(form_data, upload):
        idea = form_data.get("idea"),
        contact = form_data.get("contact"),
        team = form_data.get("team"),
        title = form_data.get("title"),
        user_id = user.id
    )
    upload.save()
    return new_upload
