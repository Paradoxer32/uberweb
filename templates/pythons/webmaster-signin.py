"""
    name: 'webmaster-signin.py'
    Doc: You can add, remove or edit your webmasters with run this file!
"""

# Modules.
from sqlite3 import connect
from rich import print as cprint
from hashlib import sha256
from getpass import getpass



# Connect to database and its cursor.
db = connect("databases/db.sqlite3")
cursor = db.cursor()

# Commit db.
db.commit()

cprint("[green]Welcome to uberweb's signin for webmasters!")


def Exists(arg=''):
    """Doc: This function will check does username and email exist?"""

    # Select all names in 'Webmasters' table.
    cursor.execute("SELECT * FROM Webmasters")

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

    goal = input("What do you want here? [S:signin-wm, R:remove-wm, N:nothing] ")

    # What is goal?
    # > Create user:
    if goal == 'S' or goal == 'signin-wm':
        
        # Get username.
        while True:
            username = input("Username: ")
            if Exists(username):
                cprint(f"[red]* '{username}' user already exists!")
                continue
            break

        # Get email.
        while True:
            email = input("Email: ")
            if not '@' in email or not '.com' in email:
                cprint(f"[red]* Please enter a correct email.")
                continue
            elif Exists(email):
                cprint(f"[red]* '{email}' email already exists!")
                continue
            break

        # Get password.
        password = getpass("Password: ")

        # Get password, again. (If it was match, delete its variable.)
        while True:
            password_again = getpass("Password again: ")
            if password_again != password:
                cprint("[red]* It's not match!")
                continue
            del password_again
            break

        # Encrypt password.
        password = sha256(password.encode('utf-8')).hexdigest()

        # Add user!
        cursor.execute(f"INSERT INTO Webmasters VALUES('{username}', '{email}', '{password}')")

        cprint("[green]Webmaster created successfully!")
        
        # Commit db.
        db.commit()


    # > Remove user:
    elif goal == 'R' or goal == 'remove-wm':
        
        # Get username.
        while True:
            username = input("Username: ")
            if not Exists(username):
                cprint(f"[red]* '{username}' doesn't exist!")
                continue
            break

        # Get user's specifications.
        cursor.execute(f"SELECT * FROM Webmasters WHERE username='{username}'")
        rows = cursor.fetchall()
        row = rows[0]
        db.commit()

        # Get password.
        while True:
            password = getpass("Password: ")
            if sha256(password.encode('utf-8')).hexdigest() != row[2]:
                cprint("[red]* Uncorrect password!")
                continue
            break

        # Are user sure?
        while True:
            sure = input(f"Are sure to remove '{username}' webmaster [y/N]? ")

            # Yes!
            if sure == 'y':
                
                # Delete user!
                cursor.execute(f"DELETE FROM Webmasters WHERE username='{username}'")
                db.commit()

                cprint("[green]> Webmaster removed successfully!")

                break

            # No!
            elif sure == 'N':
                
                cprint("[red] Cancel...")
                
                break

            else:
                cprint("[red]* Yes or No! -> [y/N]")


    elif goal == 'N' or goal == 'nothing':
        
        # Exit program.
        cprint("[red] Exit...")

        exit()

    else:
        # Wrong goal.
        cprint("[red]Please enter 'signin-wm', 'remove-wm' or 'nothing'!('S', 'R' or 'N')")

        continue

