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

after that, we must define 'uberweb' app-generator path!

    $ export uberweb=./uberweb/uberweb.py

Now, we have a variable for run uberweb!
Go to your project directory!

    $ mkdir myproject
    $ cd myproject

Then generate your web-app!:

    $ python $uberweb

And you will have a web-app structure for your project!:

    $ tree
    .
    ├── app.py
    ├── conf.py
    ├── databases
    │   └── db.sqlite3
    ├── public
    │   ├── fonts
    │   │   ├── Recursive_Casual-Black.ttf
    │   │   └── Recursive_Monospace_Casual-Light.ttf
    │   ├── images
    │   │   └── favicon.png
    │   ├── index.html
    │   ├── javascripts
    │   │   └── main.js
    │   └── stylesheets
    │       └── style.css
    └── routes
        └── index.py

    8 directories, 10 files

# Contribute with us!
Develop this project and add if you liked Develop this project and add if you liked, add your name in 'DEVELOPERS.md'!
