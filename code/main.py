from app import app

#enables @app.route('path') that exists in views.py
from views import *

# starting the app.
if __name__ == '__main__':
    app.run(debug=True)
