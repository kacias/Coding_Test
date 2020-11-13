import socket, select

CONNECTION_LIST = []
NICKNAMES = {}
RECV_BUFFER = 4096
PORT = 5000
HOST = "0.0.0.0"
WELCOME_MESSAGE = "Welcome to the server! Type '/nickname yournicknamehere' to change your nickname!"
 
# Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try:
                socket.send(bytes(message, "UTF-8"))
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)

def logMessage(msg):
    with open("chat_server_log.log", "a") as logfile:
        print("Writing to log file...")
        logfile.write(msg)
 
if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    CONNECTION_LIST.append(server_socket)
 
    print("Chat server started on port " + str(PORT))
 
    while True:
        # Get the list sockets which are ready to be read through select
        (read_sockets,write_sockets,error_sockets) = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                (sockfd, addr) = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                sockfd.send(bytes(WELCOME_MESSAGE, "UTF_8"))
                 
                broadcast_data(sockfd, "[{0}] entered room\n".format(addr))
            else: # there's incoming data
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER).decode("UTF-8")
                    if data:
                        print("Got data from client.")
                        clientName = str(sock.getpeername())
                        # The message is a command.
                        if data[0] == "/":
                            args = data[1:].split(' ', 1)

                            if args[0] == "nickname":
                                nick = args[1].rstrip() # there might be a newline character attached
                                NICKNAMES[clientName] = nick 
                                print("Client set their nickname to '{}'".format(nick))
                            else:
                                unknownCommandString = "Unknown command: '{}'".format(args[0])
                                sock.send(bytes(unknownCommandString, "UTF-8"))
                        else:
                            if clientName in NICKNAMES.keys():
                                clientAlias = NICKNAMES[clientName]
                            else:
                                clientAlias = clientName
 
                            msgToBroadcast = '<' + clientAlias + '> ' + data
                            broadcast_data(sock, "\r" + msgToBroadcast) 
                            print(msgToBroadcast)
                            logMessage(msgToBroadcast)
                 
                except:
                    broadcast_data(sock, "Client ({0}) is offline".format(addr))
                    print("Client ({0}) is offline".format(addr))
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()
