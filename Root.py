import cherrypy
from Config import Config
from DB_path import DataBase

class Root:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, key):
        con = DataBase.sql_connection()
        r = DataBase.get_command(con, key)
        d = dict()
        d.update(apiKey = key)
        if len(r)>0:
            for data in r:
                DataBase.delete_command(con, data[0])
                key = str(data[1])
                value = data[2]
                d.update({key:value})
        con.close()
        return(d)


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def senddata(self):
        con = DataBase.sql_connection()
        json_string = cherrypy.request.json
        results = DataBase.get_key(con, json_string["apiKey"])
        print(json_string["apiKey"])

        if (results== -1):
            return("FALSE")
            con.close()
        else:

            for raw in results:
                print(raw[0])
                print(json_string[raw[0]])
                DataBase.update_value(con, json_string["apiKey"], str(raw[0]), json_string[str(raw[0])])
            con.close()
            return("OK")





    @cherrypy.expose()
    @cherrypy.tools.json_in()
    def postKey(self):
        json_string = cherrypy.request.json
        print(json_string["apiKey"])
        print(json_string["key"])
        db = DataBase.sql_connection()
        DataBase.add_device_to_table(db, json_string["apiKey"], json_string["key"])
        db.close()
        return("OK")

    @cherrypy.expose()
    @cherrypy.tools.json_in()
    def registeruser(self):
        json_string = cherrypy.request.json
        print(json_string["apiKey"])
        print(json_string["chatid"])
        db = DataBase.sql_connection()
        DataBase.add_device(db, json_string["apiKey"], json_string["chatid"])
        db.close()
        return("OK")


    @cherrypy.expose()
    @cherrypy.tools.json_in()
    def check_querry_length(self):
        json_string = cherrypy.request.json
        print(json_string["apiKey"])
        print(json_string["key"])
        db = DataBase.sql_connection()
        length = DataBase.get_querry_length(db, json_string["apiKey"], json_string["key"])
        db.close()
        print(length)
        return str(length)

    @cherrypy.expose()
    @cherrypy.tools.json_in()
    def add_command(self):
        json_string = cherrypy.request.json
        apiKey = json_string["apiKey"]
        Key = json_string["Key"]
        value = json_string["value"]
        db = DataBase.sql_connection()
        DataBase.add_query_command(db, apiKey,Key,value)
        db.close()
        return ("ok")