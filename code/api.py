from flask_peewee.rest import RestAPI, RestResource

from app import app
from models import User

api = RestAPI(app)

class UserResource(RestResource):
    exclude = 'password'

# register our models so they are exposed via /api/<model>/
api.register(User, UserResource)