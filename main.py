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
login_menu = ["[A] Create new data", "[B] View your data", "[C] Choice one data by site"]
loop = True
while loop:
    choice = main_menu[TerminalMenu(main_menu, title="Main menu").show()]

    if choice == "[B] Log in":
        master_password = input("What's your master password: ")

        if master_password != "1810":
            print("Login fail")
            sys.exit()
        else:
            print('Welcome in the password manager')
            connection = dbconfig.dbconfig()
            cursor = connection.cursor()

            while loop:
                choice = login_menu[TerminalMenu(login_menu, title="Login menu").show()]
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
                if choice == "[C] Choice one data by site":
                    site_input = str(input("Type the site: "))


                    def get_one_data(url):
                        try:
                            query = f"SELECT * FROM password WHERE site='{url}';"
                            cursor.execute(query)
                            rows = cursor.fetchall()
                            for r in rows:
                                print(r[0], r[1], r[2], r[3])

                        except(Exception, psycopg2.Error) as error:
                            print(error)


                    get_one_data(str(site_input))
                if choice == "[Q] Exit":
                    loop = False
                    sys.exit()

# TODO: IMPLEMENT LOGIN WITH MASTER PASSWORD

# TODO: WRITE LOGIC
