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


@blueprint.route('/cookies')
def cookies():
  page_number = request.args.get('page', 1, type=int)
  print('=> Page number:', page_number)
  cookies_pagination = Cookie.query.paginate(page_number, current_app.config['COOKIES_PER_PAGE'])
  return render_template('login.html', cookies_pagination=cookies_pagination)

@blueprint.route('/')
def index():
  return render_template('index.html')

@blueprint.route("/about")
def about():
    return ("I like cookies")


@blueprint.route("/about-me")
def about_me():
    return redirect(url_for("simple_pages.about"))

@blueprint.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment= True)
