from flask import Blueprint, render_template

blueprint = Blueprint('homework', __name__)


@blueprint.route('/')
def homework():
  return render_template('homework.html')

@blueprint.route('/about')
def about():
  works = ["Screaming Face", "Russian sadness", "Trapped inside my mind", "Loving"]
  return render_template('About.html', works=works)

@blueprint.route('/works')
def works:
  all_works = Works.query.all()
  return render_template('works.html', works=all_works)

@blueprint.route('/works/<slug>')
def works(slug):
  works = Works.query.filter_by(slug=slug).first()
  return render_template('show.html', works=works)

