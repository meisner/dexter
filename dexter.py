#!/usr/bin/python

class DexterNode(object):
    def __init__(self, node_ip):
        # set the node IP address and we need to create a socket
        # possibly, also handle the sending and receiving of commands/code
        self.ip = node_ip

class DexterServer(object):
    def __init__(self, constructor, worker, destructor):
        self.constructor = constructor
        self.worker = worker
        self.destructor = destructor

    def init_nodes(

    def run(self):
        # We make the following assumptions:
        # constructor() and destructor() code runs on the server
        # worker() code executes on each controller node
        self.constructor()
        self.worker()
        self.destructor()

class DexterServerSSH(DexterServer):
    def __init__(self, constructor, worker, destructor):
        super(self, SSHController).__init__(constructor, worker, destructor)
    
    def deploy_code(self, binary):
        # deploys binaries on all the control nodes using SCP -- look at
        # Junjie's code
        pass

    def run(self):
        # overload this method to interpret all the scripts as SSH commands
        pass

def main():
    pass

if __name__ == '__main__':
    main()
