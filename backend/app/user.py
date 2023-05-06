class User:   # add ip address from another "User.py" # testing purpose only
    def __init__(self, name, port=""):
        self.name = name
        self.server = None
        self.port = port
    
    def assign_server(self, server):
        self.server = server

    def __repr__(self):
        return f"{self.name}"
        return f"Name: {self.name} || Port: {self.port} || Server: {self.server}"