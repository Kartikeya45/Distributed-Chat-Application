class Server:
    '''
        The init function uses a "class variable" to assign a name to the server
    '''
    counter = 0

    def __init__(self):
        self.server_name = 'server' + str(Server.counter)
        Server.counter += 1

    def decrement_counter_when_server_dies(self):
        not NotImplementedError