# Modules.
from sqlite3 import connect
from rich.console import Console


# Define 'rich' console.
console = Console()

console.print("[green]Welcome to uberweb's signin for webmasters!")

# Start program.
while True:

    goal = console.input("What do you want here? [S:signin-wm, E:edit-wm, N:nothing] ")

    # What is goal?
    # > Create user:
    if goal == 'S' or goal == 'signin-wm':
        pass

    # > Edit user:
    elif goal == 'E' or goal == 'edit-wm':
        pass

    elif goal == 'N' or goal == 'nothing':
        
        # Exit program.
        console.print("[red] Exit...")

        exit()

    else:
        # Wrong goal.
        console.print("[red]Please enter 'signin-wm', 'edit-wm' or 'nothing'!('S', 'E' or 'N')")
        continue

