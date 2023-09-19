The project consists of a SERVER folder, a CLIENT folder and external PY files: client 1-3, gui and message_protocol.

in short:
How to run the program?
The server.py file must be run in the SERVER\server.py path
followed by each of the external client1-3 files.

Details of the files in the project:

CLIENT\client.py:
Managing the connection with the server - establishing contact, sending and receiving messages and disconnecting.

CLIENT\terminal_gui.py: 
Running client side in terminal interface.

SERVER/createDB:
code to create a DB for the program - to be run only once before starting the program, if no DB exists.

SERVER/RavKav.sqlite: DB file

SERVER/server: 
setting up a server, receiving connections and requests from clients, 
routing to the appropriate functions and returning a response to clients.

SERVER/services: 
functions to perform services offered by the server.

client1.py, client2.py, client3.py: GUI clients

gui.py: 
GUI interface to the program, displays graphics and forwards the requests to the server by creating a client CLIENT/client.py

Message.py: 
a kind of communication protocol between the client and the server, 
including handling the encryption and decryption of the messages according to the internal protocol.