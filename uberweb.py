# Modules.
from os import mkdir
from shutil import copytree, copy
from os.path import abspath, exists

# Define dir and destination directory.
dir = abspath(__file__).replace('uberweb.py', '')
dst_path = abspath('.')

# Copy templates and ingredients, if they don't exist!
if not exists("app.py"): copy(f"{dir}templates/pythons/app.py", dst_path)
if not exists("conf.py"): copy(f"{dir}templates/pythons/conf.py", dst_path)
if not exists("public"): mkdir("public")
if not exists("public/images"): mkdir("public/images")
if not exists("public/stylesheets"): mkdir("public/stylesheets")
if not exists("public/javascripts"): mkdir("public/javascripts")
if not exists("public/fonts"): mkdir("public/fonts")
if not exists("routes"): mkdir("routes")
if not exists("databases"): mkdir("databases")
if not exists("databases/db.sqlite3"): copy(f"{dir}templates/databases/db.sqlite3", f"{dst_path}/databases")
if not exists("public/images/favicon.png"): copy(f"{dir}templates/images/favicon.png", f"{dst_path}/public/images")
if not exists("public/images/err404favicon.png"): copy(f"{dir}templates/images/err404favicon.png", f"{dst_path}/public/images")
if not exists("public/fonts/Recursive_Casual-Black.ttf"): copy(f"{dir}templates/fonts/Recursive_Casual-Black.ttf", f"{dst_path}/public/fonts")
if not exists("public/fonts/Recursive_Monospace_Casual-Light.ttf"): copy(f"{dir}templates/fonts/Recursive_Monospace_Casual-Light.ttf", f"{dst_path}/public/fonts")
if not exists("public/index.html"): copy(f"{dir}templates/htmls/index.html", f"{dst_path}/public")
if not exists("public/err404.html"): copy(f"{dir}templates/htmls/err404.html", f"{dst_path}/public")
if not exists("public/stylesheets/style.css"): copy(f"{dir}templates/stylesheets/style.css", f"{dst_path}/public/stylesheets")
if not exists("public/javascripts/main.js"): copy(f"{dir}templates/javascripts/main.js", f"{dst_path}/public/javascripts")
if not exists("routes/index.py"): copy(f"{dir}templates/pythons/routes/index.py", f"{dst_path}/routes")
if not exists("routes/err404.py"): copy(f"{dir}templates/pythons/routes/err404.py", f"{dst_path}/routes")

