from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
from .models import Cookie



blueprint = Blueprint("simple_pages",__name__)


cookies_data = {
  'chocolate-chip' : {'name': 'Chocolate Chip', 'price': '$1.50'},
  'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': '$1.00'},
  'sugar' : {'name': 'Sugar', 'price': '$0.75'},
  'peanut-butter' : {'name': 'Peanut Butter', 'price': '$0.50'},
  'oatmeal' : {'name': 'Oatmeal', 'price': '$0.25'},
  'salted-caramel' : {'name': 'Salted Caramel', 'price': '$1.00'},
}



@blueprint.route('/cookies/<slug>')
def cookie(slug):
  cookie = Cookie.query.filter_by(slug=slug).first()
  print (cookie)
  return render_template('cookies/show.html', cookie=cookie)


@blueprint.route('/')
def main():
  return render_template('main.html')

@blueprint.route("/about")
def about():
    return render_template("aboutme.html")


@blueprint.route("/about-me")
def about_me():
    return redirect(url_for("simple_pages.about"))

@blueprint.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment= True)
