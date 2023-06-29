# UberWeb, flask web-app generator : A project for fun and passing time, but real !
    You know, man, when it's summer and you don't have any work to do, you can start a web-app generator for your favorite micro-framework!
    And this is 'UberWeb!'
    A fun web framework for geeks and nerds or other people! For web programming lovers!

> What does 'uberweb' mean ?!

 'UberWeb' is made by two words, 'uber' and 'web'. We know what is web, but what does 'uber' mean? In german, it means 'super', 'strong', 'great', or something like this!

# How does it work ?
You can run it manually!
Before everything, we need to clone this repository.

    $ git clone "github.com/Paradoxer32/uberweb"

After that, go to 'uberweb' directory and export a variable for uberweb:

    $ cd uberweb
    $ export uberweb="$(pwd)/uberweb.py"

Now, we have a variable for run uberweb!
Go to your project directory!

    $ mkdir myproject
    $ cd myproject

Then generate your web-app!(in current path):

    $ python $uberweb

For generate web-app in another path, we can use:

    $ python $uberweb --path <your path> 

Or with its short form:

    $ python $uberweb -p <your path> 

And you will have a web-app structure for your project!:

    $ tree
    .
    ├── app.py
    ├── conf.py
    ├── databases
    │   └── db.sqlite3
    ├── public
    │   ├── err404.html
    │   ├── fonts
    │   │   ├── Recursive_Casual-Black.ttf
    │   │   └── Recursive_Monospace_Casual-Light.ttf
    │   ├── images
    │   │   ├── err404favicon.png
    │   │   └── favicon.png
    │   ├── index.html
    │   ├── javascripts
    │   │   └── main.js
    │   └── stylesheets
    │       └── style.css
    └── routes
        ├── err404.py
        └── index.py
    
    8 directories, 13 files


# Contribute with us!
Develop this project and add if you liked Develop this project and add if you liked, add your name in 'DEVELOPERS.md'!
