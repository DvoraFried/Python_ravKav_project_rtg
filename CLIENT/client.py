import socket as socket_library
from Message_protocol import Message
import json
# Client class -
# Receives an IP and PORT,
# creates a connection to the appropriate server
# and manages the communication with it -
# sending requests, receiving replies and disconnecting the connection:
class Client:
    # Setting up a connection and making initial contact
    def __init__(self, ip, port):
        self.ADDRESS = (ip, port)
        self.BUFFER_SIZE = 1024
        self.client_socket = socket_library.socket(family=socket_library.AF_INET, type=socket_library.SOCK_DGRAM)

    # Sending a request to the server and sending the response back
    def connect(self, request, params):
        msg = Message.create_request(request, params)
        try:
            self.client_socket.sendto(msg.encode("UTF-8"), self.ADDRESS)
            return Message.decode_answere(self.client_socket.recvfrom(self.BUFFER_SIZE)[0].decode("UTF-8"))
        except ConnectionError:
            return dict(status='connectionFails')

    # Disconnection
    def close_connection(self):
        self.client_socket.close()