def test_about_success(client):

  response = client.get("/about")
  assert response.status_code == 200

def test_about_me_redirects(client):
  # Page redirects
  response = client.get('/about-me')
  assert response.status_code == 302


def test_main_success(client):
  response = client.get("/")
  assert response.status_code == 200


def test_content_main(client):
  response = client.get("/")
  assert b"Linking Ideas" in response.data