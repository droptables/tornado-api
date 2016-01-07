import datetime
import time,json
import tornado.escape
import tornado.ioloop
import tornado.web
from Carbonblack.FindComputer import FindCBComputer

class CarbonBlackLookup(tornado.web.RequestHandler):
    def get(self, hostname):
        time.sleep(.5)
        nowtime = time.time()
        timestamp = datetime.datetime.fromtimestamp(nowtime).strftime('%Y-%m-%d %H:%M:%S')
        print (hostname.upper().rstrip())
        cblookup = FindCBComputer.Run(hostname.upper().rstrip())

        if cblookup !=[]:
            ostype=str(cblookup[0]['os_environment_display_string'])
            registrationtime=str(cblookup[0]['registration_time'])
            status=str(cblookup[0]['status'])
            cbagent=True
            print ("[+] Has a Carbon Black Agent")
            response = { 'hostname': str(hostname),
                         'has-agent': str(cbagent),
                         'os': ostype,
                         'status': status,
                         'registrationtime': registrationtime,
                         'timestamp': timestamp }
            self.write(json.dumps(response))
        else:
            print ("[-] Has NO Carbon Black Agent")
            cbagent=False
            response = { 'hostname': str(hostname),
                         'has-agent': str(cbagent),
                         'timestamp': timestamp }
            self.write(json.dumps(response))



application = tornado.web.Application([
    (r"/cblookup/([\w\+%_& ]+)", CarbonBlackLookup)
    ])

if __name__ == "__main__":
    application.listen(80)
    print ("CB Host Lookup API Started.")
    tornado.ioloop.IOLoop.instance().start()