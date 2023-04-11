#!/usr/bin/python3
"""comments"""

from flask import Flask
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage engine on app context"""
    storage.close()

if __name__ == '__main__':
    from os import environ

    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(environ.get('HBNB_API_PORT', '5000'))

    app.run(host=host, port=port, threaded=True)
