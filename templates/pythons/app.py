# Modules.
import conf
from flask import Flask
from routes.index import index

# Define web-app.
app = Flask(__name__)

# 'home' page.
@app.route('/')
def home():
    return index()

if __name__ == '__main__':
    # Run!
    app.run(host=conf.host, port=conf.port, debug=conf.debug)

