import os

from backend import setting
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
from mako.template import Template

class WebListener:

	def __init__(self, player, library_manager):

		self.player = player
		self.library_manager = library_manager

		server_address = ('192.168.42.1', setting.PORT)
		httpd = GHTTPServer(player, library_manager, server_address, RequestHandler)

	  	print('Started web server on port ' + str(setting.PORT) + '\n')
	  	httpd.serve_forever()


class GHTTPServer(HTTPServer):
    def __init__(self, player, library_manager, *args, **kw):
        HTTPServer.__init__(self, *args, **kw)
        self.player = player
        self.library_manager = library_manager


class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
	    rootdir = os.path.dirname(os.path.abspath(__file__)) + '/iface'
	    try:
	        if self.path.endswith('.html'):
	            self.serve_file(rootdir + self.path)
	        elif self.path == "/":
	            self.serve_file(rootdir + '/index.html')
	        elif self.path.startswith('/play'):
	        	id_to_play = self.path.lstrip('/play/')
	        	self.server.player.play(id_to_play)

	    except IOError:
	        self.send_error(404, 'file not found')

	def serve_file(self, file_path):
	    template = Template(filename=file_path)

	    self.send_response(200)
	    self.send_header('Content-type','text-html')
	    self.end_headers()

	    self.wfile.write(template.render(tracks=self.server.library_manager.get_tracks()))
