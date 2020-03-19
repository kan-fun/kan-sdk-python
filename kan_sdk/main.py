import requests
import base64
import hmac

from typing import List
from hashlib import sha1

def hashBytes(data:bytes, secretKey:bytes)->str:
    h = hmac.new(secretKey, data, sha1)
    return h.hexdigest()

def hashString(s:str, secretKey:bytes)->str:
    return hashBytes(s.encode('utf-8'), secretKey)

class Credential(object):
    def __init__(self,accessKey:str,secretKey:str):
        self.accessKey=accessKey
        self.secretKey=base64.urlsafe_b64decode(secretKey)

    def prepareStringForSign(self, commonParameter, specificParameter)->str:
        commonParameterString = f'{commonParameter["access_key"]}&{commonParameter["signature_nonce"]}&{commonParameter["timestamp"]}'

        keys = specificParameter.keys()
        keys = sorted(keys)

        values = [specificParameter[key] for key in keys]
        specificParameterString = '&'.join(values)

        return f'{commonParameterString}&{specificParameterString}'
    
    def sign(self, commonParameter, specificParameter)->str:
        s = self.prepareStringForSign(commonParameter, specificParameter)
        return hashString(s, self.secretKey)

class Client(object):
    def __init__(self, accessKey:str, secretKey:str):
        self.credential = Credential(accessKey, secretKey)

    def email(self, topic:str, msg:str):
        commonParameter = {
            'access_key': self.credential.accessKey,
            'signature_nonce':'sdfsdf',
            'timestamp': '4242',
        }

        specificParameter = {
            'topic': topic,
            'msg': msg,
        }

        signature = self.credential.sign(commonParameter, specificParameter)
        data = {
            **commonParameter,
            **specificParameter,
            'signature':signature
        }

        requests.post('http://58b5dd3da8514f30a8dfbf42bb0a740c-cn-beijing.alicloudapi.com/send-email', data)