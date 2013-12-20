from flask.ext.script import Manager

from app import app, db
import main

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)

@manager.command
def create_db():
    from models import db
    db.create_all()

@manager.command
def runserver():
    main.app.run(host='0.0.0.0', debug=False)  # unsafe
    #main.app.run(debug=True)

if __name__ == "__main__":
    manager.run()

