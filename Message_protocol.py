# Message class -
# Used as a protocol:
# manages the encryption and decryption process of the messages passing between
# the client and the server and vice versa,
# so that they comply with an internal convention and suit the activity
import json
class Message:
    # encode message from client to server
    @staticmethod
    def create_request(request, json_params):
        return request + '/' + json_params

    @staticmethod
    def decode_request(request):
        msg = request.split('/')
        return {"request": msg[0], "params": json.loads(msg[1])}

    @staticmethod
    def create_answere(request, result):
        if result == -1:
            return request + '/' + 'Fails' + '/' + json.dumps({"params": result})
        if result:
            return request + '/' + 'Done' + '/' + result
        return request + '/' + 'Done' + '/' + json.dumps({"params": result})

    # decode response from server
    @staticmethod
    def decode_answere(answere):
        msg = answere.split('/')
        return {"status": msg[1], "params": json.loads(msg[2])}
