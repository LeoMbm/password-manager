# Firstly, I imported the module for psycopg
from utils import dbconfig
import sys
import bcrypt
import dotenv
import psycopg2
from getpass import getpass

from simple_term_menu import TerminalMenu
from termcolor import cprint


dotenv.load_dotenv()


main_menu = ["[A] Create new user", "[B] Log in", "[Q] Exit"]
login_menu = ["[A] Create new data", "[B] View your data", "[C] Choice one data by site", "[Q] Exit"]
loop = True
conn = dbconfig.dbconfig()
cur = conn.cursor()
while loop:

    choice = main_menu[TerminalMenu(main_menu, title="Main menu").show()]

    if choice == "[A] Create new user":
        def register_user(username, password):
            try:
                pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
                password_hash = pw.decode('utf8')
                query = "INSERT INTO users (username, master_key) values (%s, %s);"
                cur.execute(query, (username, password_hash))
                conn.commit()
                # cursor.close()
                conn.close()
                cprint('User Created, Please Login Again', 'green', attrs=['bold'])
                sys.exit()
            except Exception as error:
                print(error)
        master_username = input('Type your Username: ')
        master_password = getpass()
        register_user(master_username, master_password)
    if choice == "[B] Log in":
        # def check_password(password):


        def log_in(username, pw):
            query = f"SELECT * from users WHERE username='{username}';"
            cur.execute(query)
            rows = cur.fetchall()
            if not rows:
                cprint("This user doesn't exist", 'red', attrs=['bold'])
                sys.exit()
            for r in rows:
                hash_retrieve = bcrypt.checkpw(pw.encode('utf8'), r[2].encode('utf8'))
                if not hash_retrieve:
                    cprint("Wrong Password", 'red', attrs=['bold'])
                    sys.exit()
                else:
                    cprint('Login Success ! Welcome in the password manager', 'green', attrs=['bold'])


        master_un = input("What's your username: ")
        master_pw = getpass()
        log_in(master_un, master_pw)
        # current usage
        choice = login_menu[TerminalMenu(login_menu, title="Login menu").show()]
        if choice == "[A] Create new data":
            def store_password(usrnm, pwd, url):
                try:
                    # TODO: WHAT IS CURSOR ?
                    req = "INSERT INTO password (username, password, site, user_id) values (%s, %s, %s, %s);"
                    cur.execute(req, (usrnm, pwd, url, 'SELECT id from users where id = %d'))
                    cur.execute("select * from password;")
                    # TODO: STORE PASSWORD WHERE ID = USERNAME
                    rows = cur.fetchall()
                    for r in rows:
                        print(r[0], r[1], r[2], r[3])
                    conn.commit()
                    # cursor.close()
                    conn.close()
                    cprint('Data Added', 'green', attrs=['bold'])
                    # TODO:
                except(Exception, psycopg2.Error) as error:
                    print(error)


            def make_password(password):
                pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                print(bytes(pw))
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
                        cprint(f'Here your data for {i[3]}', 'blue', attrs=['bold'])
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
                        cprint(f'Here your data for {i[3]}', 'blue', attrs=['bold'])
                        print(i[0], i[1], i[2], i[3])

                except(Exception, psycopg2.Error) as error:
                    print(error)


            get_one_data(str(site_input))

        if choice == "[Q] Exit":
            sys.exit()
    if choice == "[Q] Exit":
        sys.exit()



# TODO: WRITE LOGIC
