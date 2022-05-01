from werkzeug.security import generate_password_hash

def change_user(form_data, user):
    user.email = form_data.get("email")
    user.username = form_data.get("username")
    user.password = generate_password_hash(form_data.get("password"))
    
    user.save()
    return user