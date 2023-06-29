# Modules.
from os import mkdir
from shutil import copy
from os.path import abspath, exists
from rich import print as cprint


# Define dir and destination directory.
dir = abspath(__file__).replace('uberweb.py', '')
dst_path = abspath('.')

# Declare dirs for create.
dirs = [
        "public",
        "public/images",
        "public/stylesheets",
        "public/javascripts",
        "public/fonts",
        "routes",
        "databases",
        ]

# Declare files for add.
tree = {
        "app.py": f"{dir}templates/pythons/app.py",
        "conf.py": f"{dir}templates/pythons/conf.py",
        "databases/db.sqlite3": f"{dir}templates/databases/db.sqlite3",
        "public/images/favicon.png": f"{dir}templates/images/favicon.png",
        "public/images/err404favicon.png": f"{dir}templates/images/err404favicon.png",
        "public/javascripts/main.js": f"{dir}templates/javascripts/main.js",
        "public/stylesheets/style.css": f"{dir}templates/stylesheets/style.css",
        "public/fonts/Recursive_Casual-Black.ttf": f"{dir}templates/fonts/Recursive_Casual-Black.ttf",
        "public/fonts/Recursive_Monospace_Casual-Light.ttf": f"{dir}templates/fonts/Recursive_Monospace_Casual-Light.ttf",
        "public/index.html": f"{dir}templates/htmls/index.html",
        "public/err404.html": f"{dir}templates/htmls/err404.html",
        "routes/index.py": f"{dir}templates/pythons/routes/index.py",
        "routes/err404.py": f"{dir}templates/pythons/routes/err404.py",
        }

# Create folders.
for fold in dirs:

    # Does this dir exists?
    # Yes!
    if exists(fold):

        cprint(f"[yellow]% '{fold}' exists, Pass.[/yellow]")

        continue 

    else:

        # Make directory.
        mkdir(f"{dst_path}/{fold}")
        cprint(f"[blue]> '{fold}' created.[/blue]")


# Add files, one by one.
for file in tree.keys():

    # Does this file exist?
    # Yes!
    if exists(file):
        
        cprint(f"[red]* In your directory, something called '{file}' exists![/red]")

        continue

    # Yes!
    else:
        
        # Create [copy template] file.
        copy(tree[file], f"{dst_path}/{file}")
        cprint(f"[blue]> '{file}' created.[/blue]")


