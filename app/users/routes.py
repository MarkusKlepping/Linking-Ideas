from distutils.command.upload import upload
from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
from app.users.models import Upload, User
from app.users.services.create_user import create_user
from app.users.services.create_upload import create_upload
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash



blueprint = Blueprint("users",__name__)

@blueprint.get('/signup')
def get_signup():
  return render_template('signup.html')


@blueprint.post('/signup')
def post_signup():

    try:
        if User.query.filter_by(email=request.form.get('email')).first():
            raise Exception ('The email address is already taken.')

        user = create_user(request.form)
        login_user(user)

        print ("User logged in success")
        return redirect(url_for('simple_pages.main'))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
    
        return render_template("signup.html", error=error)



@blueprint.get('/login')
def get_login():

  
  return render_template('login.html')

@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(username=request.form.get("username")).first()

        # Checks
    
        if not user:
            raise Exception("Username not found.")
        elif not check_password_hash(user.password, request.form.get("password")):
            raise Exception("Incorrect Password.")
        # Logic
        login_user(user)
        # View
        return redirect(url_for("simple_pages.main"))
    except Exception as error_message:
        error = error_message or "An error occurred while logging in. Please verify your email and password."
        return render_template("login.html", error=error)
  
  


@blueprint.get('/logout')
def get_logout():
    logout_user()
    return redirect(url_for('simple_pages.main'))


@blueprint.get("/delete_user")
def delete_user():
    current_user.delete()
    return redirect(url_for("users.get_login"))



@blueprint.post('/upload')
def post_upload():

    try:
        if Upload.query.filter_by(title=request.form.get('title')).first():
            raise Exception ('This title is already taken.')

        upload = create_upload(request.form)
        login_user(user)

        print ("Upload successfully")
        return redirect(url_for('simple_pages.upload'))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating an upload. Please make sure to enter valid data.'
    
        return render_template("upload.html", error=error)