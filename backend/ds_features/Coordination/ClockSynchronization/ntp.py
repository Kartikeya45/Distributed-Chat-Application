import ntplib
import time

class NTPClient:
    first_time = False
    def __init__(self, client, socket):
        self.ntp_client = ntplib.NTPClient()
        self.client = client
        self.time_detla = 0
        self.socket = socket

        if(not NTPClient.first_time):
            NTPClient.first_time = True
            socket.send_string("server_add" + " "+ "NTP")

    
    def get_time(self):
        response = self.ntp_client.request('pool.ntp.org')
        self.socket.send_string("edge"+ " " + str(self) + "," + "NTP")
        self.socket.send_string("highlight_edge_direction " + str(self) + "," + "NTP")
        return response.tx_time
    
    def update_time(self):
        self.time_detla = self.get_time() - time.time()
        self.socket.send_string("highlight_edge_direction_green " + str(self) + "," + "NTP")
        self.socket.send_string("sleep 0.2")
        self.socket.send_string("close_edge " + str(self) + "," + "NTP")
    def get_current_time(self):
        return time.time() + self.time_detla

    def __repr__(self):
        s = str(self.client)
        if(s[0]=='<'):
            return s[1].upper() + s[-2]
        return s[0]+s[-1]