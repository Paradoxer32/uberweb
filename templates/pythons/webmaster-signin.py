# Modules.
from sqlite3 import connect
from rich.console import Console


# Define 'rich' console.
console = Console()

# Connect to database and its cursor.
db = conenct("databases/db.sqlite3")
cursor = db.cursor()

console.print("[green]Welcome to uberweb's signin for webmasters!")


def Exists(arg=''):
    """Doc: This function will check does username and email exist?"""

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
    if arg in usernames or arg in emails:
        return True

    # No!
    else:
        return False


# Start program.
while True:

    goal = console.input("What do you want here? [S:signin-wm, E:edit-wm, N:nothing] ")

    # What is goal?
    # > Create user:
    if goal == 'S' or goal == 'signin-wm':
        
        # Get username.
        while True:
            username = console.input("Username")
            if Exists(username):
                console.print(f"[red]* '{username}' user already exists!")
                continue

        # Get email.
        while True:
            email = console.input("Email: ")
            if not '@' in email or not '.com' in email:
                console.print(f"[red]* Please enter a correct email.")
                continue
            elif Exists(email):
                console.print(f"[red]* '{email}' email already exists!")
                continue

        # Get password.
        while True:
            password = console.input("Password: ")
        
        # Get password, again.
        while True:
            password_again = console.input("Password again: ")
            if password_again != password:
                console.print("[red]* It's not match!")
                continue

        # Add user!
        cursor.execute(f"INSERT INTO Users VALUES('{username}', '{email}', '{password}')")

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

