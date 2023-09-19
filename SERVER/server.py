import socket as socket_library
from Message_protocol import Message
from SERVER import services

ADDRESS = ("127.0.0.1", 1023)
BUFFER_SIZE = 1024

server_socket = socket_library.socket(family=socket_library.AF_INET, type=socket_library.SOCK_DGRAM)
server_socket.bind(ADDRESS)
server_socket.settimeout(300)
clients = {}

while True:
    try:
        data, address = server_socket.recvfrom(BUFFER_SIZE)
        clients[address] = data
    except socket_library.timeout:
        print("No data received. timed out")
        server_socket.close()
        break
    except ConnectionError:
        print("The server is unreachable and will be closed")

    del_keys = []
    for client_address, data in clients.items():
        try:
            msg = Message.decode_request(data.decode("UTF-8"))
            if msg['request'] == '1':
                res = services.createCard(msg["params"]['user_id'], msg["params"]["wallet"], msg["params"]["contract_name"])
            elif msg['request'] == '2':
                res = services.getDataCard(msg["params"]["card_id"])
            elif msg['request'] == '3':
                res = services.payRide(msg["params"]["card_id"], msg["params"]["contract_name"])
            elif msg['request'] == '4':
                res = services.fillWallet(msg["params"]["card_id"], int(msg["params"]["sum"]))
            elif msg['request'] == '5':
                res = services.changeContract(msg["params"]["card_id"], msg["params"]["contract_name"])

            server_socket.sendto(Message.create_answere(msg['request'], res).encode("UTF-8"), client_address)
        except socket_library.timeout:
            print("No message received from", client_address)
            server_socket.close()
            break
        except ConnectionError:
            print(str(client_address) + " is disconnected")
            del_keys.append(client_address)
    for c in del_keys:
        del clients[c]
