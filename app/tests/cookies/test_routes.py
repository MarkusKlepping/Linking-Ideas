def test_success_login(client):
    response = client.get("/login")
    assert response.status_code == 200

def test_content_login(client):
    response = client.get("login")
    assert b"Log In" in response.data



def test_success_signup(client):
    response = client.get("/signup")
    assert response.status_code == 200

def test_content_signup(client):
    response = client.get("/signup")
    assert b"Sign Up" in response.data



def test_upload_redirect(client):
    response = client.get("/upload")
    assert response.status_code == 302


