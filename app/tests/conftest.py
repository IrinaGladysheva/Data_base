from flask_migrate import upgrade
from os import environ

environ['DATABASE_URL'] = 'sqlite://'
app = create_all()

with app.app_context():
  upgrade()
  yield app.test_client()
