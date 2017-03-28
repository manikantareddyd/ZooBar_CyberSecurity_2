from debug import *
from zoodb import *
import rpclib

def transfer(sender, recipient, zoobars):
    with rpclib.client_connect('/banksvc/sock') as c:
        kwargs = {"sender":sender, "recipient":recipient, "zoobars": zoobars}
        ret = c.call('transfer', **kwargs)
        return ret

def balance(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        kwargs = {"username":username}
        ret = c.call('balance', **kwargs)
        return ret

def new_account(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        kwargs = {"username":username}
        ret = c.call('new_account', **kwargs)
        return ret