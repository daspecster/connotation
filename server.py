import time
import BaseHTTPServer
import urlparse
import json
import sqlite3
import os
import bayes
import urllib

HOST_NAME = 'localhost'
PORT_NUMBER = 80

class APIServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        path = s.path
        print path
        url_variables = urlparse.parse_qs(path[2:])
        bor = bayes.BayesOnRedis(redis_host='localhost', redis_port=6379, redis_db=0)

        text = urllib.unquote(url_variables['text'][0])
        connotation = bor.classify(text)
        s.send_response(200)
        s.end_headers()
        s.wfile.write(connotation)

def start_server():
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), APIServerHandler)
    #print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    start_server()