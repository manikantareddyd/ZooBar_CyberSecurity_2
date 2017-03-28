#!/usr/bin/python

import rpclib
import sys
import auth
from debug import *

class AuthRpcServer(rpclib.RpcServer):
    def rpc_login(self, **kwargs):
        username = kwargs['username']
        password = kwargs['password'] 
        return auth.login(username, password)
    def rpc_register(self, **kwargs):
        username = kwargs['username']
        password = kwargs['password'] 
        return auth.login(username, password)
    def rpc_check_token(self, **kwargs):
        username = kwargs['username']
        token = kwargs['token'] 
        return auth.login(username, token)

(_, dummy_zookld_fd, sockpath) = sys.argv

s = AuthRpcServer()
s.run_sockpath_fork(sockpath)
