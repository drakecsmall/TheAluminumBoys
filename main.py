import time
import BaseHTTPServer

import header as h
import footer as f
import questions as q

def BuildBody():
    question = "<div id='frame'></div>"
    cuteItemText = '''<a href="#" class="tooltip" style='position:fixed;top:{}vh;left:{}vw;'><img class="cute" src='{}'/>
  <span>{}</span>
</a> '''
    cute_shit = [
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Recycle001.svg/2000px-Recycle001.svg.png",15,15,"The Mobius Loop was introduced in the 1960's to sybolize Reduce, Reuse, and Recycle."],
        ["https://d30y9cdsu7xlg0.cloudfront.net/png/84573-200.png",15,75,"The first self-propelled garbage trucks were introduced in 1897."],
        ["http://www.garbagegoodguys.com/wp/wp-content/themes/thegarbagegoodguys/images/double-bins.png",80,80,"Did you know that refuse collection began as a method for keeping disease and pestilence in check?"],
        ["https://rocketr.net/uploads/c42b8e747ba702.png",100,100,"The first waste to energy plant was put on-line in 1918."],
        ["http://transfinder.com/img/logo.png",50,15,"Transfinder is an industry leader in safe, efficient, and cost-effective transportation management and communication solutions"]

    ]
    cuteItems = "\n".join([cuteItemText.format(i[1],i[2],i[0],i[3]) for i in cute_shit])
    return '''<body>
               {}
              </body>'''.format(question + '\n' + cuteItems)

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
