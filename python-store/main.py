import sys
import time
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from backend import app, args, PORT

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(PORT)
IOLoop.instance().start()
