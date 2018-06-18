import hmac
import hashlib
import collections
import json
from requests.auth import AuthBase

class HMACAuth(AuthBase):
    def __init__(self,api_key,api_secret,api_version = "v1"):
        self.api_key = api_key 
        self.api_secret = api_secret
        self.api_version = api_version
    
    def __call__(self,request):
        message = request.url.split("?")[-1] 
        print("debug output: signature data:",message)
        secret = self.api_secret

        if not isinstance(message,bytes):
            message = message.encode()
        if not isinstance(secret,bytes):
            secret = secret.encode()

        signature = hmac.new(secret,message,hashlib.sha256).digest()
        if not isinstance(signature,bytes):
            signature = signature.encode()
        hexsignature = signature.hex()

        request.url = request.url + "&sign={}".format(hexsignature)
        print("debug output: finally request_url: ",request.url)

        return request

