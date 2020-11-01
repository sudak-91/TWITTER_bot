import cherrypy
import Root
from Config import Config
class Server:
    def __init__(self):
        cherrypy.config.update({
            'server.socket_host': Config.SocketHost,
            'server.socket_port': 9090,
            'server.socket_timeout': 500,

        })

    def Start(self):
        cherrypy.quickstart(Root.Root(), '/', {'/': {}})