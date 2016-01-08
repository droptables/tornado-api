import requests
from clint.textui import colored

class FindCBComputer(object):

    @staticmethod
    def Run(computername):
    	cbserverurl="URL"
    	cbapitoken="API TOKEN"
        headers = {"X-Auth-Token": cbapitoken}  
        resp = requests.get(cbserverurl+str("/api/v1/sensor?hostname="+str(computername)), headers=headers, verify=False)  
        return resp.json()