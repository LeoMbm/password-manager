# Firstly, I imported the module for psycopg
from utils import dbconfig
import sys
import bcrypt
import dotenv
import psycopg2
from getpass import getpass, getuser

from simple_term_menu import TerminalMenu

dotenv.load_dotenv()

# # Get Password & Encrypt
# master_secret_key = getpass()
# salt = bcrypt.gensalt()
# pw = bcrypt.hashpw(master_secret_key.encode(), salt)
# ## Username & Password needs to be stored somewhere
# # For checking future logins
# ## `pw` would be retrieved from a db, I would prefer keyring APIs
# password_prompt = getpass()
# if not bcrypt.checkpw(password_prompt.encode(), pw):
#     print('Fail')
# else:

main_menu = ["[A] Create new user", "[B] Log in", "[Q] Exit"]
login_menu = ["[A] Create new data", "[B] View your data", "[C] Choice one data by site", "[Q] Exit"]
loop = True
conn = dbconfig.dbconfig()
cur = conn.cursor()
while loop:

    choice = main_menu[TerminalMenu(main_menu, title="Main menu").show()]
    if choice == "[Q] Exit":
        sys.exit()
    if choice == "[A] Create new user":
        def register_user(username, password):
            try:

                salt = bcrypt.gensalt()
                pw = bcrypt.hashpw(password.encode(), salt)
                query = "INSERT INTO users (username, master_key) values (%s, %s);"
                cur.execute(query, (username, pw))
                conn.commit()
                # cursor.close()
                conn.close()
            except Exception as error:
                print(error)


        master_username = input('Type your Username: ')
        master_password = getpass()
        register_user(master_username, master_password)
    if choice == "[B] Log in":
        def log_in(usnm, pw):
            query = f"SELECT * from users WHERE (master_key='{pw}' );"
            cur.execute(query)
            rows = cur.fetchall()
            for r in rows:
                print(r[0], r[1], r[2])
                if bcrypt.checkpw(pw, str(r[2])):
                    # FIXME: THIS 'IF'DO THINGS WRONG
                    print('Welcome in the password manager')
                else:
                    print("Login fail or user doesnt exist")
                    sys.exit()

            # FIXME: HE DOESNT CHECK THE PASSWORD, ANY PASSWORD WORKS


        master_un = input("What's your username: ")
        master_pw = str(getpass())

        log_in(master_un, master_pw)
while loop:
    choice = login_menu[TerminalMenu(login_menu, title="Login menu").show()]
    if choice == "[A] Create new data":
        def store_password(usrnm, pwd, url):
            try:
                # TODO: WHAT IS CURSOR ?
                req = "INSERT INTO password (username, password, site) values (%s, %s, %s);"
                cur.execute(req, (usrnm, pwd, url))
                cur.execute("select * from password;")
                # TODO: STORE PASSWORD WHERE ID = USERNAME
                rows = cur.fetchall()
                for r in rows:
                    print(r[0], r[1], r[2], r[3])
                conn.commit()
                # cursor.close()
                conn.close()
                # TODO:
            except(Exception, psycopg2.Error) as error:
                print(error)


        def make_password(password):
            pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            print(str(pw))
            return pw


        username_input = input("Type your username/email: ")
        password_input = input("Type your password: ")
        site_input = input("Type the site: ")

        store_password(str(username_input), make_password(str(password_input)), str(site_input))
    if choice == "[B] View your data":
        def get_data():
            try:
                que = "SELECT * FROM password;"
                cur.execute(que)
                row = cur.fetchall()
                for i in row:
                    print(i[1], i[2], i[3])
            except(Exception, psycopg2.Error) as error:
                print(error)


        get_data()
    if choice == "[C] Choice one data by site":
        site_input = str(input("Type the site: "))


        def get_one_data(url):
            try:
                query = f"SELECT * FROM password WHERE site='{url}';"
                cur.execute(query)
                row = cur.fetchall()
                for i in row:
                    print(i[0], i[1], i[2], i[3])

            except(Exception, psycopg2.Error) as error:
                print(error)


        get_one_data(str(site_input))

    if choice == "[Q] Exit":
        sys.exit()

# TODO: IMPLEMENT LOGIN WITH MASTER PASSWORD

# TODO: WRITE LOGIC
