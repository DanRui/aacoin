import requests
from .auth import HMACAuth
import collections

class Api():
    def __init__(self):
        self.session = requests.session()
        self.base_url = "https://api.aacoin.com/v1"

    def _build_session(self,auth):
        self.session.auth = auth 

    def authorize(self,api_key,api_secret):
        self.api_key = api_key 
        self.api_secret = api_secret 
        auth = HMACAuth(api_key,api_secret)
        self._build_session(auth)
        return self

    def accounts_balance(self):
        api_url = self.base_url + "/account/accounts"
        params = {
                "accessKey": self.api_key
        }
        sorted_params = self._sorted_params(params)
        return self.session.post(api_url, params = sorted_params).json()

    def create_order(self,symbol,order_type,quantity,price):
        api_url = self.base_url + "/order/place"
        params = {
            "accessKey": self.api_key,
            "symbol": symbol,
            "type": order_type,
            "quantity": quantity,
            "price": price,
        }
        sorted_params = self._sorted_params(params)
        return self.session.post(api_url,params = sorted_params).json()

    def cancel_order(self,order_id):
        api_url = self.base_url + "/order/cancel"
        params = {
            "accessKey": self.api_key,
            "orderId": order_id
        }
        sorted_params = self._sorted_params(params)
        return self.session.post(api_url,params = sorted_params).json()

    def batchcancel_order(self,order_ids):
        api_url = self.base_url + "order/batchCancel"
        params = {
            "accessKey": self.api_key,
            "orderIds": order_ids 
        }
        sorted_params = self._sorted_params(params)
        return self.session.post(api_url, params = sorted_params).json()
        

    def _sorted_params(self,params):
        sorted_params =  collections.OrderedDict(sorted(params.items()))
        return sorted_params


