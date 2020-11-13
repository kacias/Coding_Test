import socket

HOST = "localhost"
PORT = 9999

class Client():
    def __init__(self, host, port):
        self.port = port

        # Resolve hostname
        try:
            remote_ip = socket.gethostbyname(host)
            print("Client.__init__ - Host IP resolved: " + remote_ip)
            self.host = remote_ip
        except (socket.gaierror):
            # Could not resolve
            print("Client.__init__ - Hostname could not be resolved - exiting.")
            sys.exit()


    def sendMessage(self, msg):
        # Create a TCP socket.
        print("Client.sendMessage - sending message: '{}'".format(msg))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created.")
        except (socket.error, msg):
            print("Failed to create socket. Error code: " + str(msg[0]) + ", Error message: " + msg[1])
            sys.exit()

        print("Attempting to connect...")
        s.connect((self.host, PORT))
        print("Socket connected to " + self.host)

        # Send the message to the server        
        try:
            s.sendall(bytes(msg, "UTF-8"))
            print("Sending message: " + msg)
        except(socket.error):
            print("Send failed.")
            sys.exit()

        binary_response = s.recv(1024)
        response = binary_response.decode("UTF-8")
        print("Response received from server: " + response)
        s.close()

        return response

if __name__ == "__main__":
    c = Client(HOST, PORT)
    response = c.sendMessage("Hello server!")
