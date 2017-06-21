from config.brocas import Brocas as BrocasConfig
import requests

class Brocas(object):
    def handle(self, text):      
        payload = {"text": text}
        
        return requests.post(BrocasConfig.getURL(), json=payload);