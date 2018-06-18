# aacoin



## How to use

```
import aacoin

api_key = ""
api_secret = ""

api = aacoin.Api()
api.authorize(api_key,api_secret)

print(api.accounts_balance())
print(api.create_order("ethusdt","buy","500","10"))

```
