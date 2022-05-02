def change_upload(form_data, upload):#

    if form_data.get("idea"):
        upload.idea = form_data.get("idea")
    
    if form_data.get("contact"):
        upload.contact = form_data.get("contact")
    
    if form_data.get("team"):
        upload.team = form_data.get("team")

    if form_data.get("title"):
        upload.title = form_data.get("title")

    upload.save()
    return upload
