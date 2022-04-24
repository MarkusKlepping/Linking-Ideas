from app.orders.models import Order, Address, CookieOrder
from flask import render_template
from app.cookies.models import Cookie

def create_order(form_data, cookies):
      # Create an order
  order = Order()
  order.save()

  address = Address(
    name= form_data.get('name'),
    street=form_data.get('street'),
    city=form_data.get('city'),
    state=form_data.get('state'),
    zip=form_data.get('zip'),
    country=form_data.get('country'),
    order=order
)
  cookies = Cookie.query.all()

  for cookie in cookies:
    number_of_cookies = form_data.get(cookie.slug, 0)

    if int(number_of_cookies) > 0:
      cookie_order = CookieOrder(
        cookie=cookie,
        order=order,
        number_of_cookies=number_of_cookies
      )
      cookie_order.save()
    return render_template('orders/new.html', cookies=cookies)
    