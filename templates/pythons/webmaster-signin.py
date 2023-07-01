# Modules.
from sqlite3 import connect
from rich.console import Console


# Define 'rich' console.
console = Console()

console.print("Welcome to uberweb's signin for webmasters!")

# Start program.
while True:

    goal = console.input("What do you want here? [S:signin-wm, E:edit-wm, N:nothing] ")

    # What is goal?
    # > Create user:
    if goal == 'S' or 


