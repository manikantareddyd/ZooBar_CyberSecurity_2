#!/usr/bin/python

import rpclib
import sys
import bank
from debug import *

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, **kwargs):
        sender = kwargs['sender']
        recipient = kwargs['recipient']
        zoobars = kwargs['zoobars']
        return bank.transfer(sender, recipient, zoobars)
    def rpc_balance(self, **kwargs):
        username = kwargs['username']
        return bank.balance(username)
    def rpc_new_account(self, **kwargs):
        username = kwargs['username']
        return bank.new_account(username)
    


(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
