from werkzeug.security import generate_password_hash

def change_user(form_data, user):
    
    if form_data.get("email"):
        user.email = form_data.get("email")
    
    if form_data.get("username"):
        user.username = form_data.get("username")
    
    if form_data.get("password"):
        user.password = generate_password_hash(form_data.get("password"))
    
    user.save()
    return user