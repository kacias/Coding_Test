import json
import socket
import sys
import time

class SnakeClient():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        

    def sendSnakeDataGetResponse(self, snakeRequest):
        request_string = json.dumps(snakeRequest)
        print("SnakeClient.sendSnakeDataGetResponse: request_string = ", request_string)
            
        try:
            # Connect to server and send data
            # SOCK_STREAM means a TCP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))
            sock.sendall(bytes(request_string + "\n", "utf-8"))

            # Receive data from the server and shut down
            data = sock.recv(1024)
            while not data:
                print("Waiting for response from server...")
                time.sleep(0.05)
                data = sock.recv(1024)

            print("response received!")
            response = data.decode("UTF-8")

        finally:
            sock.close()

        print("SnakeClient.sendSnakeDataGetResponse: response = ", response)
        return response

request = {"idNum": 1, "direction":0}
client = SnakeClient("localhost", 9999)
response = client.sendSnakeDataGetResponse(request)
print(response)
