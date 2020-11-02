import sqlite3
import sys
import traceback
from sqlite3 import Error
from Config import Config

def sql_connection():
    try:
        con = sqlite3.connect(Config.DataPath)
        print("Нормес прошло. ДБ создано")
        return con
    except Error:
        print(Error)

def create_user_device_table(con):
    cursObj = con.cursor()
    try:
        cursObj.execute('CREATE TABLE IF NOT EXISTS userdevices (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, apiKey text NOT NULL, chatid INTEGER NOT NULL)')
        print("Table userdevices created")
        con.commit()
    except Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

def create_device_value_table(con):
    cursObj = con.cursor()
    try:
        cursObj.execute('CREATE TABLE IF NOT EXISTS devicevalue (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, apiKey text  NOT NULL, Key text NOT NULL, valueKey INTEGER)')
        print("Table devicevalue created")
        con.commit()
    except Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

def add_device_to_table(con, apiKey, Key):
    cursObj = con.cursor()
    try:
        cursObj.execute('INSERT INTO devicevalue(apiKey, Key) VALUES(?,?)', [apiKey, Key])
        con.commit()
        print("Device add")
    except Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))


def add_device(con, apiKey, chatid):
    cursObj = con.cursor()
    try:
        cursObj.execute('INSERT INTO userdevices(apiKey, chatid) VALUES(?,?)', [apiKey, chatid,])
        con.commit()
        print("Device add")
    except Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))


def update_value(con, apiKey, key, value):
    cursObj = con.cursor()
    try:
        sql =  f''' UPDATE devicevalue
              SET value = {value} ,
              WHERE apiKey = {apiKey}
              AND
              Key = {key}'''

        cursObj.execute(sql)
        con.commit()
        print("Value update")
    except Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

def get_key(con, apiKey):
    cursObj = con.cursor()
    try:
        sql = '''SELECT Key FROM devicevalue
                WHERE apiKey =?
        '''
        cursObj.execute(sql, (apiKey,))
        results = cursObj.fetchall()
        if (results != 0):
            return results
        else:
            return -1

    except Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))