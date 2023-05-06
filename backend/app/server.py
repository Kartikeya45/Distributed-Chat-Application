'''
    class Server
        contains all the basic functionalities of a Server
            currently doing only for round-robin for testing purposes
'''

class Server:
    '''
        The init function uses a "class variable" to assign a name to the server
    '''
    counter = 0

    def __init__(self, port):
        self.server_name = 'server' + str(Server.counter)
        Server.counter += 1
        self.port = port
    
    def __repr__(self):
        return f"Server name: {self.server_name} || Port: {self.port}"
        return "<"+self.server_name+">"