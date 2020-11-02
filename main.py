# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import tweepy, webbrowser
from pip._vendor.distlib.compat import raw_input
import socket
from cherrypy import tools
import Server
from DB_path import DataBase


if __name__ == '__main__':
    con = DataBase.sql_connection()
    DataBase.create_user_device_table(con)
    DataBase.create_device_value_table(con)
    con.close()
    Serverlocal = Server.Server()
    Serverlocal.Start()




