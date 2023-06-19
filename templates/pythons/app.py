# Modules.
import conf
from flask import Flask
from routes.index import index

# Define web-app.
app = Flask(__name__)


@app.route('/')
def home():
    """Doc: 'home' page."""

    # Define template, database and its cursor!
    template, db, cursor = index()

    return template

if __name__ == '__main__':
    # Run!
    app.run(host=conf.host, port=conf.port, debug=conf.debug)

