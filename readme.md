# Password Manager

I build this project because I'm tired of lose my password, and I don't want to put all my stuff in some online "cloud, password dashboard" etc...
It's a simple Python password manager. It allows you to securely save secrets with a simple CLI interface.

[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/LeoMbm/password-manager/main/LICENSE.txt)



## Features

 - Secrets are stored in an encrypted SQL database with [PostgreSQL](https://www.postgresql.org/docs/)
 - Within the database, each password and notes are encrypted with a unique salt using [bcrypt](https://pypi.org/project/bcrypt/)
 - Master key is hashed with a unique salt
 - Clipboard cleared automatically
 - Password suggestions with [password-generator-py](https://github.com/gabfl/password-generator-py)
 - Import / Export in Json

## Basic usage
IN PROGRESS..


## Installation and setup

Pwmgm requires `postgres/psycobg2` to be installed on your machine.


### Cloning the project

```bash
# Clone project
git clone https://github.com/LeoMbm/password-manager && cd password-manager

