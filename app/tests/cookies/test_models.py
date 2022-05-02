from app.extensions.database import db
from app.users.models import Upload, User

#test whether ideas can be uploaded
def test_idea_upload(client):

#Create an upload which can be tested
  test_upload = Upload(
    title = "WeWork",
    idea ="We want to change the working world",
    contact ="MiraMusterfrau@we.de",
    team ="Mira Musterfrau & Max Mustermann"
  
  )
  db.session.add(test_upload)
  db.session.commit()
  test_upload.save()

  #Check whether the title of the new upload is "WeWork"
  uploaded_title = Upload.query.filter_by(title="WeWork").first()
  assert uploaded_title.contact == "MiraMusterfrau@we.de"

#Test whether signups work
def test_user_signup(client):
  test_user = User(
    username ="Mira Musterfrau",
    email ="MiraMusterfrau@we.de",
    password ="1234"
  )
  db.session.add(test_user)
  db.session.commit()
 

  #Check whether there is a user with the username "Mira Musterfrau"
  uploaded_user = User.query.filter_by(email="MiraMusterfrau@we.de").first()
  assert uploaded_user.username == "Mira Musterfrau"

#Testing whether changes at the user db work
def test_user_change(client):
  test_user = User(
    username ="Mira Musterfrau",
    email ="MiraMusterfrau@we.de",
    password ="1234"
  )

  db.session.add(test_user)
  db.session.commit()
#Changing the username 
  test_user.username ="Max Mustermann"
  test_user.save()

  updated_user = User.query.filter_by(email="MiraMusterfrau@we.de").first()
  assert updated_user.username == "Max Mustermann"

#User delete Test
def test_user_delete(client):

  test_user = User(
    username ="Mira Musterfrau",
    email ="MiraMusterfrau@we.de",
    password ="1234"
  )

  db.session.add(test_user)
  db.session.commit()

  test_user.delete()

  deleted_user = User.query.filter_by(username="Mira Mustermann").first()
  assert deleted_user is None
