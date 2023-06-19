
def index():
    """Doc: This is 'home' page!"""
    
    # Read 'index.html' file.
    html = open("../public/index.html", 'r').read()
    
    # Replace variables.
    html = html.replace("{{name}}", "Uberweb")
    html = html.replace("{{favicon_path}}", "../public/images/favicon.png")

    # Return view!
    return html

