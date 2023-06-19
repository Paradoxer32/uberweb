from os import mkdir
from shutil import copytree, copy
from os.path import abspath

dir = abspath(__file__).replace('uberweb.py', '')
dst_path = abspath('.')

copy(f"{dir}templates/pythons/app.py", dst_path)
copy(f"{dir}templates/pythons/conf.py", dst_path)
mkdir("public")
mkdir("routes")
mkdir("databases")
mkdir("public/images")
mkdir("public/stylesheets")
mkdir("public/javascripts")
mkdir("public/fonts")
copy(f"{dir}templates/databases/db.sqlite3", f"{dst_path}/databases")
copy(f"{dir}templates/images/favicon.png", f"{dst_path}/public/images")
copy(f"{dir}templates/fonts/Recursive_Casual-Black.ttf", f"{dst_path}/public/fonts")
copy(f"{dir}templates/fonts/Recursive_Monospace_Casual-Light.ttf", f"{dst_path}/public/fonts")
copy(f"{dir}templates/htmls/index.html", f"{dst_path}/public")
copy(f"{dir}templates/stylesheets/style.css", f"{dst_path}/public/stylesheets")
copy(f"{dir}templates/javascripts/main.js", f"{dst_path}/public/javascripts")
copy(f"{dir}templates/pythons/routes/index.py", f"{dst_path}/routes")
