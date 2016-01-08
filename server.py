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
        cblookup = FindCBComputer.Run(hostname.upper().rstrip())

        if cblookup !=[]:
            response=[]
            print ("[+] Hostname match found for "+str(hostname))
            for computer in cblookup:
                computer_name=computer['computer_name']
                os_type=str(computer['os_environment_display_string'])
                registration_time=str(computer['registration_time'])
                status=str(computer['status'])
                cbagent=True
                computer['computer_name'] = { 'computer_name': str(computer_name),
                             'has_agent': str(cbagent),
                             'os': os_type,
                             'status': status,
                             'registration_time': registration_time,
                             'timestamp': timestamp }
                response.append(computer['computer_name'])
            self.write(str(response))

        else:
            print ("[-] Has NO Carbon Black Agent")
            cbagent=False
            response = { 'computer_name': str(hostname),
                         'has_agent': str(cbagent),
                         'timestamp': timestamp }
            self.write(json.dumps(response))



application = tornado.web.Application([
    (r"/cblookup/([\w\+%_& ]+)", CarbonBlackLookup)
    ])

if __name__ == "__main__":
    print ("CB Host Lookup API Started.")
    application.listen("80")
    tornado.ioloop.IOLoop.instance().start()