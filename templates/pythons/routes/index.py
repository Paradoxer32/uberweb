# Modules
from sqlite3 import connect


def index():
    """Doc: This is 'home' page!"""

    # Connect to database and define a cursor!
    db = connect("databases/db.sqlite3")
    cursor = db.cursor()

    def template():
        """Doc: Return html template."""

        # Read 'index.html' file.
        html = open("public/index.html", 'r').read()
    
        # Replace variables.
        html = html.replace("{{name}}", "Uberweb")
        html = html.replace("{{favicon_path}}", "public/images/favicon.png")

        # Return view!
        return html

    # Return database and template.
    return template(), db, cursor

