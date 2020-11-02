import cherrypy
from Config import Config
from DB_path import DataBase

class Root:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, key):
        if(key == Config.key):
            print("Config = 42")
            d = dict(Key=key)
            return(d)
            if(key == ""):
                print("Ну норм")
            else:
                raise cherrypy.HTTPError(503)

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
                DataBase.update_value(con, json_string["apiKey"], raw[0], json_string[raw[0]])
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
        db = DataBase.sql_connection()
        length = DataBase.get_querry_length(db,json_string["apiKey"], json_string["key"])
        db.close()
        return length