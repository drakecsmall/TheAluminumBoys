import time
import BaseHTTPServer

import header as h
import footer as f
import questions as q

def BuildBody():
    question = "<div id='frame'></div>"
    return '''<body>
               {}
              </body>'''.format(question)

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type","text/html")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type","text/html")
        s.end_headers()
        s.wfile.write(h.BuildHeader())
        s.wfile.write(BuildBody())
        s.wfile.write(f.BuildFooter())

HOST = "ecitydata.tk"
PORT = 8080

httpd = BaseHTTPServer.HTTPServer((HOST,PORT),Handler)
print time.asctime(), "Server Starts - %s:%s" % (HOST, PORT)
httpd.serve_forever()
