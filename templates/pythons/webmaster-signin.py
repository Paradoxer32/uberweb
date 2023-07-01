# Modules.
from sqlite3 import connect
from rich.console import Console


# Define 'rich' console.
console = Console()

console.print("[green]Welcome to uberweb's signin for webmasters!")


def Exists(username='', email=''):
    """Doc: This function will check does username and email exist?"""

    # Connect to database and its cursor.
    db = conenct("databases/db.sqlite3")
    cursor = db.cursor()

    # Select all names in 'Users' table.
    cursor.execute("SELECT * FROM Users")

    # Declare webmasters' specifications
    rows = cursor.fetchall()

    # Define usernames and emails as empty list.
    usernames, emails = [], []

    # Append usernames and emails in it.
    for r in rows:
        usernames.append(r[0])
        usernames.append(r[2])

    # Does arg-email or arg-username exist in database?
    # Yes!
    if username in usernames:
        return 'username'

    # Yes!
    elif email in emails:
        return 'email'

    # No!
    else:
        return None


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

