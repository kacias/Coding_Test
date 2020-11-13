import socket
import sys
import threading
import select

PORT = 9999

class Server():
    def __init__(self, port, max_connections=10):
        self.port = port
        self.max_connections = max_connections

    def startListening(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server.__init__: Socket created.")

        try:
            s.bind(("localhost", self.port))
        except (socket.error, msg):
            print("Could not bind to port. Error code: " + str(msg[0]) + ". Message: " + msg[1])
            sys.exit()

        print("Socket bind completed.")

        s.listen(self.max_connections)
        print("Listening on port " + str(self.port) + ".")
        # Begin server loop.
        while True:  
            (conn, addr) = s.accept()

            print("\nConnected with " + addr[0] + ":" + str(addr[1]))
            print("Spawning new thread to handle request...")
            thread = threading.Thread(target=self.handleConn, args=(conn,))
            thread.start()
            
        s.close()

    def handleConn(self, conn):
        # Loop until all data received.
        while True:
            data = conn.recv(1024)
            if not data:
                print("All data received from client.")
                break
            else:
                message = data.decode("UTF-8")
                print("Received message from client: " + message)

                response = "Hello client!"
                print("Sending back response: " + response)
                conn.sendall(bytes(response, "UTF-8"))

        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    s = Server(PORT)
    s.startListening()
