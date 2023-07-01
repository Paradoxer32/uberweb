"""
    name: 'err404.py'
    Doc: Return 404 error template.
"""

# Modules.
from flask import render_template


def err404(url):
    """Doc: Return 404 error."""

    # Return 404 error template.
    return render_template('err404.html', current_url=url, favicon_path='images/err404favicon.png'), 404
