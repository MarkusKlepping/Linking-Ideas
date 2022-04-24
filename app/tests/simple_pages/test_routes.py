def test_index_success(client):
  # Page loads
  response = client.get('/')
  assert response.status_code == 200

def test_about_success(client):

    response = client.get("/about")
    assert response.status_code == 200

def test_about_me_redirects(client):
  # Page redirects
  response = client.get('/about-me')
  assert response.status_code == 302


def test_legal_download(client):

    response = client.get("/legal")
    assert response.headers["Content-Disposition"] == "attachment; filename=legal.txt"

def test_index_content(client):

    response = client.get("/")
    assert b"Welcome to my cookie shop!" in response.data