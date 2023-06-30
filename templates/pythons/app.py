# Modules.
import conf
from flask import Flask, request
from routes.index import index
from routes.err404 import err404
from sqlite3 import connect
from pathlib import Path


# Define web-app.
app = Flask(conf.app_name, template_folder=conf.template_folder)

# Declare static folder.
app.static_folder = conf.static_folder

# Connect to database and its cursor!
db = connect(conf.db)
cursor = db.cursor()

@app.route('/')
def home():
    """Doc: 'home' page."""

    # Define template.
    template = index()

    return template

@app.errorhandler(404)
def PageNotFound(arg):
    """Doc: 404 error page."""
    
    # Get base url. (False url)
    current_url = request.base_url

    return err404(current_url)
    

if __name__ == '__main__':
    # Run!
    app.run(host=conf.host, port=conf.port, debug=conf.debug)

    # Remove all '.pyc' and '.pyo' files and '__pycache__' directories.
    for i in Path('.').rglob('*.py[co]'): i.unlink()
    for i in Path('.').rglob('__pycache__'): i.rmdir()

