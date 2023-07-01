"""
    name: 'index.py'
    Doc: Function for return 'home' page.
"""

# Modules.
from flask import render_template


def index():
    """Doc: This is 'home' page!"""

    return render_template('index.html', name='Uberweb', favicon_path='images/favicon.png')
