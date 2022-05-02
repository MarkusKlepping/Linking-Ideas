import math
from random import choice

from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
# from .models import Cookie
from app.users.models import Upload


blueprint = Blueprint("simple_pages",__name__)


image_sources = ["Mountain.jpg", "Interior.jpg","Plant.webp", "Italy.jpg"]


@blueprint.route('/')
def main():

  all_uploads = Upload.query.all()

# loops through the 4 imgs of the list image_sources and assigns them one after another to an upload
  for idx, upload in enumerate(all_uploads):

    upload.image = image_sources[idx % len(image_sources)]


# takes the lenght of the list and splits it in half 
  half_idx = math.floor(len(all_uploads) / 2)
#until half_idx when it is an odd number of uploads
  first_upload_column = all_uploads[:half_idx]
#after half_idx when it is an odd number of uploads
  second_upload_column = all_uploads[half_idx:]
#list with all index this is where the for loop is running over
  upload_columns = [first_upload_column, second_upload_column]
  

  return render_template('main.html', all_uploads = all_uploads, upload_columns=upload_columns)

@blueprint.route("/about")
def about():
    return render_template("aboutme.html")


@blueprint.route("/about-me")
def about_me():
    return redirect(url_for("simple_pages.about"))

