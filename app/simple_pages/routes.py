from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
# from .models import Cookie
from app.users.models import Upload


blueprint = Blueprint("simple_pages",__name__)


@blueprint.route('/')
def main():

  all_uploads = Upload.query.all()
  return render_template('main.html', all_uploads = all_uploads)

@blueprint.route("/about")
def about():
    return render_template("aboutme.html")


@blueprint.route("/about-me")
def about_me():
    return redirect(url_for("simple_pages.about"))

@blueprint.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment= True)


