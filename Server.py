import cherrypy
import Root
class Server:
    def __init__(self):
        cherrypy.config.update({
            'server.socket_host': '192.168.1.242',
            'server.socket_port': 88,
            'server.socket_timeout': 500,

        })

    def Start(self):
        cherrypy.quickstart(Root.Root(), '/', {'/': {}})