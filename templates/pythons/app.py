# Modules.
import conf
from flask import Flask
from routes.index import index
from sqlite3 import connect


# Define web-app.
app = Flask(__name__, template_folder=conf.template_folder)

# Declare static folder.
app.static_folder = conf.static_folder

# Connect to database and its cursor!
db = connect("databases/db.sqlite3")
cursor = db.cursor()

@app.route('/')
def home():
    """Doc: 'home' page."""

    # Define template.
    template = index()

    return template

if __name__ == '__main__':
    # Run!
    app.run(host=conf.host, port=conf.port, debug=conf.debug)

