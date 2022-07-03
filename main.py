# Firstly, I imported the module for psycopg
import argparse
from utils import dbconfig
import sys
import bcrypt
import dotenv
import psycopg2

from simple_term_menu import TerminalMenu

dotenv.load_dotenv()
my_parser = argparse.ArgumentParser(description="Password Manager: Create, Add and Delete account", usage="[options]")

main_menu = ["[A] Create new user", "[B] Log in", "[Q] Exit"]
login_menu = ["[A] Create new data", "[B] View your data"]
loop = True
while loop:
    choice = main_menu[TerminalMenu(main_menu, title="Main menu").show()]

    if choice == "[B] Log in":
        master_username = input("What's your name: ")
        master_password = input("What's your master password: ")

        if master_username != "Chicago" and master_password != "1810":
            print("Login fail")
            sys.exit()
        else:
            print('Welcome in the password manager')
            connection = dbconfig.dbconfig()
            cursor = connection.cursor()

            while loop:
                choice = login_menu[TerminalMenu(login_menu, title="Login menu").show()]
                # my_parser.add_argument("-a", "--add", type=str, nargs=2, help="Add new entry", metavar=("[URL]",
                # "[USERNAME]")) my_parser.add_argument("-q", "--query", type=str, nargs=1, help="Look up entry by
                # USERNAME", metavar="[USERNAME]") my_parser.add_argument("-l", "--list", action="store_true",
                # help="List all account") my_parser.add_argument("-d", "--delete", type=str, nargs=1, help="Delete
                # Account", metavar="[USERNAME]") my_parser.add_argument("-uurl", "--update_url", type=str, nargs=2,
                # help="Update a URL", metavar=("[NEW_URL]", "[OLD_URL]")) my_parser.add_argument("-uuname",
                # "--update_username", type=str, nargs=2, help="Update a username in account", metavar=("[URL]",
                # "[NEW_USERNAME]")) my_parser.add_argument("-upasswd", "--update_password", type=str, nargs=2,
                # help="Update a password in account", metavar=("[URL]", "[NEW_PASSWORD]"))
                #
                # args = my_parser.parse_args()
                if choice == "[A] Create new data":

                    def store_password(usrnm, pwd, url):
                        try:
                            # TODO: WHAT IS CURSOR ?
                            query = "INSERT INTO password (username, password, site) values (%s, %s, %s);"
                            cursor.execute(query, (usrnm, pwd, url))
                            cursor.execute("select * from password;")
                            rows = cursor.fetchall()
                            for r in rows:
                                print(r[0], r[1], r[2], r[3])
                            connection.commit()
                            # cursor.close()
                            connection.close()
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
                            query = "SELECT * FROM password;"
                            cursor.execute(query)
                            rows = cursor.fetchall()
                            for r in rows:
                                print(r[0], r[1], r[2], r[3])
                        except(Exception, psycopg2.Error) as error:
                            print(error)


                    get_data()
    if choice == "[Q] Exit":
        loop = False
