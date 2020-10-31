import cherrypy
import json
from Config import Config
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
        print("Есть контакт");

        json_string = cherrypy.request.json
        print(json_string["ApiKey"])
        #for dD in json_string:
        #    print (dD["key"])
        #    print (dD["value"])
        print(json_string)
        return("OK")