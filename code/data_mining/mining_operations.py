from app import app, db
from models import User
from flask_peewee.rest import RestAPI

api = RestAPI(app)

def data():
    return 'this is the data part'

@app.route('/data/get')
def create_user(term = 'default'):
    user = User('username1', 'message1')
    db.session.add(user)
    db.session.commit()
    return "Created user"

@app.route('/data/get')
def get_user():
    return User.query.all()



