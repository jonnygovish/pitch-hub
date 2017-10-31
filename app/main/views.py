from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch, Category
from flask_login import login_required, current_user
from .forms import PitchForm
from datetime import datetime

@main.route('/')
def index():
  """
  """
  category = Category.get_categories()
  title = "Welcome to Pitch Hub"
  return render_template('index.html', title = title, category = category)
@main.route('/category/<int:id>')
def category(id):
  """
  """
  category = Category.query.get(id)
  pitch = Pitch.get_pitch(category.id)
  title = "Pitches"

  return render_template('category.html', category = category, pitch = pitch, title = title)

@main.route('/category/pitch/new/<int:id>',methods = ["GET","POST"])
@login_required
def new_pitch(id):
  category = Category.query.filter_by(id=id).first()

  if category is None:
        abort(404)

  form = PitchForm()

  if form.validate_on_submit():
    content = form.content.data
    new_pitch = Pitch(content = content,category_id = category.id,user_id = current_user.id)

    new_pitch.save_pitch()

    return  redirect(url_for('.category', id=category.id))

  title = "New pitch page"
  return render_template('new_pitch.html', pitch_form = form, title = title )


  


























































