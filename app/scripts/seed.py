from app.app import create_app
from app.users.models import User, Upload
from app.users.services.create_user import create_user
from app.users.services.create_upload import create_upload
from app.extensions.database import db

app = create_app()
app.app_context().push()


initial_data = {
  'email': 'initial@code.berlin',
  'password': '12345678',
  'username': 'initialuser'
}

initial_user = create_user(initial_data)



first_upload_data  ={'title':'ExPlore', 'idea': 'We want to create an app which helps you to explore the world', 'contact': 'Explore1994@we.de', 'team': 'Max Mustermann, Mira Musterfrau'}
second_upload_data = {'title':'Your Arch', 'idea': 'The Idea is to share your architecture ideas with the world', 'contact': 'Architecture9933@we.de', 'team': 'Max Mustermann, Mira Musterfrau'}
third_upload_data = {'title':'Plantae', 'idea': 'Plantae is going to be your app for taking care of your plants ', 'contact': 'Plantae3494@we.de', 'team': 'Max Mustermann, Mira Musterfrau'}
fourth_upload_data = {'title':'Fernweh', 'idea': 'Share your most beautiful hiking tracks with yoour friends on our app', 'contact': 'Fernweh2092@we.de', 'team': 'Max Mustermann, Mira Musterfrau'}


create_upload(first_upload_data, initial_user)
create_upload(second_upload_data, initial_user)
create_upload(third_upload_data, initial_user)
create_upload(fourth_upload_data, initial_user)
