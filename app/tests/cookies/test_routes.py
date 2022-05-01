from app.simple_pages.models import Cookie

def test_cookies_renders_cookies(client):
    #loads and renders page
    new_cookie = Cookie(slug ="chocolate-chip", name ="Chocolate Chip", price = 1.50)
    new_cookie.save()
    response = client.get("/cookies")
    assert b"Chocolate Chip" in response.data