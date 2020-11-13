import socket
import sys
from thread import *

HOST = "localhost"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created.")

try:
    s.bind((HOST, PORT))
except (socket.error, msg):
    print("Could not bind to port. Error code: " + str(msg[0]) + ". Message: " + msg[1])
    sys.exit()

print("Socket bind completed.")

# The number argument means the max number of connections to hold.
s.listen(10)
print("Socket now listening")


# Connection handling function.
def clientthread(conn):
    conn.send("Welcome to the server.")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        else:
            reply = 'OK...' + data
            conn.sendall(reply)

    # Close connection once all data received.
    conn.close()

# Begin server loop.
while True:  
    # This is a blocking call:
    (conn, addr) = s.accept()

    # Display client info:
    print("Connected with " + addr[0] + ":" + str(addr[1]))

    # Now talk with client, sending back whatever data they send:
    start_new_thread(clientthread, (conn,))
    
s.close()
