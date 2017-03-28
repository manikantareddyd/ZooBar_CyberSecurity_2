#!/usr/bin/python

import rpclib
import sys
import bank
import auth_client
from debug import *

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, **kwargs):
        sender = kwargs['sender']
        recipient = kwargs['recipient']
        zoobars = kwargs['zoobars']
        token = kwargs['token']
        if auth_client.check_token(sender, token):
            return bank.transfer(sender, recipient, zoobars)
        else:
            print "Invalid Token"
            return 0
    def rpc_balance(self, **kwargs):
        username = kwargs['username']
        return bank.balance(username)
    def rpc_new_account(self, **kwargs):
        username = kwargs['username']
        return bank.new_account(username)
    


(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
